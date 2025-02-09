def string_permutations(s):
    def backtrack(path, remaining, result):
        # Base case: if no characters are left, add the permutation to the result
        if not remaining:
            result.append(path)
            print(path)
            return
        
        # Explore all choices for the next character
        for i, char in enumerate(remaining):
            # Choose a character and explore further
            backtrack(path + char, remaining[:i] + remaining[i+1:], result)

    result = []
    backtrack("", s, result)
    return result

# Example usage
s = "ABC"
result = string_permutations(s)
print(result)