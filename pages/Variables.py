import streamlit as st

st.title("Learn All About Variables")

st.markdown("A string variable can be declared like this:")

code = '''my_string = "Hello"'''
st.code(code, language='python')