import os
import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub
# For saving 'feature vectors' into a txt file
import numpy as np
# Glob for reading file names in a folder
import glob
import os.path
import io
from imageio import imread
import base64
from io import BytesIO
import PIL
from keras.preprocessing.image import load_img
from tempfile import NamedTemporaryFile
from PIL import Image
import time

# Glob for reading file names in a folder
import glob
# json for storing data in json file
import json
import pandas as pd

# Annoy and Scipy for similarity calculation
from annoy import AnnoyIndex
from scipy import spatial
from Spotify_algo import get_all_images
from Spotify_algo import features
from Spotify_algo import get_vector
from Spotify_algo import search_similar_image
from Spotify_algo import match_id
st.set_option('deprecation.showfileUploaderEncoding', False)
d = []
images = {}
images = get_all_images()
features()
img = {}
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
slid=st.slider('Select number of images (k) to be retrieved :', 0, 10, 1)
if st.button('Submit'):
	if uploaded_file is not None:
		#st.write("Classifying...")
		vector = get_vector(uploaded_file)
		img = search_similar_image(vector, slid)
		#st.write(img)
		im = Image.open(uploaded_file)
		st.image(im, caption = "Uploaded image")
		st.write("Similar images")
		for i in range(0, slid):
			image_name = img[i]
			file = image_name["img"]
			#filename = ".".join(file.split(".").[-1])
			filename = '.'.join(file.split('.')[:-1])
			st.image(images[filename])
			#img = Image.open(BytesIO(images[filename]))

		#st.write(img[0] for img in img)
		#filename = ".".join(img.keys())[0].split(".").[:-1]
		# for i in range(0, slid):
		# 	img=Image.open(BytesIO(images[img[0]]))
		# 	d.append(img)
		# 	st.image(d[i])

			

		


    	#vector = get_image_feature_vectors(uploaded_file)
    	

