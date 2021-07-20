'''
#Assuming the starting of the sequence as 0
def counting_sort(lst):
    #Extract the range of the lst values. Create an index_count array using this. 
    index_count = [0 for _ in range(max(lst))]

    #Increment the count for each value in the index array
    for _,lst_item in enumerate(lst):
        index_count[lst_item-1] += 1

    #Create a cummulative sum of the index values
    for j in range(len(index_count)-1):
        index_count[j+1] = index_count[j+1] + index_count[j]
    
    #Create an output list
    output_lst = [0 for _ in range(len(lst))]

    #Add corresponding values to the output list
    for _,lst_item in enumerate(lst):
        output_lst[index_count[lst_item-1]-1] = lst_item
        index_count[lst_item-1] -= 1
    
    return output_lst
'''

#For Negetive Numbers also
def counting_sort(lst):
    #Extract the range of the lst values. Create an index_count array using this.
    min_val = min(lst)
    max_val = max(lst)
    #Extra 1 is to incorporate 0
    range_val = max_val - min_val + 1

    index_count = [0 for _ in range(range_val)]

    #Increment the count for each value in the index array
    for _,lst_item in enumerate(lst):
        index_count[lst_item - min_val] += 1

    #Create a cummulative sum of the index values
    for j in range(len(index_count)-1):
        index_count[j+1] = index_count[j+1] + index_count[j]
    
    #Create an output list
    output_lst = [0 for _ in range(len(lst))]

    #Add corresponding values to the output list
    #for i in range(len(lst)):
    #    output_lst[index_count[lst[i]-min_val]-1] = lst[i]
    #    index_count[lst[i]-min_val] -= 1
    
    for _,lst_item in enumerate(lst):
        output_lst[index_count[lst_item-min_val]-1] = lst_item
        index_count[lst_item-min_val] -= 1

    return output_lst

a = [-11,6,4,8,6,4,2,3]
print(a)
print(counting_sort(a))