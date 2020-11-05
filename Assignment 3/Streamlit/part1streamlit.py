k import streamlit as st
import os 
import pandas as pd
import requests
from elasticsearch import Elasticsearch 
from PIL import Image
import requests
from io import BytesIO

#os.chdir('N:/Digital Marketing Fall 2020/Streamlit/')

st.title('Elasticsearch using Neural Style Transfer - Tensor Flow')

# df = pd.read_csv('heart.csv')

# if st.checkbox('Show me Training Data'):
#         st.dataframe(df)

# st.dropdown('https://s3.amazonaws.com/kalange-visualsearch/3669338_1.jpg')
# st.button('Submit')



es=Elasticsearch()
s=st.selectbox('Select the images',('3592260_0.jpg','3778102_2.jpg','3785598_0.jpg'))
slid=st.slider('Select number of images (k) to be retrieved :', 0, 10, 1)
if st.button('Submit'):
	st.text('Selected Image')
	res= es.search(index='visual',body={'query':{'match':{'master_pi':'https://s3.amazonaws.com/kalange-visualsearch/'+str(s)}}})
	st.image('https://s3.amazonaws.com/kalange-visualsearch/'+str(s))                                                                                             
	st.text('Matching images')
	d=[]
	for hit in res['hits']['hits']:
	    url=(hit['_source']['similar_pi'])
	    response = requests.get(url)
	    img=Image.open(BytesIO(response.content))
	    d.append(img)
	for i in range(0,slid):
		st.image(d[i])


# age = st.text_input(label='Age')

# gender_ls = ['Male', 'Female']
# sex = st.selectbox('Gender', gender_ls)

# cp_ls = ['Typical Angina', 'Atypical Angina', 'Non-anginal pain', 'Asymptomatic']
# cp = st.multiselect('Chest pain Type', cp_ls)

# restbp = st.slider('Resting Blood Pressure', 0, 220, 120)

# chol = st.slider('Serum Cholesterol in mg/dl', 0, 600, 150)

# fbs_ls = ['fasting blood sugar > 120 mg/dl', 'fasting blood sugar < 120 mg/dl']
# fbs = st.selectbox('Fasting Blood Sugar (>126 mg/dL signals diabetes)', fbs_ls)

# s=['one','two','three']
# cp1 = st.multiselect('Select any', s)

# if st.button('Check Diagnosis'):

#         st.header('A Machine Learning Model would predict this') 