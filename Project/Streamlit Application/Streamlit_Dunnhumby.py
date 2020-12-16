import streamlit as st
import pandas as pd
from PIL import Image

def load_homepage():
	st.title('Dunnhumby - The Complete Journey')
	st.subheader('Data Overview')

def load_CustomerSegmentation():
	st.header("Customer Segmentation")
	st.markdown('Customer segmentation is the process of dividing customers into groups based on common characteristics so companies can market to each group effectively and appropriately.')
	st.markdown('Segmentation allows marketers to better tailor their marketing efforts to various audience subsets. Those efforts can relate to both communications and product development.')
	st.markdown('Customer segmentation requires a company to gather specific information – data – about customers and analyze it to identify patterns that can be used to create segments.')
	imageData = Image.open('Images/Segmentation.png')
	st.image(imageData, width = 800, height = 1000)

def load_eda():
	report = st.radio('Select the report you would like to view',('Household Demographics','Coupon Redemption and Sales'))
	if(report == 'Household Demographics'):
		st.markdown("""
    <iframe width="850" height="450" src="https://datastudio.google.com/embed/reporting/09309c31-918f-4abd-88ed-8ac6fa6c9548/page/g3HtB" frameborder="0" style="border:0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

def create_layout():
	app_mode = st.sidebar.selectbox("Please select a page", ["Homepage : Data Description",
															 "Exploratory Data Analysis",
                                                             "Customer Segmentation",
                                                             "Predictive Analytics",
                                                             "Conclusions",
                                                             "References"])
	if app_mode == 'Homepage : Data Description':
		load_homepage()
	elif app_mode == 'Exploratory Data Analysis':
		load_eda()
	elif app_mode == 'Customer Segmentation':
		load_CustomerSegmentation()
	elif app_mode == 'Predictive Analytics':
		load_predictiveAnalytics()
	elif app_mode == 'Conclusions':
		load_conclusions()
	elif app_mode == 'References':
		load_reference()

def main():
	create_layout()

main()

#st.set_option('deprecation.showPyplotGlobalUse', False)
#load_homepage()
#st.markdown("eNTERED MAIN")





