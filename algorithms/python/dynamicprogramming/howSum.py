# Problem Statement:
#   Write a function 'howSum(targetSum, numbers)' that takes 
#   in a targetSum and an array of numbers as arguments.
#   The function should return an array containing combination 
#   of elements that add up to exactly the targetSum. 
#   If there is no combination that adds up to the targetSum, then return None.
#   If there are multiple combinations possible, you may return any single one.

# Time Complexity: O(n^m*m) (n = len(numbers), m = targetSum)
# Reason: In the worst case, each iteration will have n recursive calls.
#         The number of iterations (height of the tree) is m.
#         At each level, we are copying the array of numbers. 
#         In the worst case, the array will have m elements (Think of a case where the numbers are all ones).
#         So, the time complexity is O(n^m*m)
#
# Space Complexity: O(m)
# Reason: The space complexity is O(m) because the height of the tree is m.
def how_sum(targetSum, numbers):
    if targetSum == 0:
        return []
    
    if targetSum < 0:
        return None
    
    for num in numbers:
        remainder = targetSum - num
        if how_sum(remainder, numbers) != None:
            return [num] + how_sum(remainder, numbers)
    
    return None

# Time Complexity: O(n*m^2) (n = len(numbers), m = targetSum)
# Reason: In the worst case, each iteration will have n recursive calls.
#         The number of iterations (height of the tree) is m.
#         At each level, we are copying the array of numbers.
#         In the worst case, the array will have m elements (Think of a case where the numbers are all ones).
#         So, the time complexity is O(n*m^2)

# Space Complexity: O(m^2)
# Reason: The space complexity is O(m^2) because the height of the tree is m.
#         At each call of the function, we are storing an array of m elements.
#        The number of calls is m. So, the space complexity is O(m^2) 
def how_sum_memo(target_sum, numbers, memo={}):
    if target_sum in memo:
        return memo[target_sum]
    
    if target_sum == 0:
        return []
    
    if target_sum < 0:
        return None
    
    for num in numbers:
        remainder_result = how_sum_memo(target_sum-num, numbers, memo)
        if remainder_result != None:
            memo[target_sum] = [num] + remainder_result
            return [num] + remainder_result

    memo[target_sum] = None
    return None


if __name__ == "__main__":
    print(how_sum_memo(7, [2, 3], {})) # [2, 2, 3]
    print(how_sum_memo(7, [5, 3, 4, 7], {})) # [3, 4]
    print(how_sum_memo(7, [2, 4], {})) # None
    print(how_sum_memo(8, [2, 3, 5], {})) # [2, 2, 2, 2]
    print(how_sum_memo(300, [7, 14], {})) # None 