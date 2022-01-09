from math import factorial
n=int(input("enter number:: "))


array=[]

for i in range(n):
    row=[]
    for j in range(i+1):
       row.append(factorial(i)//(factorial(j)*factorial(i-j)))
    array.append(row)
            
for i in array:
    print(i)
           
