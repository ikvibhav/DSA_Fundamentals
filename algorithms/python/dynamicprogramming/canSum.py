# Give a target sum and an array of numbers, return a boolean indicating whether or not it is possible to generate the target sum using numbers from the array.
# You may use an element of the array as many times as needed.
# You may assume that all input numbers are nonnegative.


# Time complexity: O(n^m) (n = len(numbers), m = target)
# Reason: In the worse case the function iterates through 
# all the numbers in the array and makes n recursive calls for each number.
# The number of iterations above is m, which is the target sum.
# So the total number of recursive calls is n^m.

# Space complexity: O(m)
# Reason: The maximum depth of the recursive call stack is m.
# So, the space occupied by the call stack is in the order of m.
def can_sum(target, numbers):
    if target == 0:
        return True
    
    if target < 0:
        return False
    
    for num in numbers:
        if can_sum(target - num, numbers):
            return True
        
    return False

# Time complexity: O(n*m) (n = len(numbers), m = target)
# Reason: Due to memoization, each target sum is computed only once.
# The function makes n recursive calls for each target sum.
# The number of target sums is m.
# So the total number of recursive calls is n*m.

# Space complexity: O(m)
# Reason: The maximum depth of the recursive call stack is m.
# So, the space occupied by the call stack is in the order of m.
def can_sum_memo(target, numbers, memo={}):
    if target in memo:
        return memo[target]
    
    if target == 0:
        return True
    
    if target < 0:
        return False
    
    for num in numbers:
        if can_sum_memo(target - num, numbers, memo):
            memo[target] = True
            return True
    
    memo[target] = False
    return False


if __name__ == "__main__":
    print(can_sum_memo(7, [2, 3], {})) # True
    print(can_sum_memo(7, [5, 3, 4, 7], {})) # True
    print(can_sum_memo(7, [2, 4], {})) # False
    print(can_sum_memo(7, [2, 4], {})) # False
    print(can_sum_memo(300, [7, 14], {})) # False