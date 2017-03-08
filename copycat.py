#!/usr/bin/env python3

import sys
source=sys.argv[1]
target=sys.argv[2]
sum_of_words=0
def reader(x,y):
    global sum_of_words
    lines=open(x).read().splitlines()
    i=0 
    import urllib.request
    for z in lines:
        i=i+1
        url=z
        try:
            response=urllib.request.urlopen(url)
            data=response.read()
            text=data.decode('utf-8')
            sum_of_words+=len(text.split())
            print(str(i)+"th file has "+str(len(text.split()))+" words")
            f=open(y+str(i), "w+")
            f.write(text)
            f.close
        except IOError: 
            print("Oops! There is an error. "+str(i)+"th file skipped.")   
reader(source, target)
print("The sum of all the words in the copied files is "+str(sum_of_words))
