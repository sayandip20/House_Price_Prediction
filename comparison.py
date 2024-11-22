import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle 

def load_data_X():
    with open('Model/X.pkl','rb') as f:
        X = pd.read_pickle(f)
    return X

def load_data_Y():
    with open('Model/y.pkl','rb') as f:
        y = pd.read_pickle(f)
    return y

def load_lr_model():
    with open('Model/lr_model.pkl','rb') as f:
        lr_model = pickle.load(f)
    return lr_model 

def load_dt_model():
    with open('Model/dtr_model.pkl','rb') as f:
        dt_model = pickle.load(f)
    return dt_model 

def load_rf_model():
    with open('Model/model.pkl','rb') as f:
        rf_model = pickle.load(f)
    return rf_model 

X = load_data_X()
y = load_data_Y()
lr_model = load_lr_model()
dt_model = load_dt_model()
rf_model = load_rf_model()

def show_comparison_page():
    st.title('Comparison of ML models')

    col = st.selectbox("Select a Model...", ["Multiple Linear Regression", "Decision Tree Regressor", "Random Forest Regressor"])

    if col == "Multiple Linear Regression":
        predicted_values = lr_model.predict(X)
    elif col == "Decision Tree Regressor":
        predicted_values = dt_model.predict(X)
    elif col == "Random Forest Regressor":
        predicted_values = rf_model.predict(X)

    plt.scatter(y, predicted_values, color='blue')
    plt.plot(y, y, color='red', linestyle='--')
    plt.xlabel('Actual Values')
    plt.ylabel('Predicted Values')
    plt.title('Actual vs Predicted Values')
    plt.grid(True)
    st.pyplot()