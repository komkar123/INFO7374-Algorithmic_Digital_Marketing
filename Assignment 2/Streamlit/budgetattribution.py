import streamlit as st
import os 
import pandas as pd
import altair as alt
import seaborn as sns
from PIL import Image
import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse', False)
def main():
	create_layout()

def create_layout():
	app_mode = st.sidebar.selectbox("Please select a page", ["Homepage : Data Description",
                                                             "Attribution Models",
                                                             "Visualizations",
                                                             "Conclusions",
                                                             "References"])
	if app_mode == 'Homepage : Data Description':
		load_homepage()
	elif app_mode == 'Attribution Models':
		load_attribution()
	elif app_mode == 'Visualizations':
		load_visualization()
	elif app_mode == 'Conclusions':
		load_conclusions()
	elif app_mode == 'References':
		load_reference()


def load_homepage():
 	st.title('Attribution Modeling and Budget Optimization')
 	st.markdown('Marketers usually use multiple channels–such as sponsored search, display ads, and emails–to reach their customers, and each channel usually includes multiple activities or has multiple parameters that are associated with various costs. For example, a marketer can run several email campaigns, each of which corresponds to a certain price discount, or run sponsored search for multiple keywords, each of which is associated with a certain bid amount. On the other hand, customers usually interact with multiple touchpoints along the way to conversion, so that the effects from different touchpoints intertwine and accumulate')
 	imageData = Image.open('DataDes.jpeg')
 	st.image(imageData, width = 800, height = 1000)
 	st.markdown('This leads to the problem of marketing spend optimization, which requires estimating the true contribution of individual channels and activities to the final outcome and optimally allocating budgets across these channels, or even setting individual activity parameters such as bids in sponsored keyword search.')
 	st.markdown('Criteo has published an online advertising dataset which has details of campaigns and budget allocated for each of them. The aim is to check the cross-channel Optimization using various parameters to access which channel should be getting the maximum budget for advertisement.')
 	imageData2 = Image.open('DataDes2.jpeg')
 	st.image(imageData2, width = 800, height = 1000)
 	st.subheader('Data')
 	st.markdown('This dataset represents a sample of 30 days of Criteo live traffic data. Each line corresponds to one impression (a banner) that was displayed to a user. For each banner we have detailed information about the context, if it was clicked, if it led to a conversion and if it led to a conversion that was attributed to Criteo or not')
 	st.markdown("♟ Timestamp : timestamp of the impression (starting from 0 for the first impression). The dataset is sorted according to timestamp. ")
 	st.markdown("♟ UID : Unique User Identifier")
 	st.markdown("♟ Campaign : Unique Campaign Identifier")
 	st.markdown("♟ Conversion :  1 if there was a conversion in the 30 days after the impression; 0 otherwise")
 	st.markdown("♟ Conversion ID :  A unique identifier for each conversion")
 	st.markdown("♟ Click : 1 if the impression was clicked; 0 otherwise")
 	st.markdown("♟ Cost: The price paid for this ad ")
 	st.markdown("♟ Cat1-Cat9 : Categorical features associated with the ad")
 	st.subheader("Key Figures")
 	st.markdown("* 2.4Gb uncompressed")
 	st.markdown("* 16.5M impressions")
 	st.markdown("* 45K conversions")
 	st.markdown("* 700 campaigns")




