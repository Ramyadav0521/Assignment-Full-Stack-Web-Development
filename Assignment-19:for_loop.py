              #Assignment-19: for loop
# 1. Write a python script to print each character of a string with its corresponsing Unicode.
print("Find your all string in unicode")
s = input("Enter a string") 
for ram in s:
    print(ram, ord(ram))

# 2. Write a script to print only vowels of the given string. 
s = input("Enter a string")
for ram in s:
    if ram in 'aeiou,AEIOU':
        print(ram)

# 3. Write a python script to count occurrence of spaces in a given string. 
s = input("Enter a string")
count=0
for ram in s:
    if ram==' ':
        count=count+1
print("Count Occurrence of spaces", count)

#4 . Write a python script to print unique digit of a given integer.
l =[] 
n=input("Enter a number")
for ram in n:
    l.append(ram)
l=list(set(l))
print(l)

# 5. Write a python script to count number of digit in given number. 
count=0
s = input("Enter a number")
for ram in s:
    count+=1
print("Count=",count)