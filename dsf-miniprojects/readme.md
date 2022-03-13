# The Data Incubator - Sample Data Science Miniprojects
Here you'll find a sample of 5 out of 8 miniprojects worked on as part of [The Data Incubator, Data Science Fellowship Program](https://www.thedataincubator.com/programs/data-science-fellowship/) that I participated in the Full-time Online Winter 2022 Cohort.

The Data Science Fellowship program is an immersive 8-week bootcamp-style shop that works with top talent `(~2% acceptance rate)` wanting to transition roles as professional Data Scientists. Typically fellows come from academia with advanced graduate degrees, however the program is also geared towards working professionals wanting to enhance their data science skillset.

The miniprojects were done in **Jupyter / IPython Notebooks** using the Digital Ocean Cloud Computing platform running on Linux.

Out of considerations for present and future Fellows **only limited and edited** scope of work of a **subset of miniprojects** are presented here. Feel free to inquire for more details as appropriate.

## (1) Data Wrangling & Webscraping - Examining The New York Social Graph

<a href="https://web.archive.org/web/20150913112557/http://www.newyorksocialdiary.com/">The New York Social Diary</a> provides a fascinating lens into New York's socially active and well-to-do individuals. As shown in <a href="https://web.archive.org/web/20150913112351/http://www.newyorksocialdiary.com/party-pictures/2014/holiday-dinners-and-doers">this report of a holiday party</a>, almost all the photos have annotated captions with names of the subjects in them. We can think of this as an implied social graph: there is a connection between two individuals if they appear in a picture together!

Methodologically this was performed using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) by scraping website pages with photo captions up to a given date cut off. These captions were then parsed to return unique names, revealing a total of ~110,000 names in the social network. The structure of this social network was analyzed via node degrees and pagerank algorithm. From this popularity and influence was gaged, and strength of connections (spouse, friends, family) can be proxied. 

_TOOLS USED_: BeautifulSoup, Dill, spaCy, NetworkX, Matplotlib

![network graph](https://github.com/bassaad17/tdi_pub/blob/main/dsf-miniprojects/images/1_social_graph.jpg)

## (2) Machine Learning - Predicting Yelp Star Ratings

The provided Yelp dataset contains unstructured metadata about each venue (city, latitude/longitude, category descriptions, etc), and numerical star ratings. Predicting a new venue's popularity from such information makes for a great Machine Learning problem. This miniproject contained all the classics from data wrangling in JSON, feature engineering, creating custom transformer in the ML pipeline, to an [ensemble regressor](http://scikit-learn.org/stable/modules/ensemble.html) 

_TOOLS USED_: NumPy, Pandas, Scikit-learn

## (3) SQL - Investigating NYC Restaurant Inspections

The City of New York inspects roughly 24,000 restaurants a year and assigns a grade to restaurants after each inspection is concluded. Over a decade, this created a public dataset of over 500,000 records. SQL was used to parse and analyze these inspections. Different slices were examined to determine the inspection grade distribution by zipcode, borough, and cuisines, with some cuisines tending to have a disproportionate number of violations.

_TOOLS USED_: SQL

## (4) Adv. Machine Learning | NLP - Predicting Yelp Ratings

Given the richness of information contained in text data, Yelp client review data was explored in the context of predicting ratings. Various natural language processing (NLP) techniques were explored on the text data. At its most fundamental level, words needed to be transformed into quantities via tokenizers and vectorizers.

_TOOLS USED_: spaCy, NumPy, Pandas, Scikit-learn, Bag of Words, Bigrams

## (5) TensorFlow - Image Classification with Neural Networks

Neural networks are all the rage in Machine Learning, and deservedly so for their high performance in tasks that spans far beyond image classification. In this project, a series of models are built to classify a series of images into one of ten classes `('airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck')`. For expediency, these images are pretty small (32×32×3). This can make classification a bit tricky---human performance is only about 94%. 

![example image](https://github.com/bassaad17/tdi_pub/blob/main/dsf-miniprojects/images/5_tf_frog.png)

The image above is a frog---now you see it! :)

TensorFlow is a popular framework as it is an open-source software library for "dataflow" programming. Computations are expressed as stateful dataflow graphs. The name TensorFlow derives from the operations neural networks perform on multidimensional data arrays (AKA "tensors"). 

A multi-layer fully-connected neural network achieves an accuracy of about 44% on a training set and 41% on a test set. A simple convolutional neural net achieves accuracy of 80% on a training set and 70% on a test set. A simple transfer learning model based on GoogLeNet achieves a training accuracy of 87% and a test accuracy of 85%.

_TOOLS USED_: TensorFlow
