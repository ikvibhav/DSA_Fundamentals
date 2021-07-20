def selection_sort(lst):
    n = len(lst)
    for i in range(n-1):
        min_i = i
        for j in range(i+1,n):
            if lst[j] < lst[min_i]:
                min_i = j
        
        lst[i], lst[min_i] = lst[min_i], lst[i]

a = [5,6,7,8,1,4,2,3]
print(a)
selection_sort(a)
print(a) 