import datetime
import streamlit as st
from utils.database import DatabaseManeger
from utils.helpers import Transaction

db = DatabaseManeger()


st.title('Transaction')
st.space(size=50) 

st.subheader('Add Transaction')

with st.form("user_form", clear_on_submit=True):
    col1 , col2 = st.columns(2)
    tranid = col1.text_input('Transaction Id') #باید خودش ایدی جنریت کنه
    tranname = col2.text_input('Transaction Name')
    trantype = col1.selectbox('Transaction Type',['Income','Expense'],)
    trandate = col2.datetime_input('Transaction Date')
    tranamount = col1.number_input('Transaction Amount')
    allcats = db.get_all(db.category)
    catnames = {cat.get('category_name'):cat.get('category_id') for cat in allcats}
    options = list(catnames)
    trancategory = col2.selectbox('Transaction Category',options=options)
    trancategoryid = catnames[trancategory]
   
    trandescription = st.text_area('Transaction Description')
    
    if st.form_submit_button('Add Transaction'):
        tranobj = Transaction(transaction_amount=tranamount,transaction_category_id=int(trancategoryid),
                              transaction_date=str(trandate),
                              transaction_description=trandescription,transaction_id=int(tranid),
                              transaction_name=tranname,transaction_type=trantype)
        tranobj.addTransaction(wallet_id=3232,DatabaseManeger=db)
        st.success('Successfuly Added')


           
st.space(size=50) 
st.subheader('Transactions')
st.space(size=20) 
alltran = db.get_all(db.transaction)
for Transaction in alltran:
    col3,col4,col5 = st.columns([1,2,1])
    col3.text(F'Transactions id: {Transaction.get('transaction_id')}')
    col4.text(F'Transactions name: {Transaction.get('transaction_name')}')
    col5.text(F'Transactions type: {Transaction.get('transaction_type')}')
    col3.text(F'Transactions Date: {Transaction.get('transaction_date')}')
    col4.text(F'Transactions Amount: {Transaction.get('transaction_amount')}')
    catids = {cat.get('category_id'):cat.get('category_name') for cat in allcats}
    col5.text(F'Transactions category: {catids[Transaction.get('transaction_category_id')]}')
    st.text(F'Transactions description: {Transaction.get('transaction_description')}')
    st.divider()
