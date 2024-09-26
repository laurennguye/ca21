import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Year': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
    'Sales Amount': [24, 27, 22, 30, 25, 29, 31, 26, 28, 32, 35],  # Expanded sales amount to 11 rows
    'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East']  # Expanded regions
}
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
df.to_html('data.html')

st.title("Interactive Sales Dashboard")
st.write("This will display sales data analysis for different regions")
year = st.slider("Choose the year", 2010, 2020)
st.write("Data for the year ", year)
filtered_df =df[df['Year'] == year]
st.write(filtered_df)
if st.button('Show Analysis'):
  st.write('Analysis')

fig, ax = plt.subplots()
ax.bar(filtered_df['Region'], filtered_df['Sales Amount'], color='skyblue')
plt.title(f'Sales in {year}')
plt.xlabel('Region')
plt.ylabel('Sales Amount')
st.pyplot(fig)
