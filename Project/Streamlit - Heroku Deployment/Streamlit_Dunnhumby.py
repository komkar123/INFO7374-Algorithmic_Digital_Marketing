import streamlit as st
import pandas as pd
#from PIL import Image
import pickle
from model import predict

def load_homepage():
	st.title('Dunnhumby - The Complete Journey')
	st.subheader('Introduction')
	st.markdown('An algorithmic marketing approach to understand the response and effects of \
transactions during different campaigns. Dunnhumby work with a range of sectors,\
including grocery retail, retail pharmacy, and retailer financial services. The expert \
teams work alongside their global clients in these sectors, helping them to make\
the most of their customer data and to put the Customer at the heart of everything\
 they do.')
	st.image('Images/cap.jpg',width = 800, height = 1000)
	st.subheader('Motivation')
	st.markdown('The overall data which has been collected contains demographics of 2500 households \
	who have been customers at various retail stores managed by Dunnhumby. There were different campaigns \
	ran by Dunnhumby by introducing coupons for discounts on various households. Some of the reacted \
	and showed interested, made purchasing and others did not redeem the coupons. At this current situation we \
	have to study the kind of households we are dealing with us and analyze their buying behaviours. \
	A marketing and machine learning based solution should be designed to approach this situation \
	for the growth of our retail stores and help them to maximize profit.  ')
	st.image('Images/algo.jpg',width = 800, height = 1000)
	st.subheader('Goals')
	st.markdown('**Household Segmentation using RFM modeling**')
	st.markdown('Segregating 2500 households based on their transactional history over the two years, to understand the plan to maximize profit.')
	st.markdown('**Predictive Analytics for Coupon Redemption**')
	st.markdown('Devising a ML based model to predict whether a household is sensitive to coupon or not. This will help retailers to customize coupon codes to maximize the overall outcome.')
	st.image('Images/goal.jpg',width = 800, height = 1000)
# def dataset():
# 	st.subheader('Overview of Dataset')
# 	st.markdown('This dataset contains household level transactions over two years from a group of \
# 2,500 households who are frequent shoppers at a retailer. It contains all each \
# household’s purchases, not just those from a limited number of categories. For \
# certain households, demographic information as well as direct marketing contact \
# history are included.')
# 	st.image('Images/data.jpg',width = 800, height = 1000)
# 	st.markdown('campaign_desc.csv : Description of Campaigns') 
# 	st.markdown('campaign_table.csv : Campaign and households participating')
# 	st.markdown('coupon.csv : Coupon information')
# 	st.markdown('coupon_redempt.csv : Coupon Redemptions')
# 	st.markdown('hh_demographic.csv : Household demographics')
# 	st.markdown('product.csv : Product Information')
# 	st.markdown('transaction_data.csv : Overall Transactions data')
def load_conclusions():
	st.header('Dunnhumby : Improving Retailers through Data Science')
	st.image('Images/conc.jpg', width = 800, height = 1000)
	st.markdown('The impact of algorithmic marketing tends to boost the performance of various retailers.\
		Tracking down the granular level of transactions, collecting data about the customers seems of vital importance.\
		Conducting campaigns to attract different section of people helps us understand the purchasing behaviour of public. \
		Segmenting allows marketers to better tailor their marketing efforts to various audience subsets. Those efforts can relate to both communications and product development. \
		Customer segmentation requires a company to gather specific information – data – about customers and analyze it to identify patterns that can be used to create segments. \
		Predicting whether a cretain section of household would be sensitive to coupons would be a good starting point to host campaigns. \
		It can be used to tailor and customize campaigns for targeted users. Based on the demographics, building a model made sense because \
		different mindset of people have changing moods to behave and deviate the market. The intersection of data science and marketing helps to \
		optimize the traditional methods of growth improvement and can enhance the growth of market')

