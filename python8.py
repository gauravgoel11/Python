#first programm to print
# print('Hellow world')

#variables
# name = "gaurav"
# age =22
# print(name)
# print(age)
# is_adult = True
# print(is_adult)
# name2 = input("what is your name ?")
# print("Hello "+name2)

#Type conversion
# old_age=float(input("Enter your old age : "))
# new_age=old_age + 2
# print(new_age)
# float()
# str()
# bool()

#operators
# print(5%2)
# print(5**2)
# print(2+3/5)

# logical operator
# print(2>3 or 2>1)
# print(not 2>3)

# loops
# age = int(input("Enter your age : "))
# if age>=18:
#     print("you are an adult")
# else:
#     print("you are not an adult")

# range
# for i in range(199,0,-5):
#     print(i)

# List data type(muteable)
# marks = [95,98,97,97]
# print(marks[0:3])
# for score in marks :
#     print(score)
# marks.insert(0,99)
# print(marks)
# print(99 in marks)
# print(len(marks))
# i=0
# while i<len(marks):
#     print(marks[i])
#     i=i+1
# marks.clear()
# print(marks)
# students = ["ram","sham","kishan","radha","radhika"]
# for student in students:
#     if student == "radha":
#         continue
#     print(student)

# marks[0]=55
# print(marks)

# tuple(immutable)
# marks = (95,98,96,97,97)
# print(marks.count(97))
# print(marks.index(97))
# marks[0]=22

# sets(repeatation not allowed)
# marks = {95,98,96,97,97}
# print(marks)

# dictionary
# marks={"english":95,"chemistry":98}
# print(marks["chemistry"])
# marks["physics"]=97
# print(marks)
# marks["physics"]=99
# print(marks)

# function
# 1 in-built function
# 2 module function
# 3 user-define function
# import math
# from math import *
# print(dir(math))
# print(sqrt(16))

def print_sum(first,second=4):
    print(first+second)

a=int(input("Please enter first number : "))
b=int(input("Please enter second number : "))
print_sum(a,b)
