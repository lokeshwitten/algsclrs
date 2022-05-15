#Program to find if the sum of two numbers in the array is equal to 
# A given intezer x
from merge import MergeSort, merge, removeTabs
def find_sum(A,x):
    i=0
    j=len(A)-1
    while(i<j):
        if(A[i]+A[j] ==x):
            return (A[i],A[j])
        elif(A[i]+A[j]<x):
            i+=1
        else:
            j-=1
    return None
A=[-2,-4,2,7,6,3]
A=removeTabs(MergeSort(A,0,len(A)-1))
print(A)
print(find_sum(A,4))