def load_CustomerSegmentation():
	st.header("Customer Segmentation")
	st.markdown('Customer segmentation is the process of dividing customers into groups based on common characteristics so companies can market to each group effectively and appropriately.')
	st.markdown('Segmentation allows marketers to better tailor their marketing efforts to various audience subsets. Those efforts can relate to both communications and product development.')
	st.markdown('Customer segmentation requires a company to gather specific information – data – about customers and analyze it to identify patterns that can be used to create segments.')
	#imageSegment = Image.open('Images/Segmentation.png')
	st.image('Images/Segmentation.png', width = 800, height = 1000)
	st.header("Segmentation using RFM scores")
	st.markdown("Recency, frequency, monetary value is a marketing analysis tool used to identify a company's or an organization's best customers by using certain measures. The RFM model is based on three quantitative factors:")
	st.markdown("* Recency: How recently a customer has made a purchase")
	st.markdown("* Frequency: How often a customer makes a purchase")
	st.markdown("* Monetary Value: How much money a customer spends on purchases")
	st.markdown("RFM analysis numerically ranks a customer in each of these three categories, generally on a scale of 1 to 5")
	#imageRFM = Image.open('Images/RFMModel.jpg')
	st.image('Images/RFMModel.jpg', width = 800, height = 1000)
	st.markdown("In order to implement RFM Model, we first needed to calculate the recency value, frequency value and the monetary value of every household")
	st.markdown("After calculating the appropriate values, in order to assign the RFM score we split the dataset into 4 quantiles. The most desirable values get a score of 4 and it reduces as we go down")
	st.markdown("Since the lesser score of recency value is desirable, the 1st quantile get a score of 4 whereas when it comes to frequency and monetary value, larger the value, larger is the score")
	st.markdown("After assigning the scores, we concatenate it to get the RFM score")
	st.markdown("Based on the RFM Score and the individual Recency, Frequency and Monetary Value scores, we segment the customers")
	st.markdown("The map of the segmented customers is depicted below:")
	#imageRFMResult = Image.open('Images/RFM_Result.png')
	st.image('Images/RFM_Result.jpg', width = 800, height = 1000)
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
	#imageRecency = Image.open('Images/Recency.png')
	st.image('Images/Recency.jpg', width = 800, height = 1000)
	#imageFrequency = Image.open('Images/Frequency.png')
	st.image('Images/Frequency.jpg', width = 800, height = 1000)
	#imageMV = Image.open('Images/MV.png')
	st.image('Images/MV.jpg', width = 800, height = 1000)
	st.markdown("Based on that visualization, it shows that the variables with box-cox transformation shows a more symmetrical form rather than the other transformations")
	st.markdown("To normalize, we can use StandardScaler object from scikit-learn library to do it")
	st.markdown("To make our clustering reach its maximum performance, we have to determine which hyperparameter fits to the data. To determine which hyperparameter is the best for our model and data, we can use the elbow method to decide.")
	#imageElbow = Image.open('Images/Elbow.png')
	st.image('Images/Elbow.jpg', width = 800, height = 1000)
	st.markdown("By fitting the model, we can have clusters where each data belongs. By that, we can analyze the data.")
	st.write("we analyzed the segments using snake plot. It requires the normalized dataset and also the cluster labels. By using this plot, we can have a good visualization from the data on how the cluster differs from each other. The Snake Plot looks like this")
	#imageSnake = Image.open('Images/Snake.png')
	st.image('Images/Snake.jpg', width = 800, height = 1000)
	st.write("We calculated the relative importance of each attribute and plotted below")
	#imageCorr = Image.open('Images/Corr.png')
	st.image('Images/Corr.jpg', width = 800, height = 1000)
	st.markdown("To Conclude about every cluster")
	st.markdown("* Cluster 0")
	st.markdown("This has lowest frequency mean and low Monetary Value mean but lowest Recency mean. This segment of customers are lost")
	st.markdown("* Cluster 1")
	st.markdown("This has the lowest frequency and pretty lowest Monetary Value mean but the recency mean is really high. This segment of customers might have just started purchasing in the retailer and the business can invest market low prices to make them more interested")
	st.markdown("* Cluster 2")
	st.markdown("This cluster have an average Frequency and average Monetary Value but a high recency mean. We need to keep them engaged to make them buy more products")
	st.markdown("* Cluster 3")
	st.markdown("This cluster of customers have good Frequency mean, good Monetary Value mean and poor Recency mean. We need to do something to not lose them as they were interested in the business until a few months ago")


