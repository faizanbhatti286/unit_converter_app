import streamlit as st

# Function to convert distance
def distance_convertor(from_unit, to_unit, value):
    units = {
        'Meter': 1,
        'Kilometer': 1000,
        'Miles': 1609.34,
        'Feet': 0.3048
    }
    \
    result = value * units[from_unit] / units[to_unit]
    return result

# Function to convert temperature
def temperature_convertor(from_unit, to_unit, value):
    if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'Celsius' and to_unit == 'Kelvin':
        return value + 273.15
    elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
        return (value - 32) * 5/9
    elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
        return (value + 459.67) * 5/9
    elif from_unit == 'Kelvin' and to_unit == 'Celsius':
        return value - 273.15
    elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
        return (value * 9/5) - 459.67
    return value  # If the units are the same

# Function to convert weight
def weight_convertor(from_unit, to_unit, value):
    units = {
        'Gram': 1,
        'Kilogram': 1000,
        'Pound': 453.592,
        'Ounce': 28.3495
    }
    
    result = value * units[from_unit] / units[to_unit]
    return result

# Function to convert pressure
def pressure_convertor(from_unit, to_unit, value):
    units = {
        'Pascal': 1,
        'Bar': 100000,
        'Atmosphere': 101325,
        'Torr': 133.322
    }
    
    result = value * units[from_unit] / units[to_unit]
    return result

# UI
st.title('Unit Converter')

# Selecting category
category = st.selectbox('Select Category', ['Distance', 'Temperature', 'Weight', 'Pressure'])

# Category-specific unit conversion logic
if category == 'Distance':
    from_unit = st.selectbox('From', ['Meter', 'Kilometer', 'Miles', 'Feet'])
    to_unit = st.selectbox('To', ['Meter', 'Kilometer', 'Miles', 'Feet'])
    value = st.number_input('Enter Value', min_value=0.0)
    if st.button('Convert'):
        result = distance_convertor(from_unit, to_unit, value)
        if result is not None:
            st.success(f'{value} {from_unit} = {result:.2F} {to_unit}')
        else:
            st.error("Invalid unit selected.")

elif category == 'Temperature':
    from_unit = st.selectbox('From', ['Celsius', 'Fahrenheit', 'Kelvin'])
    to_unit = st.selectbox('To', ['Celsius', 'Fahrenheit', 'Kelvin'])
    value = st.number_input('Enter Value')
    if st.button('Convert'):
        result = temperature_convertor(from_unit, to_unit, value)
        st.success(f'{value} {from_unit} = {result:.2F} {to_unit}')

elif category == 'Weight':
    from_unit = st.selectbox('From', ['Gram', 'Kilogram', 'Pound', 'Ounce'])
    to_unit = st.selectbox('To', ['Gram', 'Kilogram', 'Pound', 'Ounce'])
    value = st.number_input('Enter Value', min_value=0.0)
    if st.button('Convert'):
        result = weight_convertor(from_unit, to_unit, value)
        if result is not None:
            st.success(f'{value} {from_unit} = {result:.2F} {to_unit}')
        else:
            st.error("Invalid unit selected.")

elif category == 'Pressure':
    from_unit = st.selectbox('From', ['Pascal', 'Bar', 'Atmosphere', 'Torr'])
    to_unit = st.selectbox('To', ['Pascal', 'Bar', 'Atmosphere', 'Torr'])
    value = st.number_input('Enter Value', min_value=0.0)
    if st.button('Convert'):
        result = pressure_convertor(from_unit, to_unit, value)
        if result is not None:
            st.success(f'{value} {from_unit} = {result:.2F} {to_unit}')
        else:
            st.error("Invalid unit selected.")

 
         