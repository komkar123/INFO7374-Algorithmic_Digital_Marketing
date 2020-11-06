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

# json for storing data in json file
import json
import pandas as pd
from tqdm import tqdm
import ntpath
import cv2

from sklearn.metrics.pairwise import cosine_similarity
import scipy as sc
from scipy import spatial
import matplotlib.pyplot as plt


# Annoy and Scipy for similarity calculation
from annoy import AnnoyIndex
from scipy import spatial
st.set_option('deprecation.showfileUploaderEncoding', False)


st.title("Visual Search")
def match_id(filename):
    product_id = '_'.join(filename.split('_')[:-1])
    return product_id

def load_image(image):
	
	#st.write("Entered Load Image")
	#st.write(type(path))
	#st.write(type(image))
	#image = image.decode('utf-8')
	image = np.array(image.read())
	img = tf.io.decode_jpeg(image, channels=3)
	#image = img_to_array(image)
	# reshape data for the model
	img = tf.image.resize_with_pad(img, 224, 224)
	# Converts the data type of uint8 to float32 by adding a new axis
	# img becomes 1 x 224 x 224 x 3 tensor with data type of float32
	# This is required for the mobilenet model we are using
	img = tf.image.convert_image_dtype(img,tf.float32)[tf.newaxis, ...]
	#st.write(type(img))
	return img

def features():
	allfiles = glob.glob('images_scrapped/*.npz')
	global image_style_embeddings
	image_style_embeddings = {}

	for file_index, i in enumerate(allfiles):

	# Reads feature vectors and assigns them into the file_vector 
		file_vector = np.loadtxt(i)

		# Assigns file_name, feature_vectors and corresponding product_id
		#file_index_to_file_vector[file_index] = file_vector
		image_style_embeddings[ntpath.basename(i)] = file_vector

def cluster(v0):
	print("-------Annoy Index Generation----------------")
    # Defining data structures as empty dict
	file_index_to_file_name = {}
	file_index_to_file_vector = {}
	file_index_to_product_id = {}
	# Configuring annoy parameters
	dims = 1792
	n_nearest_neighbors = 20
	trees = 10000
	# Reads all file names which stores feature vectors
	allfiles = glob.glob('images_scrapped\\*.npz')

	t = AnnoyIndex(dims, metric='angular')
	j = 0
	for file_index, i in enumerate(allfiles):

    
    # Reads feature vectors and assigns them into the file_vector 
		file_vector = np.loadtxt(i)

		# Assigns file_name, feature_vectors and corresponding product_id
		file_name = os.path.basename(i).split('.')[0]
		file_index_to_file_name[file_index] = file_name
		file_index_to_file_vector[file_index] = file_vector
		file_index_to_product_id[file_index] = match_id(file_name)
		# st.write(file_index_to_file_name[file_index])
		# st.write(file_index_to_file_vector[file_index])
		# st.write(file_index_to_product_id[file_index])

		# Adds image feature vectors into annoy index   
		t.add_item(file_index, file_vector)

		print("---------------------------------")
		print("Annoy index     : %s" %file_index)
		print("Image file name : %s" %file_name)
		print("Product id      : %s" %file_index_to_product_id[file_index])
		j = j + 1
		# st.write("Printing j")
		# st.write(j)
        #print("--- %.2f minutes passed ---------" % ((time.time() - start_time)/60))
	file_index_to_file_name[j] = 'new_file'
	file_index_to_file_vector[j] = v0
	file_index_to_product_id[j] = 'new_file'
	# st.write("printing files")

	# for i in file_index_to_file_name.keys():
	# 	st.write(file_index_to_file_name[i])
	# 	st.write(file_index_to_file_vector[i])
	# 	st.write(file_index_to_product_id[i])
	#st.write(file_index_to_file_name[108])


	t.add_item(j, v0)
	#Builds
	# Builds annoy index
	t.build(trees)

	print ("Step.1 - ANNOY index generation - Finished")
	print ("Step.2 - Similarity score calculation - Started ") 

	global named_nearest_neighbors
	named_nearest_neighbors = []
	# st.write("printing j")
	# st.write(j)

	master_file_name = file_index_to_file_name[j]
	master_vector = file_index_to_file_vector[j]
	master_product_id = file_index_to_product_id[j]

	nearest_neighbors = t.get_nns_by_item(j, n_nearest_neighbors)

	for k in nearest_neighbors:

		# Assigns file_name, image feature vectors and product id values of the similar item
		neighbor_file_name = file_index_to_file_name[k]
		neighbor_file_vector = file_index_to_file_vector[k]
		neighbor_product_id = file_index_to_product_id[k]

		# Calculates the similarity score of the similar item
		similarity = 1 - spatial.distance.cosine(master_vector, neighbor_file_vector)
		rounded_similarity = int((similarity * 10000)) / 10000.0

		# Appends master product id with the similarity score 
		# and the product id of the similar items
		named_nearest_neighbors.append({
		'similarity': rounded_similarity,
		'master_pi': master_product_id,
		'similar_pi': neighbor_product_id})
	# st.write("Printing Named Nearest neighbors")
	# st.write(named_nearest_neighbors)	
	return named_nearest_neighbors		

  # Loops through all indexed items
	# for i in file_index_to_file_name.keys():

 #    # Assigns master file_name, image feature vectors and product id values
	# 	master_file_name = file_index_to_file_name[i]
	# 	master_vector = file_index_to_file_vector[i]
	# 	master_product_id = file_index_to_product_id[i]

	# 	# Calculates the nearest neighbors of the master item
	# 	nearest_neighbors = t.get_nns_by_item(i, n_nearest_neighbors)

	# 	# Loops through the nearest neighbors of the master item
	# 	for k in nearest_neighbors:

 #            # Assigns file_name, image feature vectors and product id values of the similar item
	# 		# st.write("printing k")
	# 		# st.write(k)
	# 		neighbor_file_name = file_index_to_file_name[k]
	# 		neighbor_file_vector = file_index_to_file_vector[k]
	# 		neighbor_product_id = file_index_to_product_id[k]

	# 		# Calculates the similarity score of the similar item
	# 		similarity = 1 - spatial.distance.cosine(master_vector, neighbor_file_vector)
	# 		rounded_similarity = int((similarity * 10000)) / 10000.0

	# 		# Appends master product id with the similarity score 
	# 		# and the product id of the similar items
	# 		named_nearest_neighbors.append({
	# 		'similarity': rounded_similarity,
	# 		'master_pi': master_product_id,
	# 		'similar_pi': neighbor_product_id})
	print("Printing Named Nearest neighbors")
	print(named_nearest_neighbors)	
	return named_nearest_neighbors		

