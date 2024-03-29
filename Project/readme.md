# Dunnhumby - The Complete Journey

## Introduction

An algorithmic marketing approach to understand the response and effects of transactions during different campaigns. Dunnhumby work with a range of sectors,including grocery retail, retail pharmacy, and retailer financial services. The expert teams work alongside their global clients in these sectors, helping them to make the most of their customer data and to put the Customer at the heart of everything they do.
The overall data which has been collected contains demographics of 2500 households who have been customers at various retail stores managed by Dunnhumby. There were different campaigns ran by Dunnhumby by introducing coupons for discounts on various households. Some of them reacted and showed interest, made purchasing and others did not redeem the coupons. In this current situation we have to study the kind of households we are dealing with us and analyze their buying behaviours. A marketing and machine learning based solution should be designed to approach this situation for the growth of our retail stores and help them to maximize profit.

![alt text](https://lh6.googleusercontent.com/jjRWS6AWq4D0_ydeLRxrHVIKJGKFth4a5VudZU8LTK4sKhOAHDKriuNxII0i-6nkpldjtTMgcbMqG_54Wkqu4kYdi1HkJ8jH-jFA0ZZS6T3TVnrgkeVx1xQWWYLQCb-HbWf0xkFO)

## Goals

### Household Segmentation using RFM modeling

Segregating 2500 households based on their transactional history over the two years, to understand the plan to maximize profit.

### Predictive Analytics for Coupon Redemption

Devising a ML based model to predict whether a household is sensitive to coupon or not. This will help retailers to customize coupon codes to maximize the overall outcome.


## Flow Diagram

![alt text](https://lh3.googleusercontent.com/CmRUB0Pvv6pNl7XflTFNOWGKE6YiOlyDQ2_3JfvRlEOkS5RgTnNkbq9hqD2wynVnV8_hiyS6bB7Q7oX2WSOcX2nFXA3c_keREbbX0WSmq9szBNjlVXD2eu9Xpp9m87eHP2ekKW_g)

The data pipeline was architected using GCP platform. The raw csv files were stored on Cloud storage. A database was built on Cloud SQL which migrated csvs from Cloud Storage using a migration engine. The SQL queries were ran on Cloud SQL using Big Query, to perform custom joins and other relational operators.

The tables were connected to Google Data Studio, where the two reports for Housing and Coupons were developed. Similarly, for colab, Drive was hosted as a storage due to its simplicity. Sklearn underlying architecture was developed to build ML models. The entire architecture was set up and built on streamlit due to its simplicity. The application was hosted on Heroku Platform.

## Dashboards

![alt text](https://lh5.googleusercontent.com/oj35FSmzAg2BvssvMUPdB77Jpvg4ajiU5K9_MLuzH9SgqRW7_QuykF56FoxSSbFi5SwpaD7oldDn-gG6L91tY4P_Wx9Ibc7SftEkna6jIgB5hHStCzsfi-qSe_vwltojtMVwKuN4)
![alt text](https://lh6.googleusercontent.com/dhP5UlMlEfT5ZhL2MMDQ8djzgMG8W6OJGCsBwtaPKhJ_HVHS7a-kLGqxumQy9a6nmzEPrB0QHx6hvUpkbKIsIFYJ1x2EMJLiXWuVwoo1lWDo1Qjwax27GloIjMk7tCWCxQ7MxDtb)

## Customer Segmentation

Customer segmentation is the process of dividing customers into groups based on common characteristics so companies can market to each group effectively and appropriately.Segmentation allows marketers to better tailor their marketing efforts to various audience subsets. Those efforts can relate to both communications and product development.Customer segmentation requires a company to gather specific information – data – about customers and analyze it to identify patterns that can be used to create segments.

![alt text](https://lh3.googleusercontent.com/ztVXiXIO0qVkxmLmIRngLV1zaBZCg1XKxJuaqHdSuqZCHB4RsE02sgvvW3ixqAKo_iScRqewMU6XHnbKa_X-uj7k4V9n_vFlCLilYGncW5XMLFM2IZa-1UHCCrPZ1MAUIERkvft7)

![alt text](https://lh3.googleusercontent.com/uvzKiiH8VsQ48T1mo5O7YN6S3NxpMkDLizuKzf5OdIi3GQ4MCdxrE2fZNutrjjQrJtXaUKyu3HvA4lAAnIl_tSg6qsEVitl6sT18UXwhXnRtrHr5Yco6mOzjffyS0mr-l2V_brXY)

## Predictive Analytics : Coupon Redemptions

We have devised a model which predicts whether a particular household would be sensitive to coupons or not. Multiple datasets were joined, in which we had demographics, separate tables and coupons and their transactions. The dataset was a mix of categorical and numerical variables which consisted of custom columns like total visits and sales generated by them. As a result, logistic regression, decision tree and ensemble models were trained.

![alt text](https://lh4.googleusercontent.com/caQSJZa70QcnLShzO7LNLIZYrurdgdrUN6V5UZwQ3z2QZnBmEztGGFqWhuHrGfbvVjAj9TcLUcN1yEoA3jDAqD_11zDnr25z_9dd5k56_auIN5cSxX1ik5MQtQjaThSCFJ-QHQWq)
![alt text](https://lh4.googleusercontent.com/nB4AczITnNxkSD1Igp21mDIGUTbTprSg9u7IUydoT41oBxJq36G7K4rb77cmS_AyYENr-xfbenpDunpdlWZ8d6SuMgRIY72gMxgdWVucIofVazTWE3NwZaXSglEXUqfOwn2X11MO)

We needed a high precision score, because we want to make sure that we select the right customers and target coupons for them. Due to this we got logistic regression with 0.8, however, while testing the model, the influence of categorical variables had less impact on the model. Hence we decided to move ahead with the decision tree classifier as it had more accuracy and a precision score of 0.71 on the test data.

![alt text](https://i.ibb.co/QP5ScQD/1.jpg)
![alt text](https://i.ibb.co/xC8zCYL/2.jpg)


## Streamlit Heroku Deployment

The application is deployed on : http://dummhumbycamp.herokuapp.com/
![alt text](https://lh6.googleusercontent.com/vqvpq9slGAMbocpUoxtPjGsX1LMkIvIrabLnESgCNkEnlhjaYGk94cewd8NhS9Ybg2wTd4P4GtlVqUeBnPdY7254ydLbsKx_LluRCmPQYQlkADB3_dV3WhIrJoX_2l6fc85RBqIV)

## Steps to replicate 

1. Clone the repository
2. For MAC Users, install Heroku on terminal using: curl https://cli-assets.heroku.com/install.sh | sh
4. For Windows Users, download gz file from https://devcenter.heroku.com/articles/heroku-cli
5. From terminal/cmd go to the INFO7374-Algorithmic_Digital_Marketing/Project/Streamlit-Heroku Deployment
6. Run the commands :
7. git init
8. heroku login
9. heroku create app-name
10. git add .
11. git commit -m 'first commit'
12. git push heroku master

The app will be deployed to app-name.herokuapp.com


