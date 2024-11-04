# Problem: Write a function `canConstruct(target, wordBank)` that accepts a target string and an array of strings.
# The function should return a boolean indicating whether or not the `target` can be constructed by concatenating elements of the `wordBank` array.
# You may reuse elements of `wordBank` as many times as needed.

# Time Complexity: O(n^m * m)
## Reason: n^m for the number of calls in the recursion tree and m for the slicing operation
## slicing operation takes m time because slicing a string of length m takes O(m) time
## During slicing operation, a new string of length m is created
# Space Complexity: O(m^2)
## Reason: Call stack has m elements and the slicing operation takes m space
def can_construct(target: str, word_bank: list[str]) -> bool:
    if target == '':
        return True

    for word in word_bank:

        if word in target and target.index(word) == 0:
            new_string = target[len(word):]
            if can_construct(new_string, word_bank):
                return True

    return False



# Time Complexity: O(n * m^2)
## Reason: n for the number of calls in the recursion tree. m^2 for the slicing operation and memoization
# Space Complexity: O(m^2)
## Reason: Call stack has m elements and the slicing operation takes m space
def can_construct_memo(target, word_bank, memo = {}):
    if target in memo:
        return memo[target]
    
    if target == '':
        memo[target] = True
        return True
    
    for word in word_bank:
        if word in target and target.index(word) == 0:
            new_string = target[len(word):]
            if can_construct_memo(new_string, word_bank, memo):
                memo[target] = True
                return True
    
    memo[target] = False
    return False