def load_attribution():
	st.title('Attribution Modeling and Budget Optimization')
	st.subheader('What is Attribution Modeling?')

	st.markdown('Attribution modeling is a framework for analyzing which touchpoints/marketing channels receive credit for a conversion. Each attribution model distributes the credit across each touchpoint differently. By analyzing each attribution model one can derive the ROI for each marketing channel.')
	imageAttribution = Image.open('AttributionModeling.jpg')
	st.image(imageAttribution, width = 800, height = 1000)
	st.markdown('A model comparison tool allows you to analyze how each model distributes the value of a conversion. There are six common attribution models: First Interaction, Last Interaction, Last Non-Direct Click, Linear, Time-Decay, and Position-Based.')
	imageAllocation = Image.open('Allocation.png')
	st.image(imageAllocation, caption = "Allocation", width = 800, height = 1000)
	st.markdown('Types of attribution model we implemented')
	st.markdown('1. Single Touch Attribution Model')
	st.markdown('* Last Touch Attribution')
	st.markdown('* First Touch Attribution')
	st.markdown('2. Multi Touch Attribution')
	st.markdown('* Linear Attribution')
	st.markdown('* Time Decay Attribution')
	st.markdown('* U Shaped Attribution')
	st.markdown('3. Data Driven Attribution')
	st.markdown('* Logistic Regression')

	st.subheader('Last Touch Attribution')
	st.markdown('They do not use any statistical analysis instead assigns all the credits to the last touch point right before conversion. The ratio between the number of journeys in which a given campaign is the last event and the total number of events for the same campaign gives the attribution weight. It gives 100% of the credit for a conversion to the last click or visit that happened in a conversion path. If there was no click or visit, then it will credit the last impression.')
	st.markdown('* Pros')
	st.markdown('This is a great model for the marketers who are completely focused on driving conversions but that is only the case when non converting events do not absolutely hold any value for the business')
	st.markdown('* Cons')
	st.markdown('It does not take the path of the conversion into consideration at all. It provides zero visibility into what can be very influential interactions')

	st.markdown('Regression analysis aims to find true contributions of the touchpoints. It focuses to find the exact weightage of the touchpoints in a campaigns journey')
	datalta = {'Events':['1', '2', '3', '4', '5'],
        'Percentage':[0, 0, 0, 0, 100]}
	dflta = pd.DataFrame(datalta)

	sns.barplot(x="Events", y ="Percentage", data = dflta)
	st.pyplot()

	#fig = px.bar(dflta, x='Events', y='Percentage')
	#fig.show()
	#chart = st.bar_chart(df1)

	# image = Image.open('LTA.png')
	# st.image(image, caption = "LTA", width = 300, height = 200)

# 	st.write(alt.Chart(dflta).mark_bar().encode(
#     x=alt.X('Events', sort=None),
#     y='Percentage'
# ))
		#st.img('[![](LTA.png)]')
	st.subheader('First Touch Attribution')
	st.markdown('This model assigns 100%'' credit to the campaign that initiated the very first interaction somebody had with your business. It over emphasizes a single part of the funnel which is the top of the funnel. It is more susceptible to errors like chanel bias and technology limitations than the other models')
	st.markdown('* Pros')
	st.markdown('This model is useful for marketers who are solely focused on demand generation and are not dependent on conversions. This model emphasizes on the campaigns that first introduced a customer to the brand regardless of the outcome')
	st.markdown('* Cons')
	st.markdown('It offers very limited Optimization ability to marketers. It will give a hard time justifying their impact on a company''s bottom line')

	datafta = {'Events':['1', '2', '3', '4', '5'],
        'Percentage':[100, 0, 0, 0, 0]}
	dffta = pd.DataFrame(datafta)

	sns.barplot(x="Events", y ="Percentage", data = dffta)
	st.pyplot()
# 	st.write(alt.Chart(dffta).mark_bar().encode(
#     x=alt.X('Events', sort=None),
#     y='Percentage',
# ))

	st.subheader('Linear Attribution')
	st.markdown('This model assigns credit evenly to every marketing touch throughout the customer journey. If there are 10 touches, each will receive 10% of the credit. When there are 5 campaigns, each will receive 20%.')
	st.markdown('* Pros')
	st.markdown('By assigning equal weight to each marketing campaign, marketers can start optimizing for every the customer journey instead of a single activity')
	st.markdown('* Cons')
	st.markdown('Since every touch is receiving equal contribution, it is easy to lose the ability to optimize for specific outcomes')

	datala = {'Events':['1', '2', '3', '4', '5'],
        'Percentage':[20, 20, 20, 20, 20]}
	dfla = pd.DataFrame(datala)
	sns.barplot(x="Events", y ="Percentage", data = dfla)
	st.pyplot()


# 	st.write(alt.Chart(dfla).mark_bar().encode(
#     x=alt.X('Events', sort=None),
#     y='Percentage',
# ))

	st.subheader('Time Decay Attribution')
	st.markdown('Time Decay assigns more the most credit to the events that are closer to the date of conversion. Touches leading up to to the conversion receive less value the further back they are')
	st.markdown('* Pros')
	st.markdown('It has the ability to truly optimize. It recognizes the significance of the interaction leading up to the conversion while still placing value on the activities. Marketers can use this model to optimize for touches that drive conversions as well as the touches which increase the likelihood of a conversion in the near future.')
	st.markdown('* Cons')
	st.markdown('It lacks the ability to recognize the interaction of the event that introduced the customer to your brand. It may result in a low amount of credit for highly influential touches.')

	datatda = {'Events':['1', '2', '3', '4', '5'],
        'Percentage':[5, 10, 15, 30, 40]}
	dftda = pd.DataFrame(datatda)

	sns.barplot(x="Events", y ="Percentage", data = dftda)
	st.pyplot()
