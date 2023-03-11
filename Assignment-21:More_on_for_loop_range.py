      # Assignment-21: More on for loop and range
# 1. Write a python script to print first N even natural numbers. 
n = int(input("Enter a number"))
r = range(2,n*2+1,2)
for ram in r:
    print(ram, end=' ') 

print('\n') 


# 2. Write a python script to print first N odd natural numbers. 
num1 = int(input("Enter a number"))
print("First", num1 ,"odd natural number")
for r in range(1,num1*2,2):
      print(r, end=' ')
print('\n')

# 3. Write a python script to print squares of first N natural numbers.
num2 = int(input("Enter a number"))
for ram in range(1,num2+1):
      print(ram**2, end=' ')
print('\n') 

# 4. Write a python script to print cubes of first N natural numbers.
num3 = int(input("Enter a number"))
for ram in range(1,num3+1):
      print(ram**3, end=' ')
print('\n')

# 5. Write a python script to display all prime number numbers within a range.
# range start =15 end =45
n =int(input("Enter a number"))
n1 = int(input("Enter a number"))
for ram in range(n,n1):
      for ram1 in range(2,ram):
            if ram%ram1==0:
                  break
      else:
            print(ram, end=" ")
print("\n")
