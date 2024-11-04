# Problem: Write a function `canConstruct(target, wordBank)` that accepts a target string and an array of strings.
# The function should return a boolean indicating whether or not the `target` can be constructed by concatenating elements of the `wordBank` array.
# You may reuse elements of `wordBank` as many times as needed.

# Time Complexity: O(n^m * m)
## Reason: n^m for the number of calls and m for the slicing operation
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

