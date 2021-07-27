#### Inspecting a dense DTM resulting from text vectorized with `sklearn`'s vectorizers

```python
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer

documents = ['the cat loved my sofa',
             'the dog loved my chair',
             'the bird loved my chair']

vectorizers= [("Count vectorizer", CountVectorizer() ) ,  ("Tfidf vectorizer", TfidfVectorizer() ) ]

for name, vec in vectorizers:
    vec.fit_transform(documents)

    print(f"\n{name}\n")

    print("\t".join(vec.get_feature_names()))  # just for printing nicely
    for row in vec.transform(documents).todense():
        print("\t".join([f"{float(e):.2}" for e in row[0].tolist()[0]]))
```

or, using `pandas`:

```python
import pandas as pd

vec = TfidfVectorizer() #or CountVectorizer()
X = vec.fit_transform(documents)
print(pd.DataFrame(X.A, columns=vec.get_feature_names()).to_string())
df = pd.DataFrame(X.toarray().transpose(), index = vec.get_feature_names())
```
