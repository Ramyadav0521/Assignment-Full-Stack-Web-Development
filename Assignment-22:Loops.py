             #Assignment-22: Loops
# 1. Write a python script to calculate sum of first n natural numbers. 
n =int(input("Enter a number"))
sum = 0
for ram in range(1,n+1):
    sum =sum+ram
print("Sum is",sum)

# 2. Write a python script to calculate sum of squares of first N natural numbers. 

n =int(input("Enter a number"))
sum= 0
for i in range(2,n+1):
    sum=sum + i**2
print("Total squares sum is",sum)

# 3. Write a python script to calculate sum of cubes of first N natural numbers.

n =int(input("Enter a number"))
sum=0
for i in range(1,n+1):
      print(i**3)
      sum = i**3+sum
print(sum)

# 4. Write a python script to calculate sum of first N odd natural number.

n = int(input("Enter a number"))
sum = 0
for i in range(1,n*2+1,2):
    print(i)
    sum=i+sum
print("Sum is",sum)

# 5. Write a python script to calculate sum of first n even natural numbers. 
n = int(input("Enter a number"))
sum = 0
r = range(2,n*2+1,2)
for i in r:
    print(i)
    sum=sum+i
print("Sum of even number",sum)