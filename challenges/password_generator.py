from random import *
import string 

digits = string.digits
letters = string.ascii_letters 
p_marks = string.punctuation 

result = (digits+ letters + p_marks )
pword = "".join(choice(result) for p in range(randint(8, 16)))
print(pword)
