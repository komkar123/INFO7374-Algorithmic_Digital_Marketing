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
	imageSegment = Image.open('Images/Segmentation.png')
	st.image(imageSegment, width = 800, height = 1000)
	st.header("Segmentation using RFM scores")
	st.markdown("Recency, frequency, monetary value is a marketing analysis tool used to identify a company's or an organization's best customers by using certain measures. The RFM model is based on three quantitative factors:")
	st.markdown("* Recency: How recently a customer has made a purchase")
	st.markdown("* Frequency: How often a customer makes a purchase")
	st.markdown("* Monetary Value: How much money a customer spends on purchases")
	st.markdown("RFM analysis numerically ranks a customer in each of these three categories, generally on a scale of 1 to 5")
	imageRFM = Image.open('Images/RFMModel.jpg')
	st.image(imageRFM, width = 800, height = 1000)
	st.markdown("In order to implement RFM Model, we first needed to calculate the recency value, frequency value and the monetary value of every household")
	st.markdown("After calculating the appropriate values, in order to assign the RFM score we split the dataset into 4 quantiles. The most desirable values get a score of 4 and it reduces as we go down")
	st.markdown("Since the lesser score of recency value is desirable, the 1st quantile get a score of 4 whereas when it comes to frequency and monetary value, larger the value, larger is the score")
	st.markdown("After assigning the scores, we concatenate it to get the RFM score")
	st.markdown("Based on the RFM Score and the individual Recency, Frequency and Monetary Value scores, we segment the customers")
	st.markdown("The map of the segmented customers is depicted below:")
	imageRFMResult = Image.open('Images/RFM_Result.png')
	st.image(imageRFMResult, width = 800, height = 1000)
	st.markdown("The definition of every customer segment is described below")
	st.markdown("* Best Customers -Can't Loose Them : The customers who have been recent, frequent and have spend a decent amount in the retail store")
	st.markdown("* Champions Spenders : The customers who have spend a huge amount of money and have a decent Frequency and Recency score")
	st.markdown("* Loyal Customers : The customers who has an averge score in all the three parameters such as Frequency, Recency and Monetary Value")
	st.markdown("* Potential Loyalists : The customers who might not have spend much on the retailer but but have an averge recency and frequency score")
	st.markdown("* Needs Attention : The customers who have an average frequency score but their recency score has been pretty low")
	st.markdown("* Almost Lost : Almost Lost are the customers who might have either a decent frequency score but their recency score is poor")
	st.markdown("* Lost Customers : The customers who have a poor recency, frequency and Monetary Value score are the lost customers and there is no point in investing to trying to get them back")

	st.header("Segmentation using K means clustering and RFM scores")
	st.markdown("K means clustering is one of the most popular clustering algorithms and usually the first thing practitioners apply when solving clustering tasks to get an idea of the structure of the dataset. The goal of K means is to group data points into distinct non-overlapping subgroups. One of the major application of K means clustering is segmentation of customers to get a better understanding of them which in turn could be used to increase the revenue of the company.")
	st.markdown("We first analyse the skewness of every attribute and decide on which transformation is to be applied.  From top left clockwise on each variable shows the plot without transformation, log transformation, square root transformation, and box-cox transformation. ")
	imageRecency = Image.open('Images/Recency.png')
	st.image(imageRecency, width = 800, height = 1000)
	imageFrequency = Image.open('Images/Frequency.png')
	st.image(imageFrequency, width = 800, height = 1000)
	imageMV = Image.open('Images/MV.png')
	st.image(imageMV, width = 800, height = 1000)
	st.markdown("Based on that visualization, it shows that the variables with box-cox transformation shows a more symmetrical form rather than the other transformations")
	st.markdown("To normalize, we can use StandardScaler object from scikit-learn library to do it")
	st.markdown("To make our clustering reach its maximum performance, we have to determine which hyperparameter fits to the data. To determine which hyperparameter is the best for our model and data, we can use the elbow method to decide.")
	imageElbow = Image.open('Images/Elbow.png')
	st.image(imageElbow, width = 800, height = 1000)
	st.markdown("By fitting the model, we can have clusters where each data belongs. By that, we can analyze the data.")
	st.write("we analyzed the segments using snake plot. It requires the normalized dataset and also the cluster labels. By using this plot, we can have a good visualization from the data on how the cluster differs from each other. The Snake Plot looks like this")
	imageSnake = Image.open('Images/Snake.png')
	st.image(imageSnake, width = 800, height = 1000)
	st.write("We calculated the relative importance of each attribute and plotted below")
	imageCorr = Image.open('Images/Corr.png')
	st.image(imageCorr, width = 800, height = 1000)
	st.markdown("To Conclude about every cluster")
	st.markdown("* Cluster 0")
	st.markdown("This has lowest frequency mean and low Monetary Value mean but lowest Recency mean. This segment of customers are lost")
	st.markdown("* Cluster 1")
	st.markdown("This has the lowest frequency and pretty lowest Monetary Value mean but the recency mean is really high. This segment of customers might have just started purchasing in the retailer and the business can invest market low prices to make them more interested")
	st.markdown("* Cluster 2")
	st.markdown("This cluster have an average Frequency and average Monetary Value but a high recency mean. We need to keep them engaged to make them buy more products")
	st.markdown("* Cluster 3")
	st.markdown("This cluster of customers have good Frequency mean, good Monetary Value mean and poor Recency mean. We need to do something to not lose them as they were interested in the business until a few months ago")


def load_eda():
	report = st.sidebar.radio('Select the report you would like to view',('Household Demographics','Coupon Redemption and Sales'))
	if(report == 'Household Demographics'):
		st.markdown("""
    <iframe width="900" height="650" src="https://datastudio.google.com/embed/reporting/56e35266-5246-47bb-8e48-c83c8cb3695e/page/z3ItB" frameborder="0" style="border:0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)
	if(report == 'Coupon Redemption and Sales'):
		st.markdown("""
    <iframe width="850" height="800" src="https://datastudio.google.com/embed/u/0/reporting/7acd482b-193d-4776-aa20-84f61d71a1e7/page/jQVtB" frameborder="0" style="border:0" allowfullscreen></iframe>
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




