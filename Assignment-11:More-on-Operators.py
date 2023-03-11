           # Assignment-11:More on Operators
# 1. Write a python script to print True if the string 'my' is a member in a string entered by user. 
name = input("Enter a string")
print(name)
x='my' in name
print(x)

# 2. Write a python script to input two string from the user and display whether the two varaiables referred to the same object or not. print True or False. 
# print("Enter two string")
#s,s1=input(),input()
# s2=s is s1 
# print("this variables referred to the same object=",s2) always print false
s = 'ram'
s1 = 'ram'
s2 = s is s1
print(s2)
# 3. What will be the output of the python expression 5>10<5?
x = 5>10<5
print(x)
 
# 4. What will be the output of the python expression "Red" and "White" ?
x = "Red" and "White"
print(x)

# 5. What will be the output of the python expression True or False ?
x = True or False
print(x)