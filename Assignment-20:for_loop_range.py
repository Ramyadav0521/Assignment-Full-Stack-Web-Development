          # Assignment-20: for Loop and range 

# 1. Write a python script to print the first 10 multiples of 5. 
for ram in range(1,11):
    print(ram,"X 5 =",ram*5)

# 2. Write a python script to print first 10 multiples of N. 
n =int(input("Enter a number"))
for ram in range(1,11):
    print(ram, "X", n,"=",ram*n)

# 3. Write a python script to print first M Multiples of N.

n = int(input("Enter a number"))
m = int(input("Enter a number"))


for ram in range(1,m+1):
    print(m, 'X', ram ,"=", m*ram)
 
# 4. Write a python script to print first 10 multples of N in reverse order.
n = int(input("Enter a number"))
for ram in range(10,0,-1):
    print(ram*n, )

# 5. Write a python script to print tables of user's choice. 
n = int(input("tables choose of any number"))
for ram in range(1,11,1):
    print(n, 'X', ram, '=', n*ram)

    
