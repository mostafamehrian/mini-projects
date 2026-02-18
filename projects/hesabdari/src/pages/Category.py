import streamlit as st
from utils.database import DatabaseManeger
from utils.helpers import Category

db = DatabaseManeger()


st.title('Category')
st.space(size=50) 

st.subheader('Add Category')

with st.form("user_form", clear_on_submit=True):
    col1 , col2 = st.columns(2)
    catid = col1.text_input('Category Id')
    catname = col2.text_input('Category Name')
    cattype = col1.selectbox('Category Type',['Income','Expense'])
    catcolor = col2.color_picker('Category Color')
    #caticon = str(st.file_uploader('Category Icon'))
    if st.form_submit_button('Add Category'):
        catobj = Category(category_id=int(catid),category_name=catname,
                          category_type=cattype,category_color=catcolor,
                          category_icon=None)
        if catobj.addcategory(userid=3232,DatabaseManeger=db):
            st.success('Successfuly Added')
        else:
            st.error('There is Problem')

           
st.space(size=50) 
st.subheader('Category')
st.space(size=20) 
allcats = db.get_all(db.category)
for category in allcats:
    colid,colname,coltype = st.columns([1,2,1])
    colid.text(F'category id: {category.get('category_id')}')
    colname.text(F'category name: {category.get('category_name')}')
    coltype.text(F'category type: {category.get('category_type')}')
    st.divider()