# 	st.write(alt.Chart(dftda).mark_bar().encode(
#     x=alt.X('Events', sort=None),
#     y='Percentage',
# ))
	st.subheader('U Shaped Attribution')
	st.markdown('This model combines the best features of linear and time decay by giving weightage of 40% to the extreme touchpoints and the rest 20% is equally split between the intermediate touchpoints ')
	st.markdown('* Pros')
	st.markdown('This model ensures that every touchpoint receives some credit for the contribution towards conversion. It lets you assign significant credit to the event that introduced the customer to your brand and also the event the lead to the conversion')
	st.markdown('* Cons')
	st.markdown('This could result in two very low value touches being given too much credit')

	datausa = {'Events':['1', '2', '3', '4', '5'],
        'Percentage':[40, 20,20, 20, 40]}
	dfusa = pd.DataFrame(datausa)

	sns.barplot(x="Events", y ="Percentage", data = dfusa)
	st.pyplot()
# 	st.write(alt.Chart(dfusa).mark_bar().encode(
#     x=alt.X('Events', sort=None),
#     y='Percentage',
# ))

	st.subheader('Logistic Regression')
	st.markdown('It aims to reveal touchpoints treu contributions. Each journey is represented as a vector in which each campaign is represented by a binary feature (and can be other event features), a regression model is fit to predict conversions, and the resulting regression coefficients are interpreted as attribution weights')

