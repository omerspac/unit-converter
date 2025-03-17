import streamlit as st

conversions = {
    "meter_kilometer": 0.001, # 1 meter = 0.001 kilometer
    "kilometer_meter": 1000, # 1 kilometer = 1000 meters
    "gram_kilogram": 0.001, # 1 gram = 0.001 kilogram
    "kilogram_gram": 1000, # 1 kilogram = 1000 grams
}

def convert_unit(value, unit_from, unit_to):
    key = f"{unit_from}_{unit_to}"

    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported currently!"
    
# UI
st.title("Unit Converter")

value = st.number_input("Enter the value to convert")
unit_from = st.selectbox("Select the unit to convert from", list(conversions.keys()))
unit_to = st.selectbox("Select the unit to convert to", list(conversions.keys()))

if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)
    st.success(f"The converted value is {result}")

# if __name__ == "__main__":
#     main()
