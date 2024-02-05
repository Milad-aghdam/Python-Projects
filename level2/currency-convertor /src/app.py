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

amount = st.number_input("Amount to Convert:", min_value=0.0, value=100.)

if amount > 0 and base_currency and target_currency:
    exchange_rate = convert_currency(base_currency, target_currency)
    
    if exchange_rate:
        converted_amount = calculate_amount(amount, exchange_rate)
        st.success(f"✅ Exchange Rate: {exchange_rate:.2f}")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Base Currency", value=f"{amount:.2f} {base_currency}")
        with col2:
            st.markdown("<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", unsafe_allow_html=True)
        with col3:
            st.metric(label="Target Currency", value=f"{converted_amount:.2f} {target_currency}")
    
    else:
        st.error('Error fetching exchange rate.')
else:
    # Display a warning message
    st.warning('Please enter a valid amount and choose the currencies.')

# Display some information about the tool
st.markdown('---')
st.markdown('### About This Tool')
st.markdown(
    """
    This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
    - The conversion updates automatically as you input the amount or change the currency.
    - Enjoy seamless currency conversion without the need to press a button!
    """
)