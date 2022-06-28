import pickle
import streamlit as st

pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title('Laptop Price Predictor')

# brand
company = st.selectbox('Brand', df['Company'].unique())

# type of laptop
typename = st.selectbox('Type', df['TypeName'].unique())

ram = st.selectbox('RAM(in GB)', [2,4,6,8,12,16,24,32,64])

# Weight
weight = st.number_input('Weight of the laptop')

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
ips = st.selectbox('IPS', ['No', 'Yes'])

# Screen Size
screen_size = st.number_input('Screen Size')

# Resolution
resolution = st.selectbox('Screen Resolution', ['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

# cpu
cpu = st.selectbox('CPU', df['Cpu Brand'].unique())

# HDD
hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])\

gpu = st.selectbox('GPU', df['Gpu Brand'].unique())

os = st.selectbox('OS', df['os'].unique())

if st.button('Predict Price'):
    pass