def load_visualization():
	import matplotlib.pyplot as plt 
	st.set_option('deprecation.showPyplotGlobalUse', False)

	# LTA = Image.open('LTA.png')
	# st.image(LTA, caption = "AM", width = 800, height = 1000)

	# FTA = Image.open('FTA.png')
	# st.image(FTA, caption = "AM", width = 800, height = 1000)

	# Lin = Image.open('Linear.png')
	# st.image(Lin, caption = "AM", width = 800, height = 1000)

	# TDA = Image.open('TDA.png')
	# st.image(TDA, caption = "AM", width = 800, height = 1000)

	# USA = Image.open('USA.png')
	# st.image(USA, caption = "AM", width = 800, height = 1000)
	st.subheader('Last Touch Attribution')

	data_lta = {'Campaign_ID':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
	'Contribution'	 : [0.08040201, 0.08333333, 0.09589041, 0.21276596, 0.15714286, 0.17948718,
 	 0.1509434,  0.02857143, 0.29824561, 0.11428571, 0.14285714, 0.20610687,
	 0.10925197, 0.24183007, 0.19705882, 0.05084746, 0.11111111, 0.05660377,
	 0.29411765, 0.05128205, 0.1, 0.07777778, 0.23076923, 0.26190476,
	 0.21212121, 0.14285714, 0.19402985, 0.12337662, 0.11564626, 0.10752688,
	 0.16911765, 0.13636364, 0.08219178, 0.14423077, 0.13517241, 0.12,
	 0.2,        0.07291667, 0.18461538, 0.17757009, 0.0,         0.24390244,
	 0.36,       0.27058824, 0.14705882, 0.09859155, 0.19727891, 0.09677419,
	 0.22346369, 0.05084746]}
	LTA = pd.DataFrame(data_lta)

	ltaax = sns.barplot(x='Campaign_ID', y ="Contribution", data = LTA, color=(0.2, 0.4, 0.6, 0.6))
	ltaax.set_xticklabels(ltaax.get_xticklabels(), rotation=90, ha="right", fontsize = 7)
	st.pyplot()

	st.markdown('In this model, we gave all the 100% credit to the touchpoint that lead to conversion. We assigned this by finding the maximum of the normalized touchpoint in the journey. The drawback of this touchpoint is that it could miss all the touchpoints that lead to the conversion.')


	# fig = plt.figure(figsize=(18,8))
	# ax = fig.add_subplot(111)
	# plt.bar(range(len(LTA['Campaign_ID'])), LTA['Return_of_Investment'], label='LTA' )
	# plt.xlabel('Campaign ID')
	# plt.ylabel('Return per impression')
	# plt.legend(loc='upper left')
	# plt.show()

	st.subheader('First Touch Attribution')

	data_fta = {'Campaign_ID': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
	'Contribution': [0.08040201, 0.08333333, 0.09589041, 0.21276596, 0.15714286, 0.17948718,
	 0.1509434, 0.02857143, 0.29824561, 0.11428571, 0.14285714, 0.20610687,
	 0.10925197, 0.24183007, 0.19705882, 0.05084746, 0.11111111, 0.05660377,
	 0.29411765, 0.05128205, 0.1,        0.07777778, 0.23076923, 0.26190476, 
	 0.21212121, 0.14285714, 0.19402985, 0.12337662, 0.11564626, 0.10752688,
	 0.16911765, 0.13636364, 0.08219178, 0.14423077, 0.13517241, 0.12,
	 0.2,        0.07291667, 0.18461538, 0.17757009, 0.0,         0.24390244,
	 0.36,       0.27058824, 0.14705882, 0.09859155, 0.19727891, 0.09677419,
	 0.22346369, 0.05084746]}
	FTA = pd.DataFrame(data_fta)

	fta_bar = sns.barplot(x='Campaign_ID', y ='Contribution', data = FTA, color=(0.2, 0.4, 0.6, 0.6))
	fta_bar.set_xticklabels(fta_bar.get_xticklabels() , rotation=90, ha="right", fontsize = 7)
	st.pyplot()

	st.markdown('For this model, we found the minimum value of the normalized timestamp and gave it 100% of the weightage as this model emphasizes on discovery')

	st.subheader('Linear Attribution')
	data_lin = {'Campaign_ID': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
	'Contribution': [0.0351563,  0.05833333, 0.06262231, 0.11311968, 0.06652386, 0.13934676,
	 0.06666242, 0.01904762, 0.18504595, 0.05164835, 0.06690817, 0.0939511,
	 0.05714611, 0.1273509,  0.09719338, 0.0239025,  0.11111111, 0.02575673,
	 0.2262605,  0.02157831, 0.03319009, 0.03982804, 0.15171186, 0.17886432,
	 0.11695527, 0.06664974, 0.10371393, 0.05498966, 0.06422334, 0.06522296,
	 0.09231122, 0.06244535, 0.03150578, 0.05508087, 0.04925902, 0.06833333,
	 0.15634921, 0.02987351, 0.10338217, 0.08542501, 0.0,         0.16724739,
	 0.2429135,  0.21875817, 0.10532213, 0.05023474, 0.07207546, 0.05594448,
	 0.13140401, 0.03344431]}
	LIN = pd.DataFrame(data_lin)
	lin_bar = sns.barplot(x='Campaign_ID', y ='Contribution', data = LIN, color=(0.2, 0.4, 0.6, 0.6))
	lin_bar.set_xticklabels(lin_bar.get_xticklabels(), rotation=90, ha="right", fontsize = 7)
	st.pyplot()

	st.markdown('Linear attribution gives a more balanced look but it fails to highlight the most effective strategies that may have truly helped in conversion. For this particular model, the timestamp was normalized and equal weightage was given to all the touchpoints in the journey')

	st.subheader('Time Decay Attribution')

	data_tda = {'Campaign_ID':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
	'Contribution': [0.19062476, 0.13359402, 0.21500698, 0.45219494, 0.42189964, 0.32459297,
	 0.31157722, 0.04170178, 0.48527758, 0.22504065, 0.30118764, 0.44064813,
	 0.20572066, 0.47386639, 0.42961423, 0.09669172, 0.18972119, 0.11639765,
	 0.60135266, 0.13830427, 0.21921009, 0.10968338, 0.53263666, 0.47534501,
	 0.34265653, 0.25208998, 0.41415598, 0.25411434, 0.24208629, 0.23853916,
	 0.35744889, 0.30413892, 0.18966915, 0.2685294,  0.39420737, 0.26714394,
	 0.47819167, 0.16166493, 0.38686827, 0.3738728,  0.0,         0.44393803,
	 0.66585399, 0.49791271, 0.32941828, 0.18663626, 0.50196205, 0.18409656,
	 0.46655166, 0.10402354]}
	TDA = pd.DataFrame(data_tda)
	tda_bar = sns.barplot(x='Campaign_ID', y ='Contribution', data = TDA, color=(0.2, 0.4, 0.6, 0.6))
	tda_bar.set_xticklabels(tda_bar.get_xticklabels(), rotation=90, ha="right", fontsize = 7)
	st.pyplot()

	st.markdown('In this model, we can say that it is similar to linear attribution as it also gives emphasizes on all the touchpoints but the way it gives weightage drastically varies as the touchpoints closer to the time of conversion is given more weightage.')

	st.subheader('U Shaped Attribution')
	data_usa = {'Campaign_ID':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
	'Contribution':[0.03477706, 0.06111111, 0.0660274,  0.10896522, 0.07211535, 0.1358547,
	 0.05326146, 0.01714286, 0.2080117,  0.05584416, 0.07115941, 0.09149487,
	 0.05657818, 0.13551971, 0.09086099, 0.02014359, 0.11111111, 0.02716926,
	 0.23421369, 0.01882155, 0.0413851,  0.03648148, 0.16981285, 0.17023384,
	 0.0946892,  0.06192944, 0.09858742, 0.05135886, 0.05870889, 0.06751664,
	 0.08891607, 0.05906927, 0.02554638, 0.05718559, 0.04947172, 0.0626,
	 0.14620408, 0.02604798, 0.12270272, 0.08329328, 0.0,        0.15365854,
	 0.2274963,  0.21784314, 0.10362745, 0.04510396, 0.06486061, 0.05339167,
	 0.13618147, 0.03067797]}
	USA = pd.DataFrame(data_usa)
	usa_bar = sns.barplot(x='Campaign_ID', y ='Contribution', data = USA, color=(0.2, 0.4, 0.6, 0.6))
	usa_bar.set_xticklabels(usa_bar.get_xticklabels(), rotation=90, ha="right", fontsize = 7)
	st.pyplot()

	st.markdown('This model counts all the touchpoints emphasizing on the first and last touch points. For this, we have give 40% credit to the first and last touch points and ther est 20% is split between the intermediate touchpoints equally.')

	st.subheader('Logistic Regression')
	data_lr = {'Campaign_ID':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
	'Contribution':[0.00216253, 0.00232608, 0.00240678, 0.0023853, 0.00273383, 0.00259631,
	 0.00244698, 0.00224772, 0.00284641, 0.00278856, 0.00252788, 0.00252696,
	 0.00176995, 0.00290918, 0.0025484,  0.00181854, 0.00271356, 0.00201667,
	 0.00307334, 0.00232065, 0.00227443, 0.00196627, 0.00265682, 0.00255898,
	 0.0028988,  0.00255575, 0.00241383, 0.00208689, 0.00241719, 0.00218424,
	 0.00219224, 0.00235042, 0.00201438, 0.00241052, 0.00265763, 0.00224938,
	 0.00306203, 0.00219938, 0.00305411, 0.00279735, 0.00245667, 0.00260419,
	 0.00328661, 0.00295352, 0.00260348, 0.00233819, 0.00333214, 0.00209907,
	 0.00277404, 0.00194594]}
	LR = pd.DataFrame(data_lr)
	lr_bar = sns.barplot(x='Campaign_ID', y ='Contribution', data = LR, color=(0.2, 0.4, 0.6, 0.6))
	lr_bar.set_xticklabels(lr_bar.get_xticklabels(), rotation=90, ha="right", fontsize = 7)
	st.pyplot()

	st.markdown('logistic regression estimates the true incremental number of purchases or conversions that can be attributed to or give credit to a given marketing channel.')

	st.subheader('Comparison of Multi Touch Attribution')
	#st.subheader('LTA vs Time Decay')

	LtavsTd = Image.open('LTAvsTDA.png')
	st.image(LtavsTd, caption = "Last Touch Attribution vs Time Decay Attribution", width = 800, height = 1000)

	st.markdown('Comparing Last Touch Attribution vs Time Decay Attribution, it is very evident that Time Decay Attribution always gives a higher contribution for almost every touchpoint')

	TdvsUsa = Image.open('TDvsUSA.png')
	st.image(TdvsUsa, caption = "Time Decay Attribution vs U Shaped Attribution", width = 800, height = 1000)
	st.markdown('Comparing Time Decay Attribution and U Shaped Attribution, we can see that once again Time Decay Attribution seems to give a higher contribution for every touchpoint')


	LtvsLinear = Image.open('LTvsLinear.png')
	st.image(LtvsLinear, caption = "Time Decay Attribution vs U Shaped Attribution", width = 800, height = 1000)
	st.markdown('Comparing Linear Attribution and Last touch Attribution, there is a clear distinction in the contribution of Linear Attribution and Last Touch Attribution in which Last touch attribution always has a higher contribution')





	# fig = plt.figure(figsize=(18,8))
	# ax = fig.add_subplot(111)
	# plt.bar(range(len(FTA['Campaign_ID'])), FTA['Return_of_Investment'], label='FTA' )
	# plt.xlabel('Campaign ID')
	# plt.ylabel('Return per impression')
	# plt.legend(loc='upper left')
	# plt.show()
	# plt.close()

	
	st.markdown('After Modeling, we created a simulation algorithm to validate the whether the model will work if we allocated budgets to different channels based on the attribution weights. The below graph is used to compare different Return of Investment Models and to decide the marketing objective.')
