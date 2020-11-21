##Counting the pairs in a list with k difference

l=[1,3,5,3]
k=2

def pair_count(l, k):
    result=[]
    count=0
    # If distinct pairs are required
    #l = list(set(l))
    for index,i in enumerate(l):
        if index!=len(l)-1:
            for val in l[index+1:]:
                if abs(i-val)==k:
                    result.append((i,val))
                    count=count+1
    return "We will have {0} pairs {1}".format(count, result)

print(pair_count(l, k))
