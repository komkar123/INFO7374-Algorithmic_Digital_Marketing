import pandas as pd
import pickle
import streamlit as st
import numpy as np 

def predict(age,mar,inc,hh_desc,hh_cd,kids_cat,sales,vis):
	df_mean=pd.read_csv('means.csv')
	df_std=pd.read_csv('stds.csv')
	with open(r"logisticregression.pkl", "rb") as input_file:
		e = pickle.load(input_file)
	if age=='19-24':
		a=1
	elif age =='25-34':
		a=2
	elif age == '35-44':
		a=3
	elif age=='45-54':
		a=4
	elif age=='55-64':
		a=5
	elif age=='65+':
		a=6
	if inc=='Under 15k':
		ic=0
	elif inc =='15-24k':
		ic=1
	elif inc =='25-34k':
		ic=2
	elif inc== '35-49k':
		ic=3
	elif inc=='50-74k':
		ic=4
	elif inc=='75-99k':
		ic=5
	elif inc=='100-124k':
		ic=6
	elif inc=='125-149k':
		ic=7
	elif inc=='150-174k':
		ic=8
	elif inc=='175-199k':
		ic=9
	elif inc=='200-249k':
		ic=10
	elif inc=='250+':
		ic=11
	marital_status_code_A=0
	marital_status_code_B=0
	marital_status_code_U=0	
	if mar=='A':
		marital_status_code_A=1
	elif mar=='B':
		marital_status_code_B=1
	elif mar=='U':
		marital_status_code_U=1
	homeown=0
	probown=0
	probren=0
	homren=0
	homown=0
	if hh_desc=='Homeowner':
		homeown=1
	elif hh_desc=='Portable Owner':
		probown=1
	elif hh_desc=='Portable Renter':
		probren=1
	elif hh_desc=='Renter':
		homren=1
	elif hh_desc=='Unknown':
		homown=1
	if kids_cat=='1':
		kid=1
	elif kids_cat=='2':
		kid=2
	elif kids_cat=='3+':
		kid=3	
	elif kids_cat=='Unknown':
		kid=0
	oak=0
	tak=0
	ta=0
	of=0
	om=0
	unknown_hh=0

	if hh_cd=='1 Adult kids':
		oak=1
	elif hh_cd=='2 Adult kids':
		tak=1
	elif hh_cd=='2 Adult No kids':
		ta=1
	elif hh_cd=='Single Female':
		of=1
	elif hh_cd=='Single Male':
		om=1 		
	elif hh_cd=='Unknown':
		unknown_hh=1 

	
	age=(a-df_mean['0'][0])/df_std['0'][0]
	#st.text(age)
	inc=(ic-df_mean['0'][1])/df_std['0'][1]	
	kid=(kid-df_mean['0'][2])/df_std['0'][2]
	sales=(sales-df_mean['0'][3])/df_std['0'][3]
	vis=(vis-df_mean['0'][4])/df_std['0'][4]

	inp=[age,inc,kid,sales,vis,marital_status_code_A,marital_status_code_B,marital_status_code_U,homeown,probown,probren,homren,homown,oak,tak,ta,of,om,unknown_hh]
	inp=np.asarray(inp)
	p=e.predict(inp.reshape(1,-1))

	return p