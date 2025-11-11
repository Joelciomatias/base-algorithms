# 🧩 Palindromic Strings Challenge

# A palindrome reads the same forwards and backwards — for example: "mom", "a", or "radar". You are given an array of n strings consisting of lowercase English letters. In one operation, you can swap any two letters from any two distinct strings in the array. Your task is to determine the maximum number of palindromic strings that can be obtained by performing any number of these operations.

# Choose 4 integers x, y, i, j such that 1 ≤ x, y ≤ n, 1 ≤ i ≤ len(arr[x]), and 1 ≤ j ≤ len(arr[y]), then swap the characters arr[x][i] and arr[y][j] (1-based indexing).

# Example

# Input:

# n = 4
# arr = ["pass", "sas", "asps", "df"]


# Process:

# Select x = 1, y = 3, i = 3, j = 1 → arr = ["peas", "sas", "ssps", "df"]

# Select x = 1, y = 3, i = 4, j = 3 → arr = ["paap", "sas", "ssss", "df"]

# Now we have 3 palindromic strings: "paap", "sas", and "ssss".

# Output:

# 3

# Function Description

# Implement the following function:

# def countPalindromes(arr: list[str]) -> int:
#     """
#     Determines the maximum number of palindromic strings that can be obtained 
#     after performing any number of letter swaps between different strings.

#     Args:
#         arr (list[str]): List of lowercase strings.

#     Returns:
#         int: Maximum number of palindromic strings possible.
#     """

# Constraints

# 1 ≤ n ≤ 1000

# 1 ≤ len(arr[i]) ≤ 1000

# All strings consist of lowercase English letters only.

# Input Format

# The first line contains an integer n, the size of the array.
# Each of the next n lines contains one string arr[i].

# Sample Case 0

# Input:

# 3
# xy
# tz
# abab


# Output:

# 2


# Explanation:
# After performing optimal swaps:

# arr = ["aa", "bb", "xtyz"]


# Both "aa" and "bb" are palindromes.

# Hint

# Think about the frequency of characters across all strings. If a character appears an even number of times, it can fully contribute to forming palindromes. At most one character with an odd frequency can appear in the center of a palindrome.


from collections import Counter

def countPalindromes(arr):
    # Contar frequência total de letras
    total = Counter()
    for s in arr:
        total.update(s)

    pairs = sum(v // 2 for v in total.values())
    singles = sum(v % 2 for v in total.values())


    res = 0

    # Ordenamos as strings pelos tamanhos (menores primeiro)
    arr.sort(key=len)

    for s in arr:
        need_pairs = len(s) // 2
        need_single = len(s) % 2  # 1 se ímpar

        # Podemos formar esse palíndromo?
        if pairs >= need_pairs:
            pairs -= need_pairs
            if need_single:
                if singles > 0:
                    singles -= 1
                elif pairs > 0:
                    # quebrar um par para criar 2 singles
                    pairs -= 1
                    singles += 1  # sobrou 1 single
                    singles -= 1  # usamos 1
                else:
                    continue  # sem singles possíveis
            res += 1

    return res




def countPalindromes1(arr: list[str]) -> int:
    """
    Determina o número máximo de palíndromos possíveis
    após realizar qualquer quantidade de trocas entre letras
    de strings diferentes.
    """

    # Conta todas as letras em todas as strings
    total_letters = Counter()
    for s in arr:
        total_letters.update(s)

    # Conta quantos pares e quantas sobras ímpares existem
    pairs = 0
    odd = 0
    for count in total_letters.values():
        pairs += count // 2
        odd += count % 2

    # Cada string precisa de (len(s) // 2) pares para formar um palíndromo
    needed_pairs = [len(s) // 2 for s in arr]

    # Ordena para priorizar as menores strings (menos pares necessários)
    needed_pairs.sort()

    # Calcula quantas strings podem ser palíndromos
    result = 0
    for need in needed_pairs:
        if pairs >= need:
            pairs -= need
            result += 1
        else:
            break

    # Se ainda houver letras ímpares, podemos formar mais palíndromos ímpares
    # (1 letra central serve para strings com tamanho ímpar)
    # mas apenas para strings que ainda não viraram palíndromos
    remaining_odd = len(arr) - result
    if odd > 0:
        # cada string ímpar pode aproveitar uma letra central ímpar
        result += min(odd, remaining_odd)

    return result

arr = ["pass", "sas", "asps", "df"]
print(countPalindromes1(arr))