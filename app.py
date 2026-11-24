import streamlit as st
import pandas as pd
import joblib


model=joblib.load('house price.pkl')

scaler=joblib.load('scaler.pkl')


st.title('House Price Prediction App')

st.write('Enter the details to continue')

income=st.number_input('Average area income',min_value=0.0,value=500000.0)

house_age=st.number_input('Average age of house',min_value=0.0,value=10.0)

rooms=st.number_input('Average area number of rooms',min_value=0.0,value=5.0)

bedrooms=st.number_input('Average area number of bedrooms',min_value=0.0,value=5.0)

population=st.number_input('Average area number of population',min_value=0.0,value=6.0)

if st.button("Predict House Price"):
    st.write("THERE YOU GO!!")

    input_data=pd.DataFrame({
    "Avg. Area Income":[income],
    "Avg. Area House Age":[house_age],
    "Avg. Area Number of Rooms":[rooms],
    "Avg. Area Number of Bedrooms":[bedrooms],
    "Area Population":[population]
    })

    scaled_data=scaler.transform(input_data)
    prediction=model.predict(scaled_data)

    predicted_value=prediction.item()
    st.success(f"Predicted house price: ${predicted_value:,.2f}")


    

