# -*- coding: utf-8 -*-
"""fifaAPP.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1REQQAk-fZhAHIvKYMYW8C1Diy0m4FE5W
"""



import numpy as np
import pandas as pd
import pickle
import streamlit as st

# Load the model
loaded_model = pickle.load(open('C:\\Users\\user\\Documents\\ARTIFICIAL INTELIGENCE\\FIFADEPLOYMENT\\best_xgb_model.pkl', 'rb'))

# Load the predictions
predicted_data = pd.read_pickle('C:\\Users\\user\\Documents\\ARTIFICIAL INTELIGENCE\\FIFADEPLOYMENT\\predicted_players_22.pkll')

# Define the prediction function
def fifa_predictions(input_data):
    # Convert input data to numpy array
    input_data = np.array(input_data).reshape(1, -1)
    # Make prediction
    prediction = loaded_model.predict(input_data)
    # Get prediction confidence (if applicable)
    confidence = None
    if hasattr(loaded_model, 'predict_proba'):
        confidence = loaded_model.predict_proba(input_data).max()  # Adjust as per model's predict_proba method
    return prediction, confidence


def main():
    st.title("FIFA Player Rating Prediction")

    # Display existing predictions
    st.header("Existing Predictions")
    st.write(predicted_data)

    st.header("Make New Predictions")

    # Define input fields
    age = st.number_input("Age", min_value=15, max_value=45, value=25)
    overall_rating = st.number_input("Overall Rating", min_value=0, max_value=100, value=70)
    potential = st.number_input("Potential", min_value=0, max_value=100, value=70)
    shooting = st.number_input("Shooting", min_value=0, value=50)
    passing = st.number_input("Passing", min_value=0, value=50)
    dribbling = st.number_input("Dribbling", min_value=0, value=50)
    defending = st.number_input("Defending", min_value=0, value=50)
    physic = st.number_input("Physic", min_value=0, value=50)

    # Collect inputs into a list
    input_data = [age, overall_rating, potential, shooting, passing, dribbling, physic]

    # Make prediction when the button is clicked
    if st.button("Predict Rating"):
        prediction, confidence = fifa_predictions(input_data)
        st.success(f"The predicted rating is: {prediction[0]:.2f}")
        if confidence is not None:
            st.info(f"Confidence: {confidence:.2f}")

if __name__ == '__main__':
    main()



