import streamlit as st
import numpy as np
import pickle 
import sklearn

def load_model():
    with open('Model/model.pkl','rb') as f:
        model = pickle.load(f) 
    return model 

def load_posted_map():
    with open('Model/posted_map.pkl','rb') as f:
        pmap = pickle.load(f)
    return pmap 

def load_yes_map():
    with open('Model/yes_map.pkl','rb') as f:
        ymap = pickle.load(f)
    return ymap

def load_location_map():
    with open('Model/location_map.pkl','rb') as f:
        lmap = pickle.load(f)
    return lmap

def load_scaler():
    with open('Model/scaler.pkl','rb') as f:
        scaler = pickle.load(f)
    return scaler

rf_model = load_model()
posted_map = load_posted_map()
yes_map = load_yes_map()
location_map = load_location_map()
sc = load_scaler()

def show_predict_page():
    st.title("Real Estate Price Prediction")

    local_image_path = "images/house.jpg"
    st.image(local_image_path, use_column_width=True)

    st.write("""### We need some information to predict the price""")

    post = ['Select','Owner', 'Dealer', 'Builder']
    posted_by = st.selectbox("The property has been listed by...", post)

    yes_no = ['Select','Yes', 'No']
    rera = st.selectbox("Is the property RERA approved or not?", yes_no)

    rooms = st.slider("Select the number of rooms...", 1, 6, 2)

    #sq_ft = st.slider("What's the total area of house in square feet?", 1000, 150000, 5000)

    sq_ft = st.text_input("What's the total area of house in square feet?", placeholder='Enter a value between 1000 and 10000')
    #sq_ft = float(sq_ft)

    move = st.selectbox("Is the property ready to move into?",yes_no)

    resale = st.selectbox("Is the property resaled?", yes_no)

    locations = ['Select','Bangalore', 'Mysore', 'Ghaziabad', 'Kolkata', 'Kochi', 'Jaipur', 'Mohali', 'Chennai', 'Siliguri', 'Noida',
                 'Raigad', 'Bhubaneswar', 'Others', 'Pune', 'Mumbai', 'Nagpur', 'Bhiwadi', 'Faridabad', 'Lalitpur', 'Maharashtra',
                 'Vadodara', 'Visakhapatnam', 'Vapi', 'Mangalore', 'Aurangabad', 'Vijayawada', 'Belgaum', 'Bhopal', 'Lucknow', 'Kanpur',
                 'Gandhinagar', 'Pondicherry', 'Agra', 'Ranchi', 'Gurgaon', 'Udupi', 'Indore', 'Jodhpur', 'Coimbatore', 'Valsad', 
                 'Palghar', 'Surat', 'Varanasi', 'Guwahati', 'Amravati', 'Anand', 'Tirupati', 'Secunderabad', 'Raipur', 'Vizianagaram',
                 'Thrissur', 'Madurai', 'Chandigarh', 'Shimla', 'Gwalior', 'Rajkot', 'Sonipat', 'Allahabad', 'Dharuhera', 'Durgapur',
                 'Panchkula', 'Solapur', 'Goa', 'Jamshedpur', 'Jabalpur', 'Hubli', 'Patna', 'Bilaspur', 'Ratnagiri', 'Meerut',
                 'Jalandhar', 'Ludhiana', 'Kota', 'Panaji', 'Kolhapur', 'Ernakulam', 'Bhavnagar', 'Bharuch', 'Asansol', 'Margao',
                 'Bhilai', 'Dehradun', 'Guntur', 'Jalgaon', 'Udaipur', 'Neemrana', 'Sindhudurg', 'Kottayam', 'Dhanbad', 'Navsari',
                 'Bahadurgarh', 'Nellore', 'Haridwar', 'Jamnagar', 'Junagadh', 'Ahmednagar', 'Palakkad', 'Karjat', 'Ajmer', 'Aligarh',
                 'Rudrapur', 'Solan', 'Mathura']
    location = st.selectbox("Enter your preferred location...", locations)

    ok = st.button('Calculate Price')
    if ok:
        X = [posted_by, rera, rooms, sq_ft, move, resale, location]
        X[0] = posted_map[X[0]]
        X[1] = yes_map[X[1]]
        X[4] = yes_map[X[4]]
        X[5] = yes_map[X[5]]
        X[6] = location_map[X[6]]

        val = sc.transform([X])
        price = rf_model.predict(val) 
        st.subheader(f"The estimated price is {price[0]:.2f} Lakhs")