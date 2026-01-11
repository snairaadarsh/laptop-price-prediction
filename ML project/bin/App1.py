import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('Pipe.pkl','rb'))
df = pickle.load(open('Df.pkl','rb'))

st.title("Laptop Predictor")

company = st.selectbox('Brand',df['brand'].unique())

specs = st.number_input('Spec_rating of the Laptop')

ram = st.selectbox('RAM(in GB)',[2,4,8,12,16,24,32,64])

ram_types = st.selectbox('RAM types', ["DDR4", "DDR5", "LPDDR5", "LPDDR4X", "LPDDR4",
                                        "LPDDR4x", "Unified"])

rom = st.selectbox('ROM(in GB)',[1,2,32,64,128,256,512])

rom_types = st.selectbox('ROM types',['SSD','Hard-Disk'])

warranty = st.selectbox('Warranty',df['warranty'].unique())

type = st.selectbox('Laptop types',df['type'].unique())

processor = st.selectbox('Processor',["Intel Core i5", "AMD Processor", "Intel Core i7",
                                           "Intel Core i3", "Other Intel Processor", "Apple M1", "Apple M2"])

cores = st.number_input('Cores of the Laptop')

threads = st.number_input('Threads of the Laptop')

gpu = st.selectbox('GPU',df['gpu_brand'].unique())

os = st.selectbox('OS',df['os'].unique())

resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

screen_size = st.slider('Scrensize in inches', 10.0, 18.0, 13.0)

if st.button('Predict Price'):
    # query
    if type == 'Gaming':
        type = 1
    else:
        type = 0

    ppi = None

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = np.sqrt((X_res**2) + (Y_res**2))/screen_size

    query = np.array([company,specs,ram,ram_types,rom,rom_types,warranty,type,ppi,processor,cores,threads,gpu,os])

    query = query.reshape(1,14)
    st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))