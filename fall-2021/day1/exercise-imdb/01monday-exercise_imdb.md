# A Practical Introduction to Machine Learning in Python
Anne Kroon and Damian Trilling

## Day 1 (Monday)

## Exercise: "Getting Started" with the IMDB dataset

Download and unpack the ACL IMDB dataset (https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz).
Windows users may need an additional program to unpack it, such as 7zip. 

Quick way to get everything on Linux:
```
wget https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz
tar -xzf aclImdb_v1.tar.gz

```


Specific tasks

1. Think of a good data structure to read this data in1
2. Write a script to read the data in.
3. Discuss (first in groups, then plenary) the pro's and con's of different ways of organizing the data.
4. Train a first Naive Bayes classifier on the dataset. No worries, we will discuss all the details behind each of the steps in this week; you can for now just rely on the script below. You may need to change variable names such as `y_test`, `y_pred`, `X_train_fulltext` etc. based on how you read your data, though.

```
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, classification_report

vectorizer = CountVectorizer(stop_words='english')
X_train = vectorizer.fit_transform(X_train_fulltext)
X_test = vectorizer.transform(X_test_fulltext)

nb = MultinomialNB()
nb.fit(X_train, y_train)

y_pred = nb.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

5. What is your first gut feeling about the results?
6. Can you explain what the different variables you created contain?
