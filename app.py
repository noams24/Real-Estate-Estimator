import streamlit as st
import pickle
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import numpy as np
import math
from config import cities_encoder, house_types_encoder


def preprocess_input(input):
    input['city'] = cities_encoder[input['city']]
    input['house type'] = house_types_encoder[input['house type']]
    return pd.DataFrame(input, index=[0])


def predict(processed_input):
    sales_model = joblib.load('models/sales_predict.pkl')
    rent_model = joblib.load('models/rent_predict.pkl')

    sale_predicted_price = sales_model.predict(processed_input)
    sale_predicted_price = round(math.exp(sale_predicted_price[0]))

    rent_predicted_price = rent_model.predict(processed_input)
    rent_predicted_price = round(math.exp(rent_predicted_price[0]))
    
    cap_rate = (rent_predicted_price * 12 * 100)/sale_predicted_price
    cap_rate = '{:.3f}'.format(round(cap_rate, 5))

    return sale_predicted_price, rent_predicted_price, cap_rate


def main():
    cities = ['Tel Aviv', 'Jerusalem', 'Haifa', 'Beer Sheva', 'Ramat gan', 'Natanya', 'Petah tikva', 'Rishon lezion', 'Ashdod', 'Ashkelon']
    house_types = ['apartment', 'private house', 'garden apartment', 'penthouse', 'dual family', 'duplex']
    
    # Set app title and description
    st.title("Housing Price Prediction")
    st.write("Enter the details of the house to get the estimated price.")

    # Get user input
    city = st.selectbox("Location", cities).lower()
    house_type = st.selectbox("House Type", house_types)
    rooms = st.number_input("Number of rooms", min_value=2, max_value=10)
    balconies = st.number_input("Number of balconies", min_value=0, max_value=4)
    area = st.slider('Area (in square feet)', 15, 500)
    garden_area = st.slider("Garden area (in square feet)", 0, 300) 
    air_condition = 1 if st.checkbox('Air Condition') else 0
    parking = 1 if st.checkbox('Parking') else 0
    protected_room = 1 if st.checkbox('Protected Room') else 0
    elevator = 1 if st.checkbox('Elevator') else 0
    renovated = 1 if st.checkbox('Renovated') else 0
    furniture = 1 if st.checkbox('Furniture') else 0
    accessibility = 1 if st.checkbox('Accessibility') else 0
    bars = 1 if st.checkbox('Bars') else 0
    storage = 1 if st.checkbox('Storage') else 0

    # when button clicked:
    if st.button("Predict Price"):

      input = {'city': city, 'house type' : house_type, 'house_area': area,
               'garden_area': garden_area,'rooms': rooms,
               'balconies':balconies, 'air_condition': air_condition, 'parking': parking,
                'protected_room': protected_room, 'elevator': elevator, 
                'renovated': renovated, 'furniture': furniture,'accessibility': accessibility,
                'bars': bars,'storage': storage}
    
      processed_input = preprocess_input(input)
      price, rent_price, cap_rate = predict(processed_input)

      # display the result
      col1, col2, col3= st.columns(3)
      col1.markdown("<h4 style='text-align: center; color: white;'>Estimated Price</h4>", unsafe_allow_html=True)
      col2.markdown("<h4 style='text-align: center; color: white;'>Estimated Rent Price</h4>", unsafe_allow_html=True)
      col3.markdown("<h4 style='text-align: center; color: white;'>Estimated Cap Rate</h4>", unsafe_allow_html=True)
      
      col1.success(f"{price:,.0f}₪")
      col2.success(f"{rent_price:,.0f}₪")
      col3.success(f"{cap_rate}%")

    
if __name__ == "__main__":
    main()
