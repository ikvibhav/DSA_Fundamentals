def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

a = [5,6,7,8,1,4,2,3]
print(a)
bubble_sort(a)
print(a)