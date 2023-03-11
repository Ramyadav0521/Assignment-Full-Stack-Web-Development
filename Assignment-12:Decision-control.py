         # Assignment-12: Decision Control

# 1. Write a python script to check whether a given number is positive or non-positive
# print("positive" if int(input("enter a number"))>0 else "non positive") # first method

n = int(input("Enter a number"))
if n>0:
    print("Positive")
else:
    print("Non positive")

# 2. write a python script to check whether a given number is divisible by 5 or not. 
n = int(input("Enter a number"))
if n%5==0:
    print(n,"is divisible by 5")
else:
    print(n,"is not divisible by 5")

# 3. Write a python script to check whether a given number is even or odd.

n = int(input("Enter a number"))

print(n,"is a even number",) if n%2==0 else print(n,"is odd number")

# 4. Write a python script to print Greater between two numbers. print number only once even if the numbers are the same.
print("Enter two number")
n,n1 =int(input()),int(input())
if n>n1:
    print(n)
else:
    print(n1)

# 5. Write a python script to print two given word in dictionary order.
a = input("Enter a first word")
b = input("Enter a second word")

if a<b:
    print(a,b, sep='\n')
else:
    print(b,a, sep='\n')