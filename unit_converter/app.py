import streamlit as st  # Streamlit import karna

# --- Conversion Functions ---

def convert_length(meters=None, feet=None):
    if meters is not None:
        return meters * 3.28084
    elif feet is not None:
        return feet / 3.28084

def convert_weight(kg=None, lbs=None):
    if kg is not None:
        return kg * 2.20462
    elif lbs is not None:
        return lbs / 2.20462

def convert_temperature(celsius=None, fahrenheit=None):
    if celsius is not None:
        return (celsius * 9/5) + 32
    elif fahrenheit is not None:
        return (fahrenheit - 32) * 5/9

# --- Streamlit App Start ---

st.title("🔄 UNIT CONVERTER")

conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# --- Length ---
if conversion_type == "Length":
    option = st.radio("Choose option", ["Meters to Feet", "Feet to Meters"])

    if option == "Meters to Feet":
        meters = st.number_input("Enter length in meters:", min_value=0.0)
        if st.button("Convert"):
            feet = convert_length(meters=meters)
            st.success(f"{meters} meters = {feet:.2f} feet")

    elif option == "Feet to Meters":
        feet = st.number_input("Enter length in feet:", min_value=0.0)
        if st.button("Convert"):
            meters = convert_length(feet=feet)
            st.success(f"{feet} feet = {meters:.2f} meters")

# --- Weight ---
elif conversion_type == "Weight":
    option = st.radio("Choose option", ["Kilograms to Pounds", "Pounds to Kilograms"])

    if option == "Kilograms to Pounds":
        kg = st.number_input("Enter weight in kilograms:", min_value=0.0)
        if st.button("Convert"):
            lbs = convert_weight(kg=kg)
            st.success(f"{kg} kg = {lbs:.2f} lbs")

    elif option == "Pounds to Kilograms":
        lbs = st.number_input("Enter weight in pounds:", min_value=0.0)
        if st.button("Convert"):
            kg = convert_weight(lbs=lbs)
            st.success(f"{lbs} lbs = {kg:.2f} kg")

# --- Temperature ---
elif conversion_type == "Temperature":
    option = st.radio("Choose option", ["Celsius to Fahrenheit", "Fahrenheit to Celsius"])

    if option == "Celsius to Fahrenheit":
        celsius = st.number_input("Enter temperature in Celsius:")
        if st.button("Convert"):
            fahrenheit = convert_temperature(celsius=celsius)
            st.success(f"{celsius}°C = {fahrenheit:.2f}°F")

    elif option == "Fahrenheit to Celsius":
        fahrenheit = st.number_input("Enter temperature in Fahrenheit:")
        if st.button("Convert"):
            celsius = convert_temperature(fahrenheit=fahrenheit)
            st.success(f"{fahrenheit}°F = {celsius:.2f}°C")
