import requests
import streamlit as st
#pip install -r requirements.txt

st.title("The Currency Converter Calculator")

print("Welcome to the CJB Forex calculator.")

currencies = requests.get("https://api.frankfurter.dev/v1/currencies").json()

print(currencies.keys())

amount = st.number_input("Enter amount", min_value=0.0, value=1.0, step=0.01, format="%.2f")

option = st.selectbox(
    "Enter in the currency you would like to convert from:?",
    list(currencies.keys())
)

st.write("You selected:", option)

selection = st.selectbox(
    "Enter in the currency you would like to convert to:?",
    list(currencies.keys())
)

st.write("You selected:", selection)

if st.button("Selected currency"):
    st.write(f"You are converting {amount} {option} to {selection}")
    response = requests.get(f"https://api.frankfurter.dev/v1/latest?base={option}&symbols={selection}")
    rate = response.json()['rates'][selection]

    st.write(f"{option}/{selection} = {rate}")
    st.write(f"{rate*amount:,} = {selection}") 
             
