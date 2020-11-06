# -*- coding: utf-8 -*-


import numpy as np
from numpy.linalg import norm
import pickle
from tqdm import tqdm, tqdm_notebook
import os
import tensorflow as tf
import time
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from matplotlib import pyplot as plt
import streamlit as st

root_dir = 'images'
#from google.colab import drive

# This will prompt for authorization.
#drive.mount('/content/drive')

# Defining 50 layer residual network : ResNet50 trained on million images, to get features for our dataset.


#Extracting features of images by including image path and model trained above
def extract_features(img, model):
    input_shape = (224, 224, 3)
    #img = image.load_img(img_path, target_size=(input_shape[0], input_shape[1]))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    features = model.predict(preprocessed_img)
    flattened_features = features.flatten()
    normalized_features = flattened_features / norm(flattened_features)
    return normalized_features

def extract_features1(img, model):
    input_shape = (224, 224, 3)
    img = image.load_img(img, target_size=(input_shape[0], input_shape[1]))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    features = model.predict(preprocessed_img)
    flattened_features = features.flatten()
    normalized_features = flattened_features / norm(flattened_features)
    return normalized_features

def get_file_list(root_dir):
    file_list = []
    counter = 1
    for root, directories, filenames in os.walk(root_dir):
        for filename in filenames:

          file_list.append(os.path.join(root, filename))
          counter += 1
    return file_list

filenames = sorted(get_file_list(root_dir))

# Building out function to implement FAISS :
def faiss_similarity(img,k,index):
  model = ResNet50(weights='imagenet', include_top=False,
                 input_shape=(224, 224, 3))
  feature_list=extract_features1('images/'+str(img), model)
  nprobe = 2  # find 2 most similar clusters
  dimensions=len(feature_list)
  distances, indices = index.search(feature_list.reshape(1,-1), k)

  list_ind=indices.flatten().tolist()

  names=[]
  for i,j in enumerate(list_ind):
    names.append(filenames[j])
  return names  

def faiss_similarity1(img,k,index):
  model = ResNet50(weights='imagenet', include_top=False,
                 input_shape=(224, 224, 3))
  feature_list=extract_features(img, model)
  nprobe = 2  # find 2 most similar clusters
  dimensions=len(feature_list)
  distances, indices = index.search(feature_list.reshape(1,-1), k)
  list_ind=indices.flatten().tolist()
  # names=[]
  # for i,j in enumerate(list_ind):
  #   st.text(i)
  #   st.text(j)
  #   st.text(filenames[j])
  #   names.append(filenames[j])
  # return names  
  return list_ind