# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model", "linear_house_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "model", "scaler.pkl")

if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("✅ Balanced Regression Model loaded successfully!")
else:
    model, scaler = None, None
    print("⚠️ Warning: Model files missing. Run train_model.py first.")

@app.route('/predict', methods=['POST'])
def predict():
    if not model or not scaler:
        return jsonify({'error': 'Model files are not ready'}), 500

    data = request.get_json()
    
    try:
        income = float(data.get('income'))
        house_age = float(data.get('house_age'))
        rooms = float(data.get('rooms'))
        
        # Enforce a client-side lower threshold
        if income < 10000:
            return jsonify({'error': 'Income must be $10,000 or greater'}), 400
            
        # Standard average population value to keep the regression balance stable
        default_population = 30000.0 
        
        # 1. Map all 4 features into the 2D array
        raw_features = [[income, house_age, rooms, default_population]]
        
        # 2. Scale features 
        scaled_features = scaler.transform(raw_features)
        
        # 3. Process prediction
        predicted_price = model.predict(scaled_features)[0]
        
        # Dataset True Minimum Absolute Floor Value Limit
        DATASET_MIN_PRICE = 20000.0
        if predicted_price < DATASET_MIN_PRICE:
            predicted_price = DATASET_MIN_PRICE
        
        return jsonify({
            'estimated_price': f"${predicted_price:,.2f}"
        })
        
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid matrix payload properties'}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)