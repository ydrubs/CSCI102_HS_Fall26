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




##Slide 10: Logical Operators
# a = True
# b = False
#
#
# print(a or(a and b)) # ANSWER:
# print(b and (a or b)) # ANSWER:
# print(not b or (a and b)) # ANSWER:
# print(a and not b or b and not a) # ANSWER:


# --- Write your own challenging logic statement, make it as long as you want



##slide 11 - Evaluating Logic statements
# grade = int(input("What is your grade: "))
# if pass:
#     print('Nice Job')
# elif pass:
#     print('Not bad')
# elif pass:
#     print('There is room for improvement')
# else:
#     print("Better luck next time")



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



##Slide 15 - using a for loop
"""
A for loop is used to run a block of code a defined number of times (called a definite loop)
"""
pass


## using a conditional in a for loop
pass




##Slide 17 - Looping through an algorithm





##Slide 18 - Another example





##Slide 19 - Using the loop counter in the loop
"""
The loop counter is a variable that lets Python keep track of how many times the loop has run.

Anytime there is a need to use that information in our code block, the loop counter variable can be called.
"""
pass



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
pass



##Slide21 - Controlling the loop range
"""
The SECOND ARGUMENT in the loop range tells what number the loop counter should START counting on
"""
pass



##SLide 22 - - Controlling the loop range; counting by...
"""
The THIRD ARGUMENT inside of the range command tells the loop counter how much to count by
"""
# Count by threes
pass

# Count backwards from 100
pass



##Slide 23 - Augmented Assignment
"""
To add to a variable we can do the following for example:
        x = x + 2

However, it is much more conventional to use augmented assignment to do the same thing:
        x +=2
"""
a = 5
b = 5
# print(a, b)

pass


pass

pass



##Slide 26 - The while Loop
"""
A while loop (called an entry-controlled loop) runs until a condition is met
Before the loop starts it checks whether the conidtion to start the loop is true. 
    ...If it is the code in the loop body runs
"""

""" Ask for a number and add until you hit 1000 """
pass



#slide 28 ACTIVITY
pass



##Slide 29 - While Loop for entering data
theSum = 0.0
# data = input('Enter a number or just enter to quit: ')
pass



##Slide 30 - Breaking a loop
theSum = 0.0

while True:
    # data = input("Enter a number or just enter to quit: ")
    pass


##Slide 32 - While loop to validate data
pass


##Slide 33 - The While and the Boolean flag





#Slide 34 - Common While loop errors

################  Fail to break loop
while True:
    number = int(input('Enter the numeric grade: '))
    if number >= 0 and number <= 100:
        print(number)
        # NEED TO ADD 'break'

    else:
        print('Error: grade must be between 100 and 0')
        print(number) # Just echo the valid input

################    infinite Loop, not updating variable
a = 0
count = 0
while a < 1000:
    count += 1
    print(a, count)

###############    Did not test for a = 500 condition
a = 0

while a < 1000:
    a +=1
    if a < 500:
        print("Boom", a)
    if a > 500:
        print('Pow', a)
    ##Doesn't test a = 500
