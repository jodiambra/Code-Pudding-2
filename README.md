# Tinder Relationship Predictions

![image](https://user-images.githubusercontent.com/115895428/222187881-112bd366-1be5-42e0-b60d-4fc51921cf4d.png)

## Introduction

Tinder is a popular dating app that allows users to create a profile and swipe through potential matches based on their location and personal preferences. Users can indicate their interest in a match by swiping right, or they can swipe left to pass. If two users both swipe right on each other, they are considered a match and can communicate with each other through the app's messaging system. Tinder's algorithm also takes into account factors such as mutual friends and common interests to suggest potential matches. The app is known for its simple and user-friendly interface, and it is available on both iOS and Android devices.

## Conclusions

We conducted EDA on the tinder dataset and highlighted some trends. We found more relationships with those that used Tinder, compared to those that did not use Tinder. This occurrence was confirmed with hypothesis testing, which suggested the relationship occurrences were different among Tinder users and non users. 

We then created a machine learning model to predict the relationship status of an individual, based on a few self reported features. Initially, the dataset was split into three groups: the full dataset, tinder users, and non users. The full dataset model had the best F1 score, while the non users model came a close second. A good F1 score suggests the model has good precision and recall, in other words, good at predicting both positive and negative classes. The tinder users model had an average F1 score, so the model does not accurately predict both the positive and negative classes. This was due to the small nature of the Tinder users dataset, which also left very little data to test the model. Overall, the best model to use for predictions is the model based on the full dataset. 

We tested our model with a dataset we created. The results of the model predict a relationship, with a 93.99% probability. 

Contrary to popular belief that Tinder is merely a hookup app, with relationships found far and few in between, our dataset suggests the opposite. Among these universities, individuals tend to have better luck finding a relationship using tinder. 
