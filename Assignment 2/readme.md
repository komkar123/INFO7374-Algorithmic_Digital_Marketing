# Marketa Analytics - Understanding promotions

## Introduction

Advertising tries to expand consumption in two ways; it both reminds and teaches. It reminds in-the-market consumers in order to influence their immediate brand choice and teaches to increase brand awareness and salience, which makes it easier for future advertising to influence brand choice. Adstock is the mathematical manifestation of this behavioural process
The theory behind adstock is that marketing exposures build awareness in consumers’ minds.  That awareness doesn’t disappear right after the consumers see the ad but rather remains in their memory.  Memory decays over the weeks and hence the decay portion of adstock.

Advertising effectiveness and Return on Investment (ROI) are typically measured through econometric models that measure the impact of varying levels of advertising Gross Ratings Points (GRPs) on sales or on purchase decision and choice. TV advertising has both dynamic and diminishing returns effects on sales, different models capture these dynamic and nonlinear effects differently.

![alt text](https://thinktv.ca/wp-content/uploads/2018/01/adstock_chart1.png)

## Objective

To observe the adstock effects through two different channels: 
Television and Radio 

## Salesforce Dashboard 

![alt text](https://i.ibb.co/MZwJkVM/Adstock-Dashboard.png)

## Insights

After analyzing the effects of the adstock model, we can conclude that it makes sense to invest in TV ads as the sales rate increased by some amount as compared to sales without any investment in advertisements. Radio advertisements do not seem to make any impact in sales hence spending on radio advertisements is not advisable. 

It's either because TV is more popular among the target consumers and is reflected in sales. Another reason could be that radio might not be the best medium of advertising for this product alone. Temperature could also have affected the sales depending on the product which is unknown but even if the advertisements have made an impact on the users, the users might not buy it because the temperature might not be suitable for the product. 

# Attribution Modeling and Budget Optimization

Marketers usually use multiple channels–such as sponsored search, display ads, and emails–to reach their customers, and each channel usually includes multiple activities or has multiple parameters that are associated with various costs. For example, a marketer can run several email campaigns, each of which corresponds to a certain price discount, or run sponsored search for multiple keywords, each of which is associated with a certain bid amount. On the other hand, customers usually interact with multiple touchpoints along the way to conversion, so that the effects from different touchpoints intertwine and accumulate

![alt text](https://i.ytimg.com/vi/BfnJwYuFWVM/maxresdefault.jpg)

This leads to the problem of marketing spend optimization, which requires estimating the true contribution of individual channels and activities to the final outcome and optimally allocating budgets across these channels, or even setting individual activity parameters such as bids in sponsored keyword search.

Criteo has published an online advertising dataset which has details of campaigns and budget allocated for each of them. The aim is to check the cross-channel Optimization using various parameters to access which channel should be getting the maximum budget for advertisement.

## Data
This dataset represents a sample of 30 days of Criteo live traffic data. Each line corresponds to one impression (a banner) that was displayed to a user. For each banner we have detailed information about the context, if it was clicked, if it led to a conversion and if it led to a conversion that was attributed to Criteo or not

♟ Timestamp : timestamp of the impression (starting from 0 for the first impression). The dataset is sorted according to timestamp.

♟ UID : Unique User Identifier

♟ Campaign : Unique Campaign Identifier

♟ Conversion : 1 if there was a conversion in the 30 days after the impression; 0 otherwise

♟ Conversion ID : A unique identifier for each conversion

♟ Click : 1 if the impression was clicked; 0 otherwise

♟ Cost: The price paid for this ad

♟ Cat1-Cat9 : Categorical features associated with the ad

## Key Figures
2.4Gb uncompressed
16.5M impressions
45K conversions
700 campaigns

## Comparison of multi touch models 

Comparing Last Touch Attribution vs Time Decay Attribution, it is very evident that Time Decay Attribution always gives a higher contribution for almost every touchpoint

![alt text](https://i.ibb.co/ZNjyN2r/74afd72cd180479595520b1b87619b2cc128f7a9bcb304ed9e68b4e2.png)

Comparing Time Decay Attribution and U Shaped Attribution, we can see that once again Time Decay Attribution seems to give a higher contribution for every touchpoint

![alt text](https://i.ibb.co/8sLyJ8d/c2b6f9be2328ec77c15393d25494622a5755d0bd1a9fd22e62105f02.png)

Comparing Linear Attribution and Last touch Attribution, there is a clear distinction in the contribution of Linear Attribution and Last Touch Attribution in which Last touch attribution always has a higher contribution

![alt text](https://i.ibb.co/0CShqMY/d1892a358598a37a662f20d4f09794a0ac71b9d10eb48eaffefc8d15.png)

## Simulation of Return of Investment (ROI) on different models

After Modeling, we created a simulation algorithm to validate the whether the model will work if we allocated budgets to different channels based on the attribution weights. The below graph is used to compare different Return of Investment Models and to decide the marketing objective.

![alt text](https://i.ibb.co/fFyrSmR/15b1dafc58715f29d8812ae152a4169057470cd9a5d1a67361a49083.png)

## Conclusion

Attribution allows you to trace the consumer journey to evaluate the performance of your marketing efforts. It helps you better understand how your efforts impact the entire sales cycle, and how your various channels and touchpoints work together to produce optimal results. By measuring and evaluating the performance of your marketing channels on a user level, you can distribute resources in a way that drives the most conversions at the lowest cost to your business.

After plotting the comparison graphs of every attribution model against each other, we can observe that time decay attribution comparatively performs better than the other models
The contribution of U shaped attribution model is the least
At the raw attribution weight of 3.0, time decay provides the best return of investment
Time decay attribution seems to give a higher return of investment almost throughout the pitch though initially linear attribution gives more return of investments in pitches of 0.0, 0.5
Throughout the pitches, both Time decay and Last Touch attribution seems to give almost the same return of investment as they are very plotted very close to each other
Logistic Regression Attribution gives lowest return of investment throughout the pitches.
