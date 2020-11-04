import streamlit as st
import pandas as pd
import faiss_algo

st.title('Similarity search using FAISS')

s=st.selectbox('Select the images',('3592260_0.jpg','3778102_2.jpg','3785598_0.jpg'))

slid=st.slider('Select number of images (k) to be retrieved :', 0, 10, 1)

if st.button('Submit'):
	st.text('Selected Image')
	st.image('/images/'+str(s))
	st.text('Matching images')
	images=faiss_algo.faiss_similarity(s,k)
	for i,j in enumerate(images):
		st.image('/images/'+str(images[i]))