#711,734,756,760,740,690,625,570


	#eward_list= [560,563,558,511,578,594,573,512,595,621,591,528,635,679,630,531,671,762,653,545,692,786,665,575,706,803,672,598,692,859,686,617]
	#reward_list= [560,563,558,511,578,594,573,512,595,621,591,528,635,679,630,531,671,762,653,545,692,786,665,575,706,803,672,598,692,859,686,617, 560, 580, 590, 610, 740,770, 790,840]
	#reward_list= [710,711,711,595,732,734,730,596,762,750,756,598,782,732,789,599,780,705,773,613,753,678,747,628,728,607,733,643,699,533,701,650]
	reward_list= [710,711,711,595,711,732,734,730,596,734,762,750,756,598,756,782,732,789,599,760, 780,705,773,613,740,753,678,747,628,690,728,607,733,643,625,699,533,701,650,570]

	print(len(reward_list))
	pitch_list= [0.1,0.25,0.5,1.0,1.5,2.0,2.5,3.0]
	print(len(pitch_list))
	lta_list=[]
	lin_list=[]
	usa_list=[]
	la_list=[]
	tda_list=[]
	i = 0
	while i < len(reward_list):

	  lta_list.append(reward_list[i])
	  #lin_list.append(reward_list[i+1])
	  #fta_list.append(reward_list[i+2])
	  usa_list.append(reward_list[i+1])
	  tda_list.append(reward_list[i+2])
	  la_list.append(reward_list[i+3])
	  lin_list.append(reward_list[i+4])
	  i = i+ 5
	import matplotlib.pyplot as plt 
	a=[lta_list,usa_list,tda_list,la_list, lin_list]
	b=['LTA','USA','TDA','LogReg', 'Linear']
	variables = st.sidebar.multiselect("Select the variables. LTA- Last Touch Attribution, USA- U Shaped Attribution, TDA- Time Decay Attribution, LogReg- Logistic Regression, Linear- Linear Attribution", b)
	for i, j in zip(a, variables):
	  plt.plot(pitch_list, i,marker='o',label=j)
	plt.legend()
	plt.xlabel('Pitch')
	plt.ylabel('Return on Investment')
	plt.show()
	st.pyplot()



