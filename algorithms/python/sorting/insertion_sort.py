def insertion_sort(lst):
    n = len(lst)
    for i in range(1,n):
        key_val = lst[i]
        j = i - 1
        
        # Move elements lesser in value than key_val one position ahead.
        # This done to make space for key_val
        while j>=0 and key_val<lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        
        lst[j+1] = key_val

a = [5,6,7,8,1,4,2,3]
print(a)
insertion_sort(a)
print(a)