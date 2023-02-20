import streamlit as st
import eda 
import prediction


navigation = st.sidebar.selectbox('Pilihan Halaman : ', ('Explore Data', 'Predict Churn Rsik'))


if navigation == 'Explore Data':
    eda.run()
else:
    prediction.run()
    
