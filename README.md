# OIBSIP_EMAILSPAM-DETECT
This code is a Streamlit app for email spam detection using a Multinomial Naive Bayes classifier. It loads email data, trains the classifier, and displays accuracy. The app visualizes spam/ham counts and predicts if user-inputted emails are spam or valid, showing results with color-coded text.

# Email Spam Detection with Machine Learning

This repository contains a Streamlit app that uses a Naive Bayes classifier to detect email spam. The app allows users to input an email text and predicts whether it is spam or a legitimate (ham) email.

## Table of Contents

1. [Introduction](#introduction)
2. [Analysis Section](#analysis-section)
3. [Streamlit App Section](#streamlit-app-section)
4. [Conclusion](#conclusion)

## Introduction
This Streamlit app focuses on email classification using a Naive Bayes classifier. It uses a dataset containing email texts labeled as either "spam" or "ham" (legitimate). The app preprocesses the text data, trains a classifier, and provides users with the ability to test email texts for spam detection.

## Analysis Section
The script begins by importing necessary libraries and loading the email dataset. It provides an overview of email classification, distinguishing between "spam" and "ham." The dataset is preprocessed using a CountVectorizer to convert text data into numerical features.

## Streamlit App Section
The Streamlit app interface starts by displaying the title and a brief explanation of spam and ham emails. It allows users to input an email text and click the "Predict" button. The app then displays the prediction as well as whether the predicted email is fake or valid. Additionally, it presents the accuracy of the classifier and a bar chart showing the distribution of spam and ham emails in the dataset.

## Conclusion
This Streamlit app offers a practical tool for detecting email spam using a Naive Bayes classifier. Users can input email texts to determine whether they are spam or legitimate. It provides insights into text classification and machine learning.

Created with expertise by  Rajvardhan 
For any inquiries or feedback, please feel free to reach out to me at raj2003patil@gmail.com.

**Note:** Ensure you have the required libraries, Streamlit, and a compatible Python environment to run this app successfully.
