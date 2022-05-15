#The crucial step for merge sort. Merging two
#  sorted Lists 

import math
def merge(A,B):
    i=0
    j=0
    C=[]
    r=len(A)+len(B)
    A.append('\t')
    B.append('\t')
    for k in range(0,r):
        if(A[i]=='\t'):
            C[k:r]=B[j:]
            return C
        if(B[j] =='\t'):
            C[k:r]=A[i:]
            return C
        if(A[i]<=B[j]):
            C.append(A[i])
            i+=1
        else:
            C.append(B[j])
            j=j+1

A=[2,3,8]
B=[0,1,4,9,10,23]
P=[-9,8,2,7,5,3,10,0]

def MergeSort(A,p,r):
    if p<r:
        q=math.floor((p+r)/2)
        left=MergeSort(A,p,q)
        right=MergeSort(A,q+1,r)
        return merge(left,right)
    else:
        return [A[p]]
def removeTabs(A):
    for item in A:
        if(item=='\t'):
            return A[:A.index(item)]


