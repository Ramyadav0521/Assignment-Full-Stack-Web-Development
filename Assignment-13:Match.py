
#           # Assignment-14:Match
# # 1. Write a python script to check whether a given number is a three digit number or not. 
# n = int(input("Enter a number"))
# match n:
#     case n if 1000>n>99:
#         print("Given number is a three digit number")
#     case n:
#         print("Given number is not a three digit number")



# # 2. Write a python script to check whether a given number is positive, negaitive or zero

# n = int(input("Enter a number"))

# match n:
#     case n if n>0:
#         print("Positive")
#     case n if n<0:
#         print("Negative")
#     case n if n==0:
#         print("zero")
# """
# 3 Write a python script to make a menu driven program in which user has choose one of the option 
# from four given options
# 1)Odd-Even, 2)Positive - non positive 3)simple Interest and 4) find roots od quadratic equation. 
# match and execute appropriate code on user selection.
# """
# print("menu driven program")
# print("1 Odd-Even")
# print("2 Positive - Non positive")
# print("3 Simple Interest")
# m = int(input("Enter your option"))
# match m:
#     case 1:
#         print("Find even or odd number")
#         n =int(input("Enter a number"))
#         print(n,"Even Number") if n%2==0 else print(n,"Odd number")

#     case 2:
#         print("Find positive or non positive")
#         n =int(input("Enter a number"))
#         print(n,"Positive number") if n>0 else print(n,"Non Positive number")

#     case 3:
#         print("Calculate simple Interest")
#         p =int(input("Enter pricipal volume"))
#         r =float(input("Enter Rate Volume"))
#         t =int(input("Enter time volume"))
#         s_i =(p*r*t)/100
#         print("Simple Interest is",s_i)
# """
# 4. Write a python script to take one data from user and evaluate the type of data.
# if the data is of of int type then print Monday, if the data is of float type then print Tuesday, if the data is of complex type 
# then print Wednesday, if the data is of type bool then print Thursday.
# """
# n = eval(input("Enter a number"))
# match n:
#     case n if type(n)==int:
#         print("Monday")
#     case n if type(n)==float:
#         print("Tuesday")
#     case n if type(n)==complex:
#         print("Wednesday")
#     case n if type(n)==bool:
#         print("Thursday")
#     case _:
#         print("Invaild Type")

# """
# 5 Write a python script to take a string from the user. if the string is part of "mysirg"
# then print "One" , if the string is a part of "Education" then print "Two" and if the string is a
# part of "services" then print "Three".
# """
# # n = input("Enter a string")
# # match n:
# #     case "mysirg":
# #         print("One")
# #     case "education":
# #         print("Two")
# #     case "services":
# #         print("Three")
# #     case _:
# #         print("Invaild string")

# n = input("Enter a string")
# match n:
#     case n if n in "mysirg":
#         print("One")
#     case n if n in "education":
#         print("Two")
#     case n if n in  "services":
#         print("Three")
#     case _:
#         print("Invaild string")


