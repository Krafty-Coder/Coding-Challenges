def palindrome(n)	
	n=int(input("Enter number:"))
	temp=n
	rev=0
	while(n>0):
		dig=n%10
		rev=rev*10+dig
		n=n//10
	if(temp==rev):
		print("The number is a palindrome!")
	else:
		print("The number isn't a palindrome!")
    

def validate_credit_card(n):
    digits = [int(x) for x in str(n)]
    for x in range(len(digits)-2, -1, -2):
        digits[x] = sum(map(int, str(digits[x] * 2)))
    return sum(digits) % 10 == 0
    
    
def three_n_five(n):
    lst = [num for num in range(n) if num%3==0 and num%5==0]
    return sum(lst)
