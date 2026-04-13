#  Crop Yield Prediction

##  Overview
This project aims to predict crop yield (in tons per hectare) using machine learning techniques based on environmental and agricultural factors. The goal is to help improve farming decisions and optimize resource utilization.

---

##  Features
- End-to-end Machine Learning pipeline
- Data preprocessing using ColumnTransformer
- Feature engineering (per hectare normalization)
- Model comparison (Linear Regression & Random Forest)
- Final optimized Random Forest model
- Streamlit web application for real-time prediction

---

## Dataset Features
- Crop Type
- Season
- State
- Area (hectare)
- Annual Rainfall (mm)
- Average, Max, Min Temperature (°C)
- Fertilizer usage (per hectare)
- Pesticide usage (per hectare)

---

##  Problem Statement
To build a machine learning model that predicts crop yield based on climatic and agricultural factors, enabling data-driven decision-making in agriculture.

---

##  Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

---

##  Model Performance
- **Algorithm Used:** Random Forest Regressor
- **R² Score:** ~0.96
- **MAE:** Low prediction error
- MAE : 10.244769730827832
- ## Overfitting observed
- Training Accuracy : 0.9945079356262151 
- Testing Accuracy : 0.969210877029393

---

##  Key Insights
- Rainfall and temperature significantly impact crop yield
- Crop type plays a major role in prediction
- Feature engineering improved model performance
- Random Forest outperformed Linear Regression

---

##  Streamlit App
Interactive web app for predicting crop yield based on user input.
streamlit run yield_app.py

---
### Live app 


---

## Model File
Due to GitHub size limitations, the trained model file is not included in this repository.

---
## Project Structure
```
crop-yield-prediction/
│
├── data/
      └──Crop_Yield_Prediction.ipynb
├── notebook/
├── model/
├── app.py
├── requirements.txt
└── README.md
