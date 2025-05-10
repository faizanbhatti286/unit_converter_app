import streamlit as st

# Set the title of the app
st.title('🌍 Unit Converter 🌟')

# Set the description of the app
category = st.selectbox('Select Category', ['🌍 Distance', '⚖️ Weight', '🌡️ Temperature', '💨 Pressure'])

# Function to render the conversion interface
def render_conversion_ui(category):
    conversion_data = {
        '🌍 Distance': {
            'Meter (m)': 1, 'Kilometer (km)': 1000, 'Miles (mi)': 1609.34, 'Feet (ft)': 0.3048
        },
        '⚖️ Weight': {
            'Gram (g)': 1, 'Kilogram (kg)': 1000, 'Pound (lb)': 453.592, 'Ounce (oz)': 28.3495
        },
        '💨 Pressure': {
            'Pascal (Pa)': 1, 'Bar': 100000, 'Atmosphere (atm)': 101325, 'Torr': 133.322
        },
        '🌡️ Temperature': {
            'Celsius (°C)': 'Celsius', 'Fahrenheit (°F)': 'Fahrenheit', 'Kelvin (K)': 'Kelvin'
        }
    }

    def convert(value, from_unit, to_unit, units):
        if from_unit == to_unit:
            return value
        return value * units[from_unit] / units[to_unit]

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == 'Celsius' and to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif from_unit == 'Celsius' and to_unit == 'Kelvin':
            return value + 273.15
        elif from_unit == 'Fahrenheit' and to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif from_unit == 'Fahrenheit' and to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
        elif from_unit == 'Kelvin' and to_unit == 'Celsius':
            return value - 273.15
        elif from_unit == 'Kelvin' and to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # If the units are the same

    units = list(conversion_data[category].keys())
    from_unit = st.selectbox('From', units)
    to_unit = st.selectbox('To', units)
    value = st.number_input('Enter Value', value=0.0)

    # Convert when button is clicked
    if st.button('🔄 Convert'):
        if category == '🌡️ Temperature':  # Handle temperature conversion separately
            result = convert_temperature(value, from_unit, to_unit)
        else:
            result = convert(value, from_unit, to_unit, conversion_data[category])

        if result is not None:
            st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
        else:
            st.warning("❌ Invalid conversion")

# Show the conversion UI for the selected category
render_conversion_ui(category)




 
         