def load_reference():
	st.title('REFERENCES')
	st.markdown('https://www.bizible.com/blog/marketing-attribution-models-complete-list')
	st.markdown('https://www.callrail.com/blog/guide-to-u-shaped-attribution/')
	st.markdown('https://www.marketingevolution.com/marketing-essentials/multi-touch-attribution')
	st.markdown('https://agencyanalytics.com/blog/marketing-attribution-models')
	st.markdown('https://nation.marketo.com/t5/Product-Discussions/Channel-based-vs-Campaign-based-tracking/td-p/135041')
	st.markdown('https://www.adroll.com/blog/marketing-analytics/first-last-touch-attribution-why-its-out-of-style')

def load_conclusions():
	st.title("Conclusions")
	st.markdown("Attribution allows you to trace the consumer journey to evaluate the performance of your marketing efforts. It helps you better understand how your efforts impact the entire sales cycle, and how your various channels and touchpoints work together to produce optimal results. By measuring and evaluating the performance of your marketing channels on a user level, you can distribute resources in a way that drives the most conversions at the lowest cost to your business.")
	st.markdown('* After plotting the comparison graphs of every attribution model against each other, we can observe that time decay attribution comparatively performs better than the other models')
	st.markdown('* The contribution of U shaped attribution model is the least')
	st.markdown('* At the raw attribution weight of 3.0, time decay provides the best return of investment')
	st.markdown('* Time decay attribution seems to give a higher return of investment almost throughout the pitch though initially linear attribution gives more return of investments in pitches of 0.0, 0.5')
	st.markdown('* Throughout the pitches, both Time decay and Last Touch attribution seems to give almost the same return of investment as they are very plotted very close to each other')
	st.markdown('* Logistic Regression Attribution gives lowest return of investment throughout the pitches.')
main()


