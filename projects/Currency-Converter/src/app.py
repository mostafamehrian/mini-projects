import streamlit as st
import currencies
from src.main import get_echange_rate,convert_courncy


st.title(':dollar: Currency Converter')

st.markdown(''' 
            this tool allow you to convert currency and get exchange rate
            ''')

currency_list = list(currencies.MONEY_FORMATS.keys())

base_currncy = st.selectbox('Select Base Currency',currency_list)

target_courncy = st.selectbox('Select Target Currency',currency_list)

amount = st.number_input('Enter AMOUNT: ',value=10.00)

echange_rate = get_echange_rate(base_currncy,target_courncy)
convert_amount = convert_courncy(amount,echange_rate)
st.success(f'Exchange Rate is: {echange_rate}')
#st.text(f'{amount} {base_currncy} is {convert_amount} {target_courncy}')
col1 , col2,col3 = st.columns(3)
col1.metric(label='Base currency',value=f'{amount:.4} {base_currncy}')
col2.markdown("<h1 style='text-align:center;margin:0'>&#8594;</h1>",unsafe_allow_html=True)
col3.metric(label='Target Currency',value=f'{convert_amount:.4} {target_courncy}')
