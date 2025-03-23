import streamlit as st

st.title("Unit Convertor App")
st.markdown("### This app is to convert length, weight and time instantly!")
st.write("Welcome! Select a category to enter a value and get the converted result in real time.")

category = st.selectbox("Select a category", ["Length", "Weight", "Time"])

def convert_units(category,value,unit):
    if category == "Length":
        if unit == "meters":
            return value
        elif unit == "centimeters":
            return value * 100
        elif unit == "kilometers":
            return value / 1000
        elif unit == "inches":
            return value * 39.37
        elif unit == "feet":
            return value * 3.281
    elif category == "Weight":
        if unit == "kilograms":
            return value
        elif unit == "Ton":
            return value * 1000
        elif unit == "grams":
            return value / 1000
        elif unit == "pounds":
            return value * 2.205
        elif unit == "ounces":
            return value * 35.274
    elif category == "Time":
        if unit == "seconds":
            return value
        elif unit == "minutes":
            return value * 60
        elif unit == "hours":
            return value * 3600
        elif unit == "days":
            return value * 86400