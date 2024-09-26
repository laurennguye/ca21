import streamlit as st
st.title("Interactive Sales Dashboard")
st.write("This will display sales data analysis for different regions")
year = st.slider("Choose the year", 2010, 2020)
st.write("The year is ", year)
if st.button('Show Analysis'):
  st.write('Analysis')
