# gesis-machine-learning

This repository contains study materials belonging to the course "[A practical introduction to Machine Learning](https://training.gesis.org/?site=pDetails&child=full&pID=0x5F6D5D9F21934389B6F217EA093F8180&subID=0xD00A750313384AFC8E83C510C6662B3B)" ([Gesis](https://www.gesis.org/home), 27.09 - 01.10.2021) by Damian Trilling and Anne Kroon.

------

# Course description

The course will provide insights into the concepts, challenges and opportunities associated with data so large that traditional research methods (like manual coding) cannot be applied anymore and traditional inferential statistics start to lose their meaning. Participants are introduced to strategies and techniques for capturing and analyzing digital data in communication contexts using Python. The course offers hands-on instructions regarding the several stages of computer-aided content analysis. More in particular, students will be familiarized with preprocessing methods, analysis strategies and the visualization and presentation of findings. The focus will be in particular on Machine Learning techniques to analyze quantitative textual data, amongst which both deductive (e.g., supervised) machine learning and inductive (e.g., unsupervised machine learning) approaches will be discussed.

------


# Schedule

## General schedule

|   |    |
| -- | -- |
| 09.00—11.00 |     Lecture Part I   |
| 11:00—12.30:|   Exercises Part I   |
| 12.30—13.30:|    Lunch break       |
| 13.30—15.30:|    Lecture Part II   |
| 15.30—16.30:|     Exercises Part II |
| 16.30—17.00:|  Plenary discussion exercises / wrap up |



## Topics per day

* [Monday](day1/): **From text to features**
    - Introduction
    - Working with Python: A refresher
    - From text to features
      - Vectorizers
      - document-term matrix

  - Exercise: Setting up a simple machine learning algorithm using count/ tfidf vectorizers

* [Tuesday](day2/):  **Language Processing and feature engineering**

    - NLP techniques (pre-processing, regular expressions)
    - Advanced NLP-techniques, such as Named Entity Recognition (NER), using `spaCy` and `NLTK`
    - Exercise: Extend feature engineering of yesterday's dataset, and investigate effects on performance of the classifier

* [Wednesday](day3/): **Unsupervised Machine learning**

    - Clustering features: e.g., PCA
    - Clustering cases: e.g., K-means clustering, LDA
    - Exercise: Practice with different unsupervised machine learning algorithms

* [Thursday](day4/): **Supervised Machine Learning**

    - Basics of supervised machine Learning
      - Evaluation metrics
      - Different type of classifiers (e.g., Naive Bayes, SVM, ..)
    - Optimizing supervised learning, in light of concepts such as overfitting, regularization, cross-validation and hyper-parameter tuning

* [Friday](day5/): **Advances in Machine Learning**
    - Word embeddings
    - Deep learning with `Keras`
