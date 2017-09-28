from functools import lru_cache
"""
Finding numbers in the fibonacci sequence and provided the
limit in the arguments in range

Lru Cache stores already worked upon numbers to fasten the process

"""

@lru_cache(10000)
def fibonacci(n):

    if n == 1:
    	return 1
    elif n==2:
        return 1
    elif n>2:
    	return fibonacci(n-1)+fibonacci(n-2)

for n in range(2,101):
    print(n, ":",fibonacci(n))
    
