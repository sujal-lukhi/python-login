import streamlit as st

Name = st.text_input("Enter Your Full_Name: ")
Address = st.text_area("Enter Your Text: ")
Hobbiee = st.text_input("Enter Your Hobbiee")
ClassData = st.selectbox("Enter Your Class :",(1, 2, 3, 4, 5, 6, 7, 8))

Button = st.button("Submit")
if Button:
    st.markdown(f"""
                Name : {Name}
                Address : {Address}
                Hobbiee : {Hobbiee}
                ClassData : {ClassData}
                """)
