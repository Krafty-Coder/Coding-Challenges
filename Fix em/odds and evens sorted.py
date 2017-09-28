#odds and even sorted separetly

odds=[]
even=[]

list=[2,78,34,89,32,80,0,3,57,7,9,2,5,8,0,3,1]

for i in list:
    if i%2 !=0:
        odds+=[i]
    else:
        even+=[i]

odds=sorted(odds)
even=sorted(even)
print(odds+even)



      
