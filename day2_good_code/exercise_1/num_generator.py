import random

def num_generator():
    mylist=list()
    
    for i in range(0,51):
        x=random.randint(1,100)
        mylist.append(x)
    
    return mylist