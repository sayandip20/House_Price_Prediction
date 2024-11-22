import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px

@st.cache_data
def load_data():
    data = pd.read_csv('Model/train.csv') 
    data["LONGITUDE"],data["LATITUDE"]=data["LATITUDE"],data["LONGITUDE"]
    data["ADDRESS"]= data["ADDRESS"].str.split(",").str[-1]
    data=data[data["LONGITUDE"].between(65,96) & data["LATITUDE"].between(7,36)]
    return data

data = load_data()

def show_explore_page():
    st.title("Explore Distribution of Parameters")

    st.write("""#### Distribution of property across India map""")
    fig = px.density_mapbox(data, lon='LONGITUDE', lat='LATITUDE', radius=8, zoom=6, mapbox_style='open-street-map')
    st.plotly_chart(fig)
    