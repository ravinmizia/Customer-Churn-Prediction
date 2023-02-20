import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from keras import layers
import numpy as np
import pandas as pd
import pickle
import json






# Load All Files

with open('final_pipeline.pkl', 'rb') as file_1:
  model_pipeline = pickle.load(file_1)

model_ann = load_model('churn_risk_model.h5')



def run():

  st.write('## Let us predict!')
  st.markdown('***')

    # Membuat Form
  with st.form(key='form_parameters'):
        name = st.text_input('Name', value='')
        avg_transaction_value = st.number_input('Avg Transaction Value', min_value=800, max_value=100000, step=1, value=1000)
        avg_frequency_login_days = st.number_input('Avg Log-in Frequency (In Days)', min_value=0, max_value=75, value=10)
        points_in_wallet = st.number_input('Points in Wallet', min_value=0, max_value=3000, value=0)

        membership_category = st.selectbox('Select Membership', (('No Membership','Basic Membership','Silver Membership','Premium Membership','Gold Membership','Platinum Membership')))
        feedback = st.selectbox('Select Feedback', (('Poor Website' ,'Poor Customer Service', 'Too many ads','Poor Product Quality' ,'No reason specified' ,'Products always in Stock','Reasonable Price', 'Quality Customer Care', 'User Friendly Website')))

        st.markdown('***')
    
        
        submitted = st.form_submit_button('Lets see!')
        

  data_inf = { 
        'avg_transaction_value': avg_transaction_value, 
        'avg_frequency_login_days': avg_frequency_login_days, 
        'avg_frequency_login_days': avg_frequency_login_days, 
        'points_in_wallet': points_in_wallet, 
        'membership_category': membership_category,
        'feedback': feedback,

    }

  data_inf = pd.DataFrame([data_inf])


  #data transform
  data_inf_transform  = model_pipeline.transform(data_inf)



  st.dataframe(data_inf)

  if submitted:
        
        # Predict using Linear Regression
        y_pred_inf = model_ann.predict(data_inf_transform)
        y_pred_inf = np.where(y_pred_inf>= 0.5,1,0)
        if y_pred_inf == 1:

          st.write('### Possible to churn? : Yup ')

        else:
          st.write('### Possible to churn? : Nope ')



