import os
from glob import glob

# unpack the dataset from https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz and store the folder 'aclImdb' in the same folder as this script

def read_data(dataset):
    texts = []
    labels = []
    for label in ['pos', 'neg']:
        for file in glob(os.path.join('aclImdb',dataset,label,'*.txt')):
            with open(file) as f:
                texts.append(f.read())
                labels.append(label)
    return texts, labels

X_train_fulltext, y_train = read_data('train')
X_test_fulltext, y_test= read_data('test')
