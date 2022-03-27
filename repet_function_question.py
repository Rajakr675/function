# meraki/.........................question 1).............

# def question():

#     print("Q). Who is the founder of Facebook?")

#     print("a).Mark Zuckerberg")
#     print("b).Bill Gates")
#     print("c).Steve Jobs")
#     print("d).Larry Page")
# question()


# question...........2).Q1 . You have to print the largest value out of the given list using the max function.

# def max_numbers(n):
#     x=max(n)
#     print(x)




# numbers = [3, 5, 7, 34, 2, 89, 2, 5]
# max_numbers(numbers)

# question ..........3).Q2. You have to print the sum of the elements of the given list by using the sum function.

# def sum_all(n):
#     sum=0
#     for i in n:
#         sum=sum+i
#     print(sum)

# numbers = [1, 2, 3, 4, 5]
# sum_all(numbers)

# Q4. Using sort function sort the given list.

# def sort_list(l):
#     l.sort()
#     print(l)

# list = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
# sort_list(list)


# Q4. By using reverse function print the reverse order of the list.
# Input:-
# reverse_list = ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# Output :-

# reverse_list = ["D", "R", "A", "M", "E", "B", "A", "A", "Z"]

# def str_reverce(r):
#     r.reverse()
#     print(r)

# r= ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
# str_reverce(r)

# .........Q5. Use the min function and find the minimun value of the list.
# def min_list(l):
#     m=min(l)
#     print(m)


# t = [8, 6, 4, 8, 4, 50, 2, 7]
# min_list(t)
    

# Now we debug the code related to function.<<<<<<<<<<<<   <Debug Question>    >>>>>>>>>>>
# Question 1

# def sum():
#     print(12+13)
# sum()



# Question 2
# def welcome():
#     print("Welcome to function")
# welcome()


# Question 3


# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
# isEven()



# <<<<<<<<<<  outpt 10

# numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
# print (max(numbers_list))

# question len find

# def len_a(a):
    
#     print(len(a))
# a=[1,2,3,4,5,6]
# len_a(a)


# Try the code below and see what is happening.

# def say_hello(name):
#     print("Hello ", name)
#     print("How are you?")
# say_hello("Aatif")

# 
# Question.................................>>>>>>>>>>>>>>>>>>>>>>>debug

# This function takes two parameters, name and languageand works like this:
# If language is "hindi", then should be print something in Hindi.
# If language is "punjabi", then should be print something in Punjabi.
# If "hindi" or "punjabi", you have given any langauge other than this, it will print in English.

# def say_hello_language(name, language):
#     if language == "hindi":
#         print("Namaste ", name)
#         print("Aap kaise ho?")
#     elif language == "punjabi":
#         print("Sat sri akaal ", name)
#         print("Tuhada ki haal hai?")
#     else:
#         print("Hello ", name)
#         print("How are you?")
# say_hello_language("Rishabh", "punjabi")
# say_hello_language("Armaan", "english")
# say_hello_language("Abhishek", "french")
# say_hello_language("Kavay", "hindi")



# Question 1).   If user's age is less than 18 , print “not eligible “,
# else if user's age is greater than or equal to 18, print “you are eligible”
# Input:-
# 18
# 16
# Output :-
# “you are eligible”
# “not eligible”
 
# def vote_age (a):
#     if a >=18:
#         print("you are eligible")
#     else:
#         print("not eligibal")
# a=int(input("enter_age "))
# vote_age(a)


# Question 1).>>>>>>>>>>>>>>>>>>>>>>
# 6 ek perfect number hai 6=1+2+3.
# Expected Output :-
# 6,28,496

 
# def perfect_num(n):

#     sum=0
#     for i in range (1,n):
#         if n%i==0:
#             sum+=i
#     if sum==n:
#         print("perfect number")
#     else:
#         print("not perfect")
# n=int(input("enter"))
# perfect_num(n)


# Question>>>>>>>>>>>>>>>>>>>>>> 3.)
# Create a function which takes 3 arguments(all integers) and prints their sum and average as shown below.
# Input:-
# Enter first number :-3
# Enter second number :-4
# Enter third number:-5
# Output :-
# Sum of three numbers :-12
# Average of three numbers :-4


# def sum_ave():
#     sum=0
#     cont=0
#     for i in range (3):
#         n=int(input("enter"))
#         sum+=n
#         cont+=1
#     ave=sum//cont
#     print("Total sum ",sum)
#     print("average of total",ave)
# sum_ave()






# Question >>>>>>>>>>>>>...4..
# Define a function which takes one argument which is the limit upto 
# which the function has to print the numbers and their label(even or odd) as shown below.
# For example :-
# Input:-
# 3
# Output :-
# 0 EVEN
# 1 ODD
# 2 EVEN
# 3 ODD
# Edit on Github

