from itertools import permutations

letters = ["T","Y","C","H","E"]

result = list(permutations(letters))

for word in result:
    permuted=str(word)
    print(permuted)
    
    
