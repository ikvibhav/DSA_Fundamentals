def binary_search(bst_list, search_item, low_idx, high_idx):

    # Done to stop the recursion, when high_idx <= low_idx
    if high_idx <= low_idx:
        if bst_list[low_idx] < search_item:
            return low_idx+1
        else:
            return low_idx

    mid_idx = (low_idx + high_idx)//2

    if search_item == bst_list[mid_idx]:
        return mid_idx+1
    elif search_item < bst_list[mid_idx]:
        return binary_search(bst_list, search_item, low_idx, mid_idx-1)
    else:
        return binary_search(bst_list, search_item, mid_idx+1, high_idx)

def binary_insertion_sort(lst):

    for i in range(1,len(lst)):
        key_val = lst[i]
        j = i - 1
        
        loc_idx = binary_search(lst, key_val, 0, j)

        #Due to this step, the complexity is still O(n^2)
        while j>=loc_idx:
            lst[j+1] = lst[j]
            j -= 1
        
        lst[j+1] = key_val


a = [5,6,7,8,1,4,2,3]
print(a)
binary_insertion_sort(a)
print(a)