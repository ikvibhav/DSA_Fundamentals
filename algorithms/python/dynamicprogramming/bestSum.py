# Problem Statement: A function that takes in a target sum and an array of numbers as arguments.
# The function should return an array containing the shortest combination of numbers that add up to exactly the target sum.
# If there is a tie for the shortest combination, you may return any one of the shortest.

# TimeComplexity = O(n^m*m)
# SpaceCOmplexity = O(m^2)
def best_sum(target_sum, numbers):

    if target_sum == 0:
        return []
    
    if target_sum < 0:
        return None
    
    shortest_path = None
    
    for num in numbers:
        result_best_sum = best_sum(target_sum-num, numbers)
        if result_best_sum != None:
            combination = [num] + result_best_sum
            if shortest_path == None or len(combination) < len(shortest_path):
                shortest_path = combination
        
    return shortest_path

# TimeCompelexity = O(m^2*n)
# TimeCompelexity = O(m^2)
def best_sum_memo(target_sum, numbers, memo={}):

    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return []
    
    if target_sum < 0:
        return None
    
    shortest_path = None
    
    for num in numbers:
        result_best_sum = best_sum_memo(target_sum-num, numbers, memo)
        if result_best_sum != None:
            combination = [num] + result_best_sum
            if shortest_path == None or len(combination) < len(shortest_path):
                shortest_path = combination
    
    memo[target_sum] = shortest_path
    return shortest_path


if __name__ == "__main__":
    print(best_sum(4, [2,3,1]))