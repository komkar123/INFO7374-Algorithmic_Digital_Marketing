import streamlit as st
import pandas as pd
import faiss_algo
import faiss
from PIL import Image
from tempfile import NamedTemporaryFile
import numpy as np
import tensorflow as tf
import io
import pandas as pd

index = faiss.read_index("vector.index")
filenames = sorted(faiss_algo.get_file_list('images'))
df=pd.DataFrame(filenames,columns=['imgname'])

st.title('Implementation using Facebook AI Similarity Search')
c=st.selectbox('Select mode of input',('Upload Image','Select image from existing'))
if c=='Upload Image':
	uploaded_file = st.file_uploader("Choose an image from local", type="jpg")	
	if uploaded_file is not None:			
		slid=st.slider('Select number of images (k) to be retrieved :', 0, 10, 1)	
		if st.button('Submit'):
			image = Image.open(uploaded_file)
			image = image.resize((224,224))
			st.image(image, caption='Uploaded Image', use_column_width=True)
			ind=faiss_algo.faiss_similarity1(image,slid,index)			
			for i in ind:
				st.image(df['imgname'][i])

if c=='Select image from existing':
	s=st.selectbox('Select the images',('3615116_1.jpg','3683720_1.jpg','3627022_0.jpg'))
	slid=st.slider('Select number of images (k) to be retrieved :', 0, 10, 1)
	if st.button('Submit'):
		st.text('Selected Image')
		st.image('images/'+str(s))
		st.text('Matching images')	
		images=faiss_algo.faiss_similarity(s,slid,index)
		for i,j in enumerate(images):
			st.image(str(images[i]))


