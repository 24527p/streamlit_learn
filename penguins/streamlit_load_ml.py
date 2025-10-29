import streamlit as st
import pickle

with open('rfc_model.pkl', 'rb') as f:
    rfc_model = pickle.load(f)

with open('output_uniques.pkl', 'rb') as f:
    output_uniques_map = pickle.load(f)
    
st.subheader('随机森林模型')
st.write(rfc_model)

st.subheader('映射关系实例')

st.write(output_uniques_map[1])