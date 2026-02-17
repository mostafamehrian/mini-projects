import json
import os
import streamlit as st
from src.password_generator import PinCodes,RandomPasswords,MemorablePasswords
st.image("./images/pic1.webp")
st.title(":skull: Password Generator")

passoption = st.selectbox(
    "select a password generator",
    ("Pincode Password generator", "Random Password generator","Memorable Password generator")
)

if passoption == "Pincode Password generator":
    passlenght = st.slider("select the lenght of Password",4,100)
    generator = PinCodes(passlenght)
    
    
elif passoption == "Random Password generator":
    passlenght = st.slider("select the lenght of Password",8,100)
    include_number = st.checkbox("include number",False)
    include_symbols = st.checkbox("include symbols",False)
    generator = RandomPasswords(passlenght,include_number,include_symbols)
    
else:
    passlenght = st.slider("select the lenght of Password",8,100)
    seperetaor = st.text_input("enter a seperator","-")
    include_Capitalize = st.checkbox("include Capitalize",False)
    generator = MemorablePasswords(passlenght,seperetaor,include_Capitalize)  

def generatepass():
    password = generator.generate()
    st.write("your password is ready")
    st.code(password, language="text")
    regeneratebutton = st.button("ReGenerate Password")
    if "show_form" not in st.session_state:
        st.session_state.show_form = False

    
    if st.button("Save Password"):
        st.session_state.show_form = True
        
    if st.session_state.show_form:
        with st.form("popup_form"):
            passname = st.text_input("password name")
            st.code(password, language="text")
            submitted = st.form_submit_button("save")
            paasdata = {
                "name":passname,
                "password": password
            }
            if submitted:
            # اگر فایل وجود نداشت، بساز
                if not os.path.exists("passdata.json"):
                    with open("passdata.json", "w", encoding="utf-8") as f:
                        json.dump([], f, ensure_ascii=False)

            # خواندن داده‌های قبلی
                with open("passdata.json", "r", encoding="utf-8") as f:
                    all_data = json.load(f)

            # اضافه کردن داده جدید
                all_data.append(paasdata)

            # نوشتن مجدد کل لیست
                with open("passdata.json", "w", encoding="utf-8") as f:
                    json.dump(all_data, f, ensure_ascii=False, indent=4)

                st.success("Password saved ✅")
                st.session_state.show_form = False




    
def main():
    generatepass()
    if st.button("show password"):
        with open("passdata.json", "r", encoding="utf-8") as file:
            users = json.load(file)
        
        for i,j in enumerate(users):
            password = f"Name is: ``{users[i]['name']}`` and Password is ``{users[i]['password']}``"
            st.code(password, language="text")
            
            
    
    
if __name__=="__main__":
    main()
    
    
# re create password
# save password
## pass name
## pass 
## description
# load password


