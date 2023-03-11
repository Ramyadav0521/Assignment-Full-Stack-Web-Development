             # Assignment-18: More on While loop with user input

#1. Write  a python script to print first N even natural number. 
n =int(input("Enter a number"))
i =1 
while i<=n:
    print(i*2, end=' ')
    i+=1
print('\n')

# z = int(input("Enter a number"))
# i =2
# while i<=z*2:
#     print(i, end=' ')
#     i=i+2
# print('\n')

# 2. Write a python script to print first N even natural numbers in reverse order. 
n = int(input("Enter a number"))
while n>=1:
    print(n*2, end=' ')
    n=n-1
print('\n')

# 3. Write a python script to print squares of N natural number. 
n = int(input("Enter a number"))
i = 1
while i<=n:
    print(i*i, end=" ")
    i=i+1
print('\n')

# 4. Write a python script to print cubes of first N natural numbers
c =int(input("Enter a number"))
i= 1
while i<=c:
    print(i**3,end=' ')
    i=i+1
print('\n')

# 5 . Write a python script to print first 10 multiples of N. 
n = int(input("Enter a number"))
i =1
print(n,"Table")
while i<=10:
    print(i,'X',n,'=',i*n)
    i=i+1
print('\n')