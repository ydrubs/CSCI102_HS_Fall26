"""
Chapter 2: Conditionals and Loops

In this chapter, you will learn how to make decisions in Python using conditional statements, Boolean expressions,
comparison operators, and logical operators. You will also practice using for and while loops to repeat code,
control how many times code runs, validate user input, and combine loops and conditionals to solve problems.
"""


##Slide 4 - One way selection statement
"""
Decide if a block of code will run based on a condition
"""
# name = input("Enter your name: ")
#
# if name == 'admin':
#     print("Access granted!")
#
# print()
# print("Other code")


#Slide 5 - If/else statement
"""
Gives the ability to run an alternative condition if the first one does not trigger the code block
"""
# name = input("Enter your name: ")
#
# if name == 'admin':
#     print("Access granted!")
#
# else:
#     print("Step off you!")
#
# print("Other code")

##Slide 6: Multi-way selection
"""
Checks multiple conditions to decide which block to run
"""
# grade = int(input("Enter your grade: "))
# if grade > 89:
#     print("Good job!")
#
# elif grade > 79:
#     print("Not bad")
#
# elif grade > 69:
#     print("Room to improve")
#
# else:
#     print("Better luck next time!")

# --- WHAT HAPPENS IF WE CHANGE THE FIRST ELIF TO AN IF?
## .... We will have TWO indepedent conditionals to check


## --- ANOTHER EXAMPLE
## Combining logic with a conditional

# print("What color is the traffic light?")
# trafficLight = input("(r)ed, (y)ellow, or (g)reen: ")
#
# if (trafficLight == 'r') or (trafficLight == 'red'):
#     print("Stop!")
# elif (trafficLight == 'y') or (trafficLight == 'yellow'):
#     print("Hit the Gas!!!")
# elif (trafficLight == 'g') or (trafficLight == 'green'):
#     print("Go ahead.")
# else:
#     print("Check your vision, but drive like Mario Kart!")


##Slide 7 ACTIVITY


##Slide 8 -Boolean Expressions
"""
Ability to compare TWO OR MORE things that can be quantified (given a numeric value)
"""
# x = 10
# y = 5
# z = 2
#
# print(x == y) #ANSWER: FALSE
# print(x > y) # ANSWER: TRUE
# print(x > x/z) #ANSWER: TRUE

# print(x != y) #ANSWER: TRUE
# print(x.__ne__(y)) # SAME THING AS LINE ABOVE
# print(x.__gt__(y))

l1 = 'a'
l2 = 'A'

# print(l1 > l2)



##Slide 10: Logical Operators
a = True
b = False
#
#
# print(a or(a and b)) # ANSWER: TRUE
#
# print(b and (a or b)) # ANSWER: FALSE
#
# print(not b or (a and b)) # ANSWER:
#
# print(a and not b or b and not a) # ANSWER:


# --- Write your own challenging logic statement, make it as long as you want



##slide 11 - Evaluating Logic statements
# grade = int(input("What is your grade: "))
# if grade >=90 and grade < 101:
#     print('Nice Job')
#
# elif grade < 90 and grade >= 80:
#     print('Not bad')
#
# elif grade > 80:
#     print('There is room for improvement')
#
# else:
#     print("Better luck next time")
#


## Slide 12 Activity
"""
Given the following variables:

        valid_username = "user123" 
        is_active = True

Ask the user for a username, then....

Write a multi-way conditional that does the following:

	1) If the username name matches and is_active is true, print(‘access granted’)
	2) If the username matches but is_active is false, print(‘access denied’)
	3) If the username does not match, print (‘no user found)

"""
valid_username = 'user123'
is_active = True

# user = input("Enter your username: ")

# if user == valid_username and is_active == True:
#     print('access granted')
#
# elif user == valid_username and is_active != True:
#     print('acess denied')
#
# elif user != valid_username:
#     print("No user found")

# if user == valid_username and is_active:
#     print('access granted')
#
# elif user == valid_username and not is_active:
#     print('acess denied')
#
# elif user != valid_username:
#     print("No user found")


##Slide 15 - using a for loop
"""
A for loop is used to run a block of code a defined number of times (called a definite loop)
"""
a = 4
b = 'hello'

# for number in range(a):
#     # print(number, b)
#     number = number + 1
#     print(number)



## using a conditional in a for loop
# for n in b:
#     # print(n)
#     if n != 'he':
#         print(n)


##Slide 17 - Looping through an algorithm
# number = 0
# print(number)
#
# for i in range(10):
#     number = number + 3
#     print(number)




