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
            return value / 1000
        elif unit == "grams":
            return value * 1000
        elif unit == "pounds":
            return value * 2.205
        elif unit == "ounces":
            return value * 35.274
    elif category == "Time":
        if unit == "minutes":
            return value
        elif unit == "seconds":
            return value * 60
        elif unit == "hours":
            return value / 60
        elif unit == "days":
            return value / 1440

if category == "Length":
    length_unit = st.selectbox("Select a unit", ["meters", "centimeters", "kilometers", "inches", "feet"])
elif category == "Weight":
    weight_unit = st.selectbox("Select a unit", ["kilograms", "Ton", "grams", "pounds", "ounces"])
elif category == "Time":
    time_unit = st.selectbox("Select a unit", ["seconds", "minutes", "hours", "days"])

if category == "Length":
    label = "Enter a value in meters"
    min_value = 0.0
    step = 0.1
elif category == "Weight":
    label = "Enter a value in kilograms"
    min_value = 0.0
    step = 0.1
elif category == "Time":
    label = "Enter a value in minutes"
    min_value = 0
    step = 1

value = st.number_input(label, min_value=min_value, step=step)

if st.button("Convert"):
    result = convert_units(category, value, length_unit if category == "Length" else weight_unit if category == "Weight" else time_unit)
    st.success(f"Result: {result} {length_unit if category == 'Length' else weight_unit if category == 'Weight' else time_unit}")
