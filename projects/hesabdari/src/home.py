import streamlit as st
from utils.database import DatabaseManeger
from utils.time_cheker import in_last_calendar_month
db = DatabaseManeger()


st.title('Dashboard')
st.space(size=50) 
st.subheader('Current Balance')
walletexists = db.wallet.get(DatabaseManeger.query.wallet_id == 2020)
st.header(f'{walletexists['current_balance']:,}') # با جداکننده  نمایش بده
st.space(size=50) 
col1 , col2 = st.columns(2)
with col1:
    getexpense = db.transaction.search(DatabaseManeger.query.transaction_type == 'Expense')
    st.subheader('Monthly Expense')
    results = list(filter(in_last_calendar_month, getexpense))
    monthlyexpense = sum(amu.get('transaction_amount',0) for amu in results)
    st.text(f'{monthlyexpense:,}')
    
with col2:
    st.subheader('Monthly Income')
    getincome = db.transaction.search(DatabaseManeger.query.transaction_type == 'Income')
    results = list(filter(in_last_calendar_month, getincome))
    monthlyincome = sum(inc.get('transaction_amount',0) for inc in results)
    st.text(f'{monthlyincome:,}')

st.space(size=50) 
col3 ,col4 = st.columns([1,3])
col3.subheader('Transactions')
alltransactions = db.get_all(db.transaction)
for transaction in alltransactions:
    st.text(f'Title: {transaction.get('transaction_name')}')
    st.text(f'Date: {transaction.get('transaction_date')}')
    st.text(f'Amount: {transaction.get('transaction_amount')}')
    st.text(f'Type: {transaction.get('transaction_type')}')
    st.divider()