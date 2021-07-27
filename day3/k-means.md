

### Euclidean distance

<img src="https://render.githubusercontent.com/render/math?math=d\left( p,q\right)   = \sqrt {\sum _{i=1}^{n}  \left( q_{i}-p_{i}\right)^2 }">


---


```python
from math import sqrt

plot1=[1,5]
plot2=[6,9]

euclidean_distance = sqrt ( (plot1[0]- plot2[0])**2 + (plot1[1]- plot2[1])**2)
```
