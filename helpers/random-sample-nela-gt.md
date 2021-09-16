```python
from glob import glob
import random

def read_files(outlet, randomN):
    path_to_full_sample = '../../bdaca-notes/teachingteacher'

    files = glob(f"{path_to_full_sample}/articles/*/{outlet}/*")
    fnames = []
    articles = []
    for filename in files:
        fnames.append(filename)
        with open(filename) as f:
            articles.append(f.read())

    art_dict = dict(zip(fnames, articles))

    return dict(random.sample(art_dict.items(), randomN))

infowararticles = read_files('Infowars', 2000)
bbcarticles = read_files('BBC', 2000)


def write_files(sample):
    for k, v in sample.items():
        full = "/".join( k.split("/")[-3:])
        second_ = "/".join( k.split("/")[-3:-1])
        base = 'articles/'
        os.makedirs(f'{base}{second_}', exist_ok=True)
        with open(f'{base}{full}', 'w') as w:
            w.write(v)

write_files(infowararticles)
write_files(bbcarticles)
```
