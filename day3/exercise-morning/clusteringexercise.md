# Clustering Exercise

Go to
https://figshare.com/articles/News-Processed-Dataset/5296357 and download `WSJ_20170607_to_20170726_10AmTo4Pm.json` (the small file of 9 MB)

You can read this one-json-object-per-line (jsonlines) file (and select the only key we care about simultaneously) as follows:

```python
import json
with   open('/home/damian/Downloads/WSJ_20170607_to_20170726_10AmTo4Pm.json', encoding="utf-8") as f:
  texts = [json.loads(line)['content'] for line in f]
```


- Try out some unsupervised techniques, such as `PCA`
- Next, run the `kmeans`algorithms and try to determine the right number of `k`.   

For inspiration, see [here](pca_svd_kmeans.ipynb).

#### Code suggestion for getting the right number of `k`:

```python
### Estimate some models to determine the best value of `k`
wss = []
for i in range(2, 10):
    print(i)
    km = KMeans(n_clusters=i, init='k-means++', max_iter=100, n_init=5)
    km.fit(features)
    wss.append(km.inertia_)

### Plot total within sum of squares vs. number of clusters to get the elbow plot
plt.plot(range(2, 10), wss, marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Within groups sum of squares')
plt.show()
```
