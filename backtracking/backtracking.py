# def backtrack(path, options):
#     if is_solution(path):  # Base case: stop when a solution is found
#         process_solution(path)
#         return
    
#     for option in options:  # Explore all possible choices
#         if is_valid(option, path):  # Check if this choice is valid
#             path.append(option)  # Make a choice
#             backtrack(path, options)  # Recurse
#             path.pop()  # Undo the choice (backtrack)


# def permutacoes(palavra, passo=0):
#     if passo == len(palavra):
#         print("".join(palavra))  # Mostra uma combinação válida
#         return
    
#     for i in range(passo, len(palavra)):
#         # Trocar a posição atual com a posição do passo
#         palavra[passo], palavra[i] = palavra[i], palavra[passo]
        
#         # Recursivamente gerar combinações com a nova configuração
#         permutacoes(palavra, passo + 1)
        
#         # Voltar à configuração anterior (backtrack)
#         palavra[passo], palavra[i] = palavra[i], palavra[passo]

# # Chamar a função com a palavra "asdf"
# palavra = list("asdf")  # Convertendo a palavra para lista de caracteres
# permutacoes(palavra)


import itertools

# Define the items and length of permutation
items = ['a','b','c','d','e','f']
length = 2

# Generate permutations without repetition
permutations = list(itertools.permutations(items, length))

# Display the results
for perm in permutations:
    print(''.join(perm))


# digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#



# def permutations_no_repetition(items, length):
#     if length == 0:
#         return [[]]
#     result = []
#     for i, item in enumerate(items):
#         # Remove the current item and generate permutations for the rest
#         remaining_items = items[:i] + items[i+1:]
#         for perm in permutations_no_repetition(remaining_items, length - 1):
#             result.append([item] + perm)
#     return result

# # Define the items and length of permutations
# items = ['A', 'B', 'C']
# length = 2

# Generate permutations
# permutations = permutations_no_repetition(items, length)

# # Display the results
# for perm in permutations:
#     print(''.join(perm))




numbers = {
    '2':['a','b','c'],
    '3':['d','e','f']
}


https://www.geeksforgeeks.org/introduction-to-backtracking-2/

https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/