##Slide 18 - Another example
# total = 1
# product = 2
#
# for i in range(8):
#     total = total * product
#     print(total)




##Slide 19 - Using the loop counter in the loop
"""
The loop counter is a variable that lets Python keep track of how many times the loop has run.

Anytime there is a need to use that information in our code block, the loop counter variable can be called.
"""
#COUNT to 10
# for i in range(11):
#     print(i, end=' ')



## --- Equivalent to the following but twice as long
# count = 0
# for i in range(11):
#     print(count, end='**')
#     count = count + 1


##Slide 20 - Checkpoint Activity
"""
Write a for loop that counts 20 ‘Mississippis’, such as -
1 Mississippi
2 Mississippi
...
...
20 Mississippi
"""""
#
# for i in range(20):
#     i = i + 1
#     print(i, 'Missisipi')
#


##Slide21 - Controlling the loop range
"""
The SECOND ARGUMENT in the loop range tells what number the loop counter should START counting on
"""
# for i in range(5,20):
#     print(i)
#


##SLide 22 - - Controlling the loop range; counting by...
"""
The THIRD ARGUMENT inside of the range command tells the loop counter how much to count by
"""
# Count by threes
# for i in range(0,100,5):
#     print(i)


# Count backwards from 100
# for i in range(100, -100, -1):
#     print(i)
#
# a = True
# b = False
#
# print(a and b)


##Slide 23 - Augmented Assignment
"""
To add to a variable we can do the following for example:
        x = x + 2

However, it is much more conventional to use augmented assignment to do the same thing:
        x +=2
"""
# a = 5
# b = 5
# print(a, b)
#
# a +=5
# b -=2
# print(a,b)
#
#
# c = 2
# d = 3
#
# c *=5
# d **=0.5
# print(c,d)

#################################PRACTICE###########################
total = 1
#
# for i in range(3):
#     n = int(input("Please enter an integer number: "))
#     op = input("Enter 'A' to Add to 'M' to Multiply: ")
#
#     if op == 'A':
#         total +=n
#         print(total)
#
#     elif op == 'M':
#         total *=n
#         print(total)
#
#     else: #OPTINAL
#         print("Invalid Input. You wasted one of your loops.")
#
# print(total)


######FIZZ BUZZ PRACTICE ###########################
# for i in range(1,101):
#     # print(i)
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizz Buzz')
#
#     elif i % 5 == 0:
#         print('Buzz')
#
#     elif i % 3 == 0:
#         print('Fizz')
#
#     else:
#         print(i)



##Slide 26 - The while Loop
"""
A while loop (called an entry-controlled loop) runs until a condition is met
Before the loop starts it checks whether the conidtion to start the loop is true. 
    ...If it is the code in the loop body runs
"""

""" Ask for a number and add until you hit 1000 """
# stop = 1000
# total = 0
#
# while total <= stop:
#     n = float(input("Enter a number: "))
#     print(total)
#     total +=n




##Slide 29 - While Loop for entering data
# theSum = 0.0
# data = input('Enter a number or just enter to quit: ')
#
# while data != '':
#     number = float(data)
#     theSum +=number
#     data = input('Enter a number or just enter to quit: ')
#     print(theSum)




##Slide 30 - Breaking a loop
# theSum = 0.0
#
# while True:
#     data = input("Enter a number or just enter to quit: ")
#     if data == 'stop':
#         break
#
#     print(data)


##Slide 32 - While loop to validate data



##Slide 33 - The While and the Boolean flag
# done = False
#
# while not done:
#     number = int(input("Please enter a number: "))
#     if number >=0 and number <=100:
#         print("setting done to true")
#         done = True
#
#     else:
#         print("error grade must be between 0 and 100")
#         print(number)



#Slide 34 - Common While loop errors

################  Fail to break loop
# while True:
#     number = int(input('Enter the numeric grade: '))
#     if number >= 0 and number <= 100:
#         print(number)
#         # NEED TO ADD 'break'
#         break
#
#     else:
#         print('Error: grade must be between 100 and 0')
#         print(number) # Just echo the valid input

################    infinite Loop, not updating variable
# a = 0
# count = 0
#
# while a < 1000:
#     count += 1
#     print(a, count)
#     a +=1
    # if count == 1000:
    #     break
    #
###############    Did not test for a = 500 condition
# a = 0
#
# while a < 1000:
#     a +=1
#     if a < 500:
#         print("Boom", a)
#     if a > 500:
#         print('Pow', a)
#     #Doesn't test a = 500