def get_the_features(img, image_path):
	# Definition of module with using tfhub.dev
	module_handle = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/4"
	# Loads the module
	module = hub.load(module_handle)
	st.write("loaded module")
	features = module(img)
	# Remove single-dimensional entries from the 'features' array  
	feature_set = np.squeeze(features)

	# Saves the image feature vectors into a file for later use
	outfile_name = os.path.basename(image_path) + ".npz"

	out_path = os.path.join('images_scrapped',outfile_name)
	# Saves the 'feature_set' to a text file
	np.savetxt(out_path, feature_set, delimiter=',')
	vector = np.loadtxt(out_path)
	return vector

# def get_features(img): 
#      # Definition of module with using tfhub.dev
#     module_handle = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/4"
#     # Loads the module
#     module = hub.load(module_handle)
#     features = module(img)
#     # Remove single-dimensional entries from the 'features' array  
#     feature_set = np.squeeze(features)
#     print(image_path)

#     # Saves the image feature vectors into a file for later use
#     outfile_name = os.path.basename('images_scrapped') + ".npz"

#     out_path = os.path.join('D:/Documents/Semester3/ADM/Assignment 3/Imgs_Scraped/',outfile_name)
#     # Saves the 'feature_set' to a text file
#     np.savetxt(out_path, feature_set, delimiter=',')
#     vector = np.loadtxt(out_path)
#     return vector

def get_vector(image):
	module_handle = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/feature_vector/4"
	# Loads the module
	module = hub.load(module_handle)

	#Preprocess the image
	img = load_image(image)
	# Calculate the image feature vector of the img
	features = module(img)
	# Remove single-dimensional entries from the 'features' array  
	feature_set = np.squeeze(features)
	filename = "new_image"

	# Saves the image feature vectors into a file for later use
	#outfile_name = os.path.basename('D:/Documents/Semester3/ADM/Assignment 3/New_Image/') + filename + ".npz"
	outfile_name = os.path.basename(filename) + '.npz'

	out_path = os.path.join(outfile_name)
	# Saves the 'feature_set' to a text file
	np.savetxt(out_path, feature_set, delimiter=',')
	vector = np.loadtxt(out_path)
	#image_style_embeddings['newFile'] = vector
	return vector

def get_all_images():
	image_paths = glob.glob('images\\*.jpg')
	print(f'Founnd [{len(image_paths)}] images')
	#st.write("Entered Get All Images")

	images = []
	for image_path in image_paths:
		image = cv2.imread(image_path, 3)
		b,g,r = cv2.split(image)           # get b, g, r
		image = cv2.merge([r,g,b])         # switch it to r, g, b
		image = cv2.resize(image, (200, 200))
		product_id = match_id(ntpath.basename(image_path))
		images.append({
		  'image_path' : ntpath.basename(image_path),
		    'image' : image,
		   'product_id':product_id
		})
	return images
def get_all_features():
	image_paths= glob.glob('images\\*.jpg')
	#vectorfiles = glob.glob('images_scrapped\\*.npz')
	# compute styles
	image_style_embeddings = {}

	for image_path in tqdm(image_paths): 
	    image_tensor = load_image(image_path)
	    #st.write(type(image_tensor))
	    st.write("Image Preprocessed")
	    vector = get_the_features(image_tensor, image_path)
	    #image_style_embeddings[ntpath.basename(image_path)] = vector

	st.write("Got All Features")


def search_similar_image(reference_image, max_results):
	#st.write("Entered Similar image")
	#v0 = image_style_embeddings['newFile']
	distances = {}
	for k,v in image_style_embeddings.items():
		similarity = 1 - spatial.distance.cosine(v0, v)
		rounded_similarity = int((similarity * 10000)) / 10000.0
		distances[k] = rounded_similarity
        

	sorted_neighbors = sorted(distances.items(), key=lambda x: x[1], reverse=False)
	#print(sorted_neighbors)
	data=[]
	named_nearest_neighbors = []
	f, ax = plt.subplots(1, max_results, figsize=(16, 8))
	for i, img in enumerate(sorted_neighbors[:max_results]):
		named_nearest_neighbors.append({'image':sorted_neighbors[i][0]})
		# ax[i].imshow(images[img[0]])
		# ax[i].set_axis_off()
		data.append({'img':sorted_neighbors[i][0],'score':sorted_neighbors[i][1]})
	return data
    # plt.show()