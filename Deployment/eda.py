import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


#melebarkan
st.set_page_config(
    page_title='Customer Churn',
    layout='wide',
    initial_sidebar_state='expanded'

)

st.markdown("""<style>.reportview-container {background: "5160549.jpg"}.sidebar .sidebar-content {background: "5160549.jpg"}</style>""",unsafe_allow_html=True)



def run():

    # Set title
    st.markdown("<h1 style='text-align: center; color: white;'>Customer Churn </h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: grey ;'>Please have a look</h3>", unsafe_allow_html=True)



    # library pillow buat gambar
    image = Image.open('Cust_Churn.jpeg')
    st.markdown('---')
    st.image(image, caption=' "Customer are churning? But.. Why ?" ') 

    # descripsi
    st.write('### Eksplorasi Data Customer ')

    # Membuat Garis lurus
    st.markdown('---')


    # Nampilin dataframe
    st.write('### Customer Details')

    data = pd.read_csv('churn.csv')
    st.dataframe(data.head(5))

    st.markdown('***')
    #barplot
    fig = plt.figure(figsize=(8,5))

    ###########################################
    st.write('### Churn Risk and Feedback')

    # bulan apa saja mereka biasanya cancel ?
    sns.scatterplot(data=data, y=data['feedback'], x=data['avg_time_spent'], hue='churn_risk_score')

    st.write('Kunjungan web yang tidak efektif meningkatkan churn risk.')
    st.write('Feedback yang buruk meningkatkan juga churn risk')


    st.pyplot(fig)
    st.markdown('***')


    ####################################################
    
    # plot membership
    st.write('### Membership and Referral')

    st.write('Lower membership meningkatkan churn risk.')
      
    fig2, (ax1,ax2) = plt.subplots(1, 2,  figsize=(25, 5))
    sns.countplot(data = data[data.churn_risk_score==0],x='membership_category', hue='joined_through_referral', palette=sns.color_palette('pastel'), ax=ax1)
    ax1.set_title('Membership and Refferral (Not Churn)')
    ax1.set_ylim(0,3500)
    sns.countplot(data = data[data.churn_risk_score==1],x='membership_category', hue='joined_through_referral', palette=sns.color_palette('pastel'), ax=ax2)
    ax2.set_title('Membership and Refferral (Churn)')
    ax2.set_ylim(0,3500)

    plt.tight_layout()
    st.pyplot(fig2)
    st.markdown('***')


    ###############################################
    st.write('### Points and Churn Risks')
    st.write('Points menurunkan resiko churn')
    # plotting
    fig4 = sns.displot(data, x='points_in_wallet', hue='churn_risk_score', kind='kde', fill=True, height=5, aspect=1.5)
    plt.axvline(data[data.churn_risk_score==1].points_in_wallet.mean(), ls='--', c='orange')
    plt.axvline(data[data.churn_risk_score==0].points_in_wallet.mean(), ls='--')
    plt.text(350,0.0020, s=round(data[data.churn_risk_score==1].points_in_wallet.mean(),2), fontsize=10, c='orange', weight='bold')
    plt.text(750,0.0020, s=round(data[data.churn_risk_score==0].points_in_wallet.mean(),2), fontsize=10, c='b', weight='bold')


    st.pyplot(fig4)
    st.markdown('***')


    ####################################################


# plot age dan lain ´lain


    st.write('### Log-In Activity')
    st.write('Semakin tinggi frekuensi log-in, semakin tinggi resiko churn')
    fig5, (ax1,ax2) = plt.subplots(1,2, figsize=(25, 5))

    sns.kdeplot(data, x='avg_frequency_login_days', hue='churn_risk_score', ax=ax1, palette=sns.color_palette('bright'), fill=True)
    ax1.set_xlim(0,50)
    ax1.set_title('Log-in Frequency')
    ax1.axvline(19, ls='--', c='r')


    sns.histplot(data, x='days_since_last_login', hue='churn_risk_score', ax=ax2, palette=sns.color_palette('bright'))
    ax2.set_xlim(0,30)
    ax2.set_title('Days Since Last Log-In')
    ax2.axvline(data[data.churn_risk_score==0].avg_frequency_login_days.mean(), ls='--', c='b')


    plt.tight_layout()
    st.pyplot(fig5)

    # plot mengapa login banyak tp kok churn?
    st.write('Poor website performance bisa menjadi alasan untuk tingginya frekuensi log-in customer')
    fig6 = plt.figure(figsize=(10,5))
    sns.scatterplot(data=data[data.churn_risk_score==1] , y='avg_frequency_login_days' ,x='feedback', hue='feedback', legend=None)
    st.pyplot(fig6)

    st.markdown('***')



    #berdasarkan intpput user
    st.write('### Histogram Imputed Users')
    pilihan = st.selectbox('Pilih Kolum : ', ('membership_category', 'internet_option', 'points_in_walle', 'feedback','churn_risk_score'))
    fig=plt.figure(figsize=(15,5))
    sns.histplot(data[pilihan], bins=  30)
    st.pyplot(fig)


    st.markdown('***')



if __name__ == '__main__':
    run()