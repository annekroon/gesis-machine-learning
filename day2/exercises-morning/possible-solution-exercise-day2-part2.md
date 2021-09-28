### using manually crafted features as input for supervised machine learning with `sklearn`


```python
import nltk
from sklearn.model_selection import train_test_split

from glob import glob
import random


def read_data(listofoutlets):
    texts = []
    labels = []
    for label in listofoutlets:
        for file in glob(f'../articles-small/*/{label}/*'):
            with open(file) as f:
                texts.append(f.read())
                labels.append(label)
    return texts, labels

documents, labels = read_data(['Infowars', 'BBC'])
```

Create bigrams and combine with unigrams  

```python
documents_bigrams = [["_".join(tup) for tup in nltk.ngrams(doc.split(),2)] for doc in documents] # creates bigrams
documents_bigrams[7][:5] # inspect the results...

# maybe we want both unigrams and bigrams in the feature set?
assert len(documents)==len(documents_bigrams)

documents_uniandbigrams = []
for a,b in zip([doc.split() for doc in documents],documents_bigrams):
    documents_uniandbigrams.append(a + b)

#and let's inspect the outcomes again.
documents_uniandbigrams[7]
```

some sanity checks:

```python
len(documents_uniandbigrams[7]),len(documents_bigrams[7]),len(documents[7].split())
assert len(documents_uniandbigrams) == len(labels)
```

Now lets fit a `sklearn` vectorizer on the manually crafted feature set:

```python
from sklearn.feature_extraction.text import CountVectorizer
X_train,X_test,y_train,y_test=train_test_split(documents_uniandbigrams, labels, test_size=0.3)
myvectorizer= CountVectorizer(analyzer=lambda x:x)
#myvectorizer = CountVectorizer(ngram_range=(1,2))
```

let's fit and transform

```python
#Fit the vectorizer, and transform.
X_features_train = myvectorizer.fit_transform(X_train)
X_features_test = myvectorizer.transform(X_test)
```

Inspect the vocabulary and their id mappings

```python
# inspect
myvectorizer.vocabulary_
```

Finally, run the model again

```python
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

model = MultinomialNB()
model.fit(X_features_train, y_train)
y_pred = model.predict(X_features_test)

print(f"Accuracy : {accuracy_score(y_test, y_pred)}")
print(classification_report(y_test, y_pred))
```