def load_predictiveAnalytics():
	i=0
	report = st.sidebar.radio('Select the element you would like to view',('Machine Learning Results','Predicting Households to Coupon Redemption'))
	if report == 'Machine Learning Results':
		st.subheader('Coupon Redemption Models : Results')
		st.markdown('**Precision Score of Models**')
		st.image('Images/prec.png')
		st.markdown('**Accuracy Score of Models**')
		st.image('Images/acc.png')
		st.markdown('**As we can see the logistic regression model performs better at classification than other ensemble models**')
		st.subheader('HyperParameter Tuning of Logistic Regression')
		st.image('Images/reg.png')
		st.markdown('L2 regularization with C=0.01 performs better')
		st.image('Images/regacc.png')

	try:
		while report=='Predicting Households to Coupon Redemption':
			i=i+1
			if i==1:
				st.subheader('Predict category of households for Coupon Redemption')
			age = st.selectbox(
				'Age Group',
				('19-24', '25-34', '35-44', '45-54','55-64','65+'))
			mar = st.selectbox(
				'Marital Status',
				('A','B','U'))
			inc= st.selectbox(
				'Income Range',
				('100-124k','125-149k','150-174k','175-199k','200-249k','250+','15-24k','25-34k','35-49k','50-74k','75-99k','Under 15k'),key=i)
			hh_desc = st.selectbox(
				'Homeowner type',
				('Homeowner','Portable Owner','Portable Renter','Renter','Unknown'))
			hh_cd = st.selectbox(
				'Household Description',
				('1 Adult kids','2 Adult kids','2 Adult No kids','Single Female','Single Male','Unknown'))
			kids_cat = st.selectbox(
				'Kid Category',
				('1','2','3+','Unknown'))
			sales = st.text_input('Enter sales values generated on average')
			
			vis = st.text_input('Average number of visits')
			
			if st.button('Predict'):
				try:

					sales=float(sales)
					vis=int(vis)
					r=predict(age,mar,inc,hh_desc,hh_cd,kids_cat,sales,vis)
					if r[0]==0:
						st.markdown('**Coupon Redemption**')
						st.image('Images/wrong.jpg', width = 300, height = 1000)
					if r[0]==1:
						st.markdown('**Coupon Redemption**')
						st.image('Images/yes.png', width = 300, height = 1000)
				except ValueError:
					st.markdown('**Invalid Type of Input**')

	except:
		pass			





def load_eda():
	report = st.sidebar.radio('Select the report you would like to view',('Household Demographics','Coupon Redemption and Sales'))
	if(report == 'Household Demographics'):
		st.subheader('Household Demographics Report')
		st.markdown("""
    <iframe width="900" height="650" src="https://datastudio.google.com/embed/reporting/56e35266-5246-47bb-8e48-c83c8cb3695e/page/z3ItB" frameborder="0" style="border:0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)
	if(report == 'Coupon Redemption and Sales'):
		st.subheader('Coupon Redemption and Sales')
		st.markdown("""
    <iframe width="850" height="800" src="https://datastudio.google.com/embed/u/0/reporting/7acd482b-193d-4776-aa20-84f61d71a1e7/page/jQVtB" frameborder="0" style="border:0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

def load_reference():
	st.markdown('* https://towardsdatascience.com/customer-segmentation-in-python-9c15acf6f945')
	st.markdown('* https://clevertap.com/blog/rfm-analysis/')

def create_layout():
	app_mode = st.sidebar.selectbox("Please select a page", ["Homepage",
															 "Exploratory Data Analysis",
                                                             "Customer Segmentation",
                                                             "Predictive Analytics",
                                                             "Conclusions"])
	if app_mode == 'Homepage':
		load_homepage()
	elif app_mode == 'Exploratory Data Analysis':
		load_eda()
	elif app_mode == 'Customer Segmentation':
		load_CustomerSegmentation()
	elif app_mode == 'Predictive Analytics':
		load_predictiveAnalytics()
	elif app_mode == 'Conclusions':
		load_conclusions()

def main():

	create_layout()

main()







