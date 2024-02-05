import streamlit as st
from constants import CURRENCIES
from currency_convertor import convert_currency, calculate_amount


st.set_page_config(page_title="Currency Converter",
                   layout= "centered",
)

st.title(':dollar: Currency Converter')

st.markdown("""
This tool allows you to instantly convert amounts between different currencies 🌍.

Enter the amount and choose the currencies to see the result.
""")

base_currency = st.selectbox("From Currency (base):", CURRENCIES)

target_currency = st.selectbox("To Currency (target):", CURRENCIES) 

amount = st.number_input("Amount to Convert:", min_value=0.0, value="min")

