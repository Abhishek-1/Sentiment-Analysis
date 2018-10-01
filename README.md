# Sentiment-Analysis

Abstract
Given an opinion target in a sentence, we were required to predict the sentiment label for the aspect term in the sentence.


Introduction
Sentiment Analysis is the process of identification of opinions expressed in the form of text, the opinion here refers to the context of text being in positive, negative, or neutral light.

In this project we were required to bring out the opinion of sentence for the given aspect term context.
Since the project required us to focus on the aspect context, we moved forward by simplifying the complex sentence structure and seeking out the sub-sentences containing the aspect term.

In our project we were give out database of text with below given attributes.

Column A: review sentence id
Column B: review sentence
Column C: aspect term in the sentence
Column D: aspect term location
Column E: sentiment label

Strategy Used
•	Parse the entire dataset file to build a list of records.
•	Split the sentence using conjunctions (example: and, but, nor etc.) as delimiters to get sub-sentence with aspect term.
•	For the sub-sentence remove stop words and do POS tagging.
•	Make a list of Verbs, Adverb, and Adjective that are present in all the records.
•	Get the most frequent 1000 such words and they will become features.
•	Build a bag of words representation for all the records with the 1000 features and the class label.
•	Do 10-fold cross validation to get 10 sets each with test and training data.

Validation
We have used 10-fold cross validation for building our classifier model with the below breakup for each iteration.
Training Data – 90%
Test Data – 10%

Classification Models Used
•	Naïve Bayes
•	Linear SVM
•	K-Nearest Neighbor
•	Multinomial Naïve Bayesian
•	Bernoulli Naïve Bayesian
•	Logistic Regression
