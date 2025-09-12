from glob import glob

reviews=[]
test=[]

print("Constructing training dataset")

# glob gives you a list of filenames that match a specific criterion
# in this case, all .txt-files in the postivie training folder

for file in glob ("/home/damian/aclImdb/train/pos/*.txt"):
    with open(file) as fi:
        reviews.append((fi.read(),"1"))
nopostr=len(reviews)

print ("Added",nopostr,"positive reviews")  

for file in glob ("/home/damian/aclImdb/train/neg/*.txt"):
    with open(file) as fi:
        reviews.append((fi.read(),"-1"))
nonegtr=len(reviews)-nopostr
print ("Added",nonegtr,"negative reviews")  
   
print("Constructing test dataset")

for file in glob ("/home/damian/aclImdb/test/pos/*.txt"):
    with open(file) as fi:
        test.append((fi.read(),"1"))
noposte=len(test)
print ("Added",noposte,"positive reviews")  

for file in glob ("/home/damian/aclImdb/test/neg/*.txt"):
    with open(file) as fi:
        test.append((fi.read(),"-1"))
nonegte=len(test)-noposte
print ("Added",nonegte,"negative reviews")  

#%% Checking the data
# Thus, we got two lists, reviews and test.
# Both contain tuples (pairs of two values: The first is the review, 
# the second the classification: 1 or -1)
    
# We can easiliy verify this by looking at a random entry:
print(reviews[244])
# or
print('The following review\n\n\n',reviews[244][0],"\n\n\nis evaluated as",reviews[244][1])
    
