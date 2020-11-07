# QU Analytics - Implementing Visual Search

We are building and implemented visual search algorithms for QU Analytics Client. The client is a large e-tailer (CouchSmart) who has millions of products in its catalog. They intend to enhance the user-experience of their clientele by providing rich and engaging interfaces without leaving their couches!
Many products fundamentally appeal to our perception. When browsing through outfits on clothing sites, looking for a vacation rental on Airbnb, or choosing a pet to adopt, the way something looks is often an important factor in our decision. The way we perceive things is a strong predictor of what kind of items we will like, and therefore a valuable quality to measure.

![alt text](https://cdn.searchenginejournal.com/wp-content/uploads/2017/09/visual-search-1-760x400.png)

![alt text](https://miro.medium.com/max/7506/1*bYHl1xaEiJVD7BxOxR7gBw.png)

## Dataset 

The dataset was from Kaggle Competition : kaggle.com/c/cdiscount-image-classification-challenge

The source file used was in the form of binary JSON :

train.bson - (Size: 58.2 GB) Contains a list of 7,069,896 dictionaries, one per product. Each dictionary contains a product id (key: _id), the category id of the product (key: category_id), and between 1-4 images, stored in a list (key: imgs). Each image list contains a single dictionary per image, which uses the format: {'picture': b'...binary string...'}. The binary string corresponds to a binary representation of the image in JPEG format.

### Steps involving the processing of the file :

Formulating dataframe from bson file by decoding it using bson package and segregating product and category ids
Getting count of products per category and selecting 100 categories with 100 products in every category
Selecting only initial categorical ids and products ids and ingesting them into dataframe to further convert into csv for local notebook
In this way, dataset was reduced from the orders of gigabytes to kilobytes
Loading the bson iterator on local jupyter notebook to get images of only the categories and products we selected

![alt text](https://lh4.googleusercontent.com/XdvooH4-0HfgVAHRIzHYczyESvK7zcV2kJAeCQJHm8eOlAjsNp-TDEvczwarqehGa6WfQeDnNfwmdTGDJOrqMP5cpBvfqqM1f7bikx6JOBYpd7fLo-S_1QT4VveJKhdyDFFeLhJi)

## Neural Style Transfer Algorithm
Neural style transfer is an optimization technique used to take two images—a content image and a style reference image (such as an artwork by a famous painter)—and blend them together so the output image looks like the content image, but "painted" in the style of the style reference image.

This is implemented by optimizing the output image to match the content statistics of the content image and the style statistics of the style reference image. These statistics are extracted from the images using a convolutional network.

![alt text](https://lh5.googleusercontent.com/0TtjCJyOhnbuZHjPTh35yN6fu2t7PwFV0NhGmSt9TF4f6Ov_1w33QyhP2f4rNDitC7Z41pgYiM5JOqIw4FXLvXOdZ-VsQBH2mdo8kTV75Ib4smY2GFGh0P8GBKsxUZJWBhj6PBdS)
## Facebook AI Similarity Search

FAISS is a C++ library (with python bindings) that assures faster similarity searching when the number of vectors may go up to millions or billions.

At its very heart lies the index. The index is everywhere. This index can be stored on the disk and then items can be searched through this index to get similar ones.

![alt text](https://engineering.fb.com/wp-content/uploads/2017/03/GOcmDQEFmV52jukHAAAAAAAqO6pvbj0JAAAB.jpg)
![alt text](https://lh4.googleusercontent.com/7YLLuUIO7saJ72SzW0rjfFB1RKqSIWZG2cd2VE96Ovp5uHOtnQU2S6P1hhzilL8Wi3efPdV7LyJjJl4WaD8kqQco8_Boe6pfDRgc3o357pLCMechreJsrcDV4yIDsR109aaFvAo-)

## Spotify Annoy Method

Image similarity detection is used to quantify the degree of visual and semantic similarity of the images. Duplicate product detection, image clustering, visual search, and recommendation tasks are performed with this technology in modern applications.An image feature vector is a list of numbers that represents a whole image, typically used for image similarity calculations or image classification tasks. In general, low-level image features are minor details of the image, such as lines, edges, corners or dots. High-level features are built on top of low-level features to detect objects and larger shapes in the image.

Annoy (Approximate Nearest Neighbor Oh Yeah), is an open-sourced library for approximate nearest neighbor implementation. We will need the image feature vectors in a given set that is closest (or most similar) to a given feature vector.There are just two main parameters needed to tune Annoy:

the number of trees n_trees and the number of nodes to inspect during searching search_k.
n_trees is provided during build time and affects the build time and the index size. A larger value will give more accurate results, but larger indexes.
search_k is provided in runtime and affects the search performance. A larger value will give more accurate results, but will take longer time to return

![alt text](https://lh4.googleusercontent.com/GJwqXj8pxrnOPQs518HGoOtvmjBKnDzIktqD33PS7ln9WNo4BAxyOatv826Lx0keOzdCCu3tKgaxk7-x88NP41JCFT246guXnNIjIIZZuGG6HecGZ-33t3MLWiE95nvdiIKS-RqM)

## Elasticsearch Kibana

We leveraged elasticsearch as a search engine for Neural Style Transfer algorithm and indexed the images with their similar ones. For this, we used Kibana UI to fire bulk json statements. TO get the images displayed on the web application we used, AWS S3 to store them.

Alternatively, this can also be done using Postman.

![alt text](https://lh4.googleusercontent.com/4WOhGI9nod8VYErBswX21Oz7Q62eBxEmHV3w1Z3lODrI4KOe1kRkxlLqcMAIRs8bTrvMsvSeLKwIVE7Zi3bb5Ag7bupZzQtgGLUXVJH1pCksP1yg-9N3TLaRIJjWOGrqtKhJt_3o)

![alt text](https://lh5.googleusercontent.com/hwcB8CLIEC_OeqGOjMI2SCmKoow6RMHilAfB8oX3UEx-FECA4fldIkGnfJ0jvMwDj7V-urSuBrJj0Av_L2NZTV_rH1ML2f-eLLNos23YTPsKpUvl8C8f5soI15qMHwQ4vdLtbrDg)

## Heroku Deployment

Entire application was deployed on Heroku : https://faissmodell.herokuapp.com/

![alt text](https://lh6.googleusercontent.com/HBbcr8QgDDMog6e_efjE-GZNqIaBcHzeZPVwVlabeRBrq80UYdcYqUnq7KgafhFYB23GBT2R39uLOOMG2d95_Hv822r0qIrrHIvT4QYoVWsZGnmUcSJ33CFoqOsngWhEArWs35dh)
![alt text](https://lh6.googleusercontent.com/DlLYa-lnWQQvoheZEBjQUpoPdiKDuluiJ-MwXQDJIEK-_DmPrJmGnsDcmjQI150ZP636BIf13hN5-DfgCKMgK-SP2B8yMk5iSuOEeUHbMnJX-6D-8riNCC2jZ2uHYQtv7ReyhubA)
![alt text](https://lh3.googleusercontent.com/_MQLbopyRppc6fZhot4JoYeOmj1hpPMlDDAGYHs1doSq_aRX-fIPlP_4OTKmB6Z7_PNcxeJL7GfJDx09RGE3J8nKStfdQpJgf4Obh7OnADab-Achv7GhvI-4zZwNQqgUmDocwMEq)



