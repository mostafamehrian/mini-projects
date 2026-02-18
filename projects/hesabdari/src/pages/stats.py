import streamlit as st
from utils.database import DatabaseManeger
from utils.helpers import Category
from utils.time_cheker import in_last_calendar_month
db = DatabaseManeger()


st.title('Expense Stats')
st.space(size=50) 

# allcats = db.get_all(db.category)
Expensecats = db.category.search(DatabaseManeger.query.category_type == 'Expense')
for category in Expensecats:
    getexpensecatdata = db.transaction.search(DatabaseManeger.query.transaction_type == 'Expense' and 
                                   DatabaseManeger.query.transaction_category_id == category.get('category_id'))
    st.subheader(category.get('category_name'))
    results = list(filter(in_last_calendar_month, getexpensecatdata))
    catmonthlyexpense = sum(amu.get('transaction_amount',0) for amu in results)
    st.text(f'{catmonthlyexpense:,}')
    st.divider()
    
st.title('Income Stats')
st.space(size=50) 

Incomecats = db.category.search(DatabaseManeger.query.category_type == 'Income')
for category in Incomecats:
    getexpensecatdata = db.transaction.search(DatabaseManeger.query.transaction_type == 'Income' and 
                                   DatabaseManeger.query.transaction_category_id == category.get('category_id'))
    st.subheader(category.get('category_name'))
    results = list(filter(in_last_calendar_month, getexpensecatdata))
    catmonthlyexpense = sum(amu.get('transaction_amount',0) for amu in results)
    st.text(f'{catmonthlyexpense:,}')
    st.divider()   
    




