import streamlit as st
import pandas as pd
# from PIL import Image

st.title("Snack Recommendation System using SAR algorithm")
data=pd.read_csv('snackreviews.csv',header=0)

st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #F7DC6F
    }
    </style>
    """,
    unsafe_allow_html=True
)

images = {0 : 'https://i.imgur.com/zXlOo0d.jpg',
1: 'https://i.imgur.com/iKc25Sw.jpg',
2: 'https://i.imgur.com/bpzc3X0.jpg',
3: 'https://i.imgur.com/AOOIb64.jpg',
4: 'https://i.imgur.com/OSPvJkO.jpg',
5: 'https://i.imgur.com/kPyfdYu.jpg',
6: 'https://i.imgur.com/NQx6ONq.jpg',
7: 'https://i.imgur.com/OaHLX7d.jpg',
8: 'https://i.imgur.com/CoUSvL9.jpg',
9: 'https://i.imgur.com/9dQQu12.jpg',
10: 'https://i.imgur.com/r3MW2Ai.jpg',
11: 'https://i.imgur.com/Gp1n3NQ.jpg',
12: 'https://i.imgur.com/muf8qFU.jpg',
13: 'https://i.imgur.com/CHJEuRv.jpg',
14: 'https://i.imgur.com/DXtykGm.jpg',
15: 'https://i.imgur.com/pOFlSUC.jpg',
16: 'https://i.imgur.com/XiTJbnx.jpg',
17: 'https://i.imgur.com/YcG2wSK.jpg',
18: 'https://i.imgur.com/CKjGOlC.jpg',
19: 'https://i.imgur.com/0Jg4WNs.jpg',
20: 'https://i.imgur.com/8JU9V1F.jpg',
21: 'https://i.imgur.com/tu5UL8J.jpg',
22: 'https://i.imgur.com/iDHgrMQ.jpg',
23: 'https://i.imgur.com/rMHsaXK.jpg',
24: 'https://i.imgur.com/HFNgoqC.jpg',
25: 'https://i.imgur.com/vju2gZc.jpg',
26: 'https://i.imgur.com/DjUWPpB.jpg',
27: 'https://i.imgur.com/8JfMa1N.jpg',
28: 'https://i.imgur.com/lqwrvze.jpg',
29: 'https://i.imgur.com/LJeP5nQ.jpg',
30: 'https://i.imgur.com/srYGWf2.jpg',
31: 'https://i.imgur.com/c0rvWPm.jpg',
32: 'https://i.imgur.com/Tr0vKr7.jpg',
33: 'https://i.imgur.com/07o8QXQ.jpg',
34: 'https://i.imgur.com/9BmjyHX.jpg',
35: 'https://i.imgur.com/IUYP4lw.jpg',
36: 'https://i.imgur.com/1IB5bFg.jpg',
37: 'https://i.imgur.com/f712ItU.jpg'}

#st.image('https://i.imgur.com/zXlOo0d.jpg', width = 200)
	
user_input = st.text_input("Enter user id")
slid=st.slider('Select number of items to be recommeded :', 0, 10, 1)
if st.button('Recommend'):
	if user_input == "":
		st.text('Please enter valid user_id')
	else:
		top_k = pd.read_csv("recom_items.csv")
		data=pd.read_csv('snackreviews.csv',header=0)
		top_k_with_titles = (top_k.join(data[['SnackId', 'Snack']].drop_duplicates().set_index('SnackId'), 
		                                on='SnackId', 
		                                how='inner').sort_values(by=['Userid', 'Prediction'], ascending=False))
		user_input = int(user_input)
		result = top_k_with_titles[top_k_with_titles['Userid']== user_input]
		for j in range(0, slid):
			snack = result.iloc[j]['SnackId']
			st.subheader(result.iloc[j]['Snack'])	
			link = images.get(snack)
			st.image(link, width = 200)
		st.subheader('Performance of SAR Algorithm')
		st.image('prec.jpg',width=600)
		st.image('recall.png',width=600	)

