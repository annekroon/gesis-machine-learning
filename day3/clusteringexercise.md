# Clustering Exercise

Go to 
https://figshare.com/articles/News-Processed-Dataset/5296357 and download `WSJ_20170607_to_20170726_10AmTo4Pm.json` (the small file of 9 MB)

You can read a one-json-object-per-line (jsonlines) file as follows:

```
import json
data = []
with   open('/home/damian/Downloads/WSJ_20170607_to_20170726_10AmTo4Pm.json', encoding="utf-8") as f:
  for line in f:
    data.append(json.loads(line))
texts = [e['content'] for e in data]
```

For clustering code, see pca_svd_kmeans.ipynb
