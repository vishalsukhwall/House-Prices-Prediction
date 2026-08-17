# 🏡 House Price Prediction API & Web App

A full-stack machine learning application that predicts real estate prices using a **Linear Regression** model trained on the USA Housing dataset. The project features a trained ML backend and a clean user interface.

---

## 🚀 Features

* **Machine Learning Pipeline:** Data preprocessing, feature scaling (`StandardScaler`), and trained linear regression modeling using `scikit-learn`.
* **Saved Artifacts:** Serialized model and scaler saved securely via `joblib` inside a dedicated `model/` directory.
* **Backend API Integration:** Built to serve predictions seamlessly to a frontend client.
* **Interactive Frontend:** Simple, responsive user interface to input housing parameters and instantly view estimated property values.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, Scikit-Learn, Joblib, OS
* **Frontend:** HTML5, CSS3

---

## 📂 Project Structure

```text
House pricing project/
│
├── backend/
│   ├── USA_Housing.csv       # Dataset used for training
│   ├── requirements.txt      # Python dependencies
│   └── train_model.py        # Model training script
│
├── frontend/
│   ├── index.html            # User interface layout
│   └── style.css             # UI styling and design
│
└── model/
    ├── linear_house_model.pkl # Trained Linear Regression model
    └── scaler.pkl            # Fitted StandardScaler object
