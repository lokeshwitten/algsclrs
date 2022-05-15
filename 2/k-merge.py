from heapq import heapify,heappop,heappush
heap=[]
merged_list=[]
#Implementing the k-way merge using min heap priority queue
def k_merge(lists):
    #Building the heap initailly with the first elements
    for i in range(0,len(lists)):
        heappush(heap,(lists[i][0],i))
        lists[i].pop(0)
    while(len(heap)!=0):
        try:
            extracted_tuple=heappop(heap)
            merged_list.append(extracted_tuple[0])
            index=extracted_tuple[1]
            #If the successor exists for the minimum extracted element
            if(len(lists[index])!=0):
                heappush(heap,(lists[index][0],index))
                lists[index].pop(0) 
        except ValueError as err:
            print('{0}'.format(err))
        except IndexError as Ierror:
            print('{0}'.format(Ierror))
            exit(1)
    
lists=[[-2,2,7,8],[0,1,3,6,9],[4,5,10]]
k_merge(lists)
print(merged_list)       


    
     
        