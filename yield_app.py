import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("crop_yield_model.pkl")

st.title("Crop Yield Prediction App")

st.write("Enter details to predict crop yield")

# User Inputs

crop = st.selectbox("Crop", ["Rice", "Wheat", "Maize",'Rice','Maize','Moong(Green Gram)'  ,      
'Urad', 'Groundnut', 'Sesamum',  'Potato' , 'Sugarcane', 'Wheat' ,'Rapeseed & Mustard' , 'Bajra', 'Jowar'  ,                   
'Arhar/Tur','Ragi','Gram','Small millets','Cotton(lint)' ,'Onion' ,'Sunflower' ,'Dry chillies','Other Kharif pulses',       
'Horse-gram' , 'Peas & beans (Pulses)',  'Tobacco', 'Other  Rabi pulses' , 'Soyabean' ,'Turmeric' ,'Masoor' , 'Ginger' ,                   
'Linseed' , 'Castor seed', 'Barley' ,'Sweet potato' , 'Garlic' , 'Banana' , 'Mesta' ,'Tapioca' ,'Coriander' ,'Niger seed' ,              
'Jute' ,'Coconut' ,'Safflower', 'Arecanut' ,'Sannhamp' ,'Other Cereals' , 'Cashewnut'  ,'Cowpea(Lobia)',  'other oilseeds',           
'Black pepper' ,'Moth' , 'Khesari' ,'Cardamom'  ,  'Guar seed ' ,'Oilseeds total' , 'Other Summer Pulses'])

season = st.selectbox("Season", ["Kharif", "Rabi", "Summer","Whole Year","Autumn","Winter"])

state = st.selectbox("State", ['Andhra Pradesh','Arunachal Pradesh' ,'Assam','Bihar','Chhattisgarh','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand',
                               'Karnataka', 'Kerala','Maharashtra','Manipur' ,'Meghalaya','Mizoram','Nagaland','Odisha','Puducherry' ,'Punjab', 'Sikkim', 'Tamil Nadu','Telangana',
                               'Tripura' ,'Uttarakhand','Uttar Pradesh' , 'West Bengal' ])

area = st.number_input("Area",min_value=1.0)

rainfall = st.number_input("Annual Rainfall (mm)")

fert = st.number_input("Fertilizer")

pest = st.number_input("Pesticide")

avg_temp = st.number_input("Average Temperature")

max_temp = st.number_input("Max Temperature")

min_temp = st.number_input("Min Temperature")



# Prediction
if st.button("Predict"):
    input_data = pd.DataFrame({
        'Crop': [crop],
        'Season': [season],
        'State': [state],
        'Area': [area],
        'Annual_Rainfall': [rainfall],
        'Fertilizer': [fert],
        'Pesticide': [pest],
        'Avg_Temperature': [avg_temp],
        'Min_Temperature': [min_temp],
        'Max_Temperature': [max_temp],
         
    })

    prediction = model.predict(input_data)
    st.success(f"Predicted Yield : {prediction[0]:.2f}")
    production = input_data['Area'] * prediction
    st.markdown(f"**Production** : {production[0]:.2f} ")