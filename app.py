import streamlit as st
import pickle
import pandas as pd

# Load the model from the pickle file
with open("salary_predictor.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit app
st.title("Salary Predictor")

st.sidebar.header("Input Features")
age = st.sidebar.number_input("Age", min_value=18.0, max_value=70.0, value=25.0, step=1.0)
experience = st.sidebar.number_input("Years of Experience", min_value=0.0, max_value=50.0, value=1.0, step=1.0)

if st.sidebar.button("Predict Salary"):
    # Prepare the data for prediction
    df = pd.DataFrame({
        "YearsExperience": [experience],
        "Age": [age]
    })

    # Predict salary using the loaded model
    predicted_salary = round(model.predict(df)[0], 2)

    st.success(f"The predicted salary is ₹{predicted_salary}")
