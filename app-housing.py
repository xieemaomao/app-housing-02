import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('California Housing Data by Hou Miaomiao')
df = pd.read_csv('housing.csv')

median_house_price_filter = st.slider('Median House Price:', 0, 500001, 200000)
df = df[df.median_house_value >= median_house_price_filter]

location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     None)
df = df[df.ocean_proximity.isin(location_filter)]

income_level = st.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))

if income_level == 'Low':
    df = df[df.median_income <= 2.5]
    
elif income_level == 'Medium':
    df = df[(df.median_income <=4.5) & (df.median_income >= 2.5) & (df.median_income != 2.5)] 
else:
    df = df[(df.median_income >= 4.5) & (df.median_income != 4.5)]

st.map(df)

st.subheader('Histogram of the median house value')
fig, ax = plt.subplots(figsize=(20, 10))
df.median_house_value.hist(bins=30)

st.pyplot(fig)