# answer:--
# def even_odd(n):
#     a=0
#     for i in range (n):
#         if i%2==0:
#             a+=i
#             print(i,"even")
#         else:
#             print(i,"odd")
        

# n=int(input("enter:  "))
# even_odd(n)





# Question >>>>>>>>>>>5).
# Define a function which takes one parameter(positive integer).
#  This function returns the sum of all multiples of 3 and 5 (not neccessary common multiples) 
#  in the range 1 to the integer passed as the parameter.
# Input:-
# 10
# 3 aur 5 ke multiples => 3, 5, 6, 9, 10
# Output :-
# 33

# def multipal_num(n):
#     sum=0
#     for i in range(1,n+1):
#         if i%3==0:
#             sum+=i
#             print(i)
#         elif i%5==0:
#             sum+=i
#             print(i)
#     print("total sum:=",sum)
# n=int(input("enter:"))
# multipal_num(n)




# Question 6.).
# Define a function that checks the speed of drivers. This function will take a parameter named speed, and will satisfy the following conditions:
# 1.If speed if less than 70, print 70.
# 2.If speed is more than 70, give 1 point per 5km.(NOTE:This won't count 70).
# 3. If points are more than 12, print “License suspended”
# Input:-
# 85
# 135
# Output :-
# 3
# “License suspended”.........................?avi nahi hua ye












# Question .>>>>>>>>>>>>>7).
# Define a function which takes two arguments(strings) and 
# returns the string with largest length. If both the strings have equal length, print both the strings one below the other.
# Hint :- use len() builtin function..
# Input:-
# # Write function here
# c(“hello”,”welcome”)
# function_name(“sonu”,”monu”)
# Output :-
# welcome
# sonu
# monu

# def function_name(a,b):
#     if len(a)>len(b):
#         print(a)
#     elif len(a)<len(b):
#         print(b)
#     else:
#         print(a,b)
    
# function_name("sonu","monu")





# Question 8).
# Create a function which takes one argument (a positive integer) and 
# returns a dictionary which has numbers from 1 to the integer (passed as parameter) 
# as the keys and their respective squares as the values as shown in the examble below.
# Input :-
# 20
# Output :-
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11:
#  121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}

# answer:   

# def square_num(n):
#     a={}
#     for i in range(1,n+1):
#         a.update({i:i*i})
#     print(a)


# n=int(input("enter: "))
# square_num(n)

# 2ed type
# n=int(input("enter"))
# a={i:i*i for i in range (1,n+1) }
# print(a)



# Question 1).
# What will be the output of the code given below?


# def employee(name,salary=20000):
#     print(name,"your salary is:-",salary)
    

# employee("kartik",30000)
# employee("deepak")





# Question 2).
# What will be the output of the code given below?

# def primeorNot(num):
#     if num > 1:
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#             else:
#                 print(num,"is a prime number")
#     else:
#         print(num,"is not a prime number")
# primeorNot(406)






# Question 3
# What will be the output of the code given below?

# def greet(*names):
#     for name in names:
#         print("Hello",name)

# greet("Raja","Bhumedh","Akash","Bhalu")






# Question 4).
# What will be the output of the code given below?

# def sumofdigits(number):
#     sum = 0
#     modulus = 0
#     while number!=0 :
#         modulus = number%10
#         sum+=modulus
#         number/=10
#     return sum

# print(sumofdigits(123))









# Question 5).
# What will be the output of the code given below?

# def  meal(day,time):
#     if day=="sunday":
#         if time=="breakfast":
#             return "dosa"
#         elif time=="lunch":
#             return "dal rice"
#         elif time=="dinner":
#             return "paneer and  chapati"
#         else :
#             return "time not found"
#     elif day=="monday":
#         if time=="breakfast":
#             return "fried rice"
#         elif time=="lunch":
#             return "aloo rice"
#         elif time=="dinner":
#             return "chhole bhature"
#         else :
#             return "time not found"
#     elif day=="other":
#         if time=="breakfast":
#             return "aloo"  
#         elif time=="lunch":
#             return "rajma rice"
#         elif time=="dinner":
#             return "veg-chapati"
#         else :
#             return "time not found"
# print(meal("sunday","lunch"))
# print(meal("monday","dinner"))





# a="raja is a good boy"
# def glo():
#     a="raja is a smart boy"
#     print(a)
#     def gob():
#         a="Raja is a boy"
#         print(a)
#     gob()
# glo()
# print(a)

# def glob():
#     print(a)
# glob()