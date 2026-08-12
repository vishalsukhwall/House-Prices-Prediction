# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import joblib
import os

if not os.path.exists("USA_Housing.csv"):
    raise FileNotFoundError("Please ensure USA_Housing.csv is inside this folder!")

df = pd.read_csv("USA_Housing.csv")

# We add 'Area Population' to the training matrix to fix the equation's skew
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Area Population']] 
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

lr_model = LinearRegression()
lr_model.fit(X_train_scaled, y_train)

# Save your balanced model files
os.makedirs("model", exist_ok=True)
joblib.dump(lr_model, "model/linear_house_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("✅ Balanced Kaggle model trained and saved successfully!")