"""
Chapter 1: Python Fundamentals

In this chapter, you will learn how to create basic Python programs using variables, input, output, data types,
math operations, comments, and strings. You will also practice formatting output, converting data types,
naming variables correctly, and identifying common syntax and runtime errors.
"""

# --- Slide 2 (First Program)
# greet = "Hello world!"
# print(greet)


# --- Slide 4 (Variables)
greet = "Hello world!"
# 1) Python creates memory containers in physical memory

# print(id(greet)) # Shows the memory location of the variable


#2) Variables need to be given an initial value
# name = 'Bob' # 'Bob' is the initial value
# name # We get an error if we do not give a value to a variable



#3) Variables with the same data are given the same memory location
# name = 'bob'
# same_name = 'bob'
#
# print(id(name))
# print(id(same_name))


#4) Variables can be overwritten
# age = 18
# print(age)
#
# age = 19
# print(age)


# --- Slide 6 (Data types)
# value = 2 # integer (int) data type
# temp = 93.5 # decimal (float) value
#
# symbol = '@' # Character (char)
# message = "Hello" # Text (String) data
#
# success = False # Boolean (Bool) data type


# We can check or verify a data type by using the 'type' command
# age = '1'
# print(type(age)) # Replace with a variable whose type you want to check (Notice a character is also treated like a string



# --- Slide 7 (Dynamically typed)
# 1) By declaring 'version' as 11, Python knows it is an int
# version = 11
# print(type(version))


# 2) Two literals that appear similar can be of different types
# diff_version = '11'
# print(version) # Both show up as 11 but one is an int literal and another is a string literal
# print(diff_version)
# print(type(version), type(diff_version))

# --- Slide 8 Input
# first_name = input("What is your first name? ")
# last_name = input("Enter your last name, please: ")
#
# print("hello", first_name, last_name) # Comma separated values
# print("wazzzuuuuup " + first_name + " " + last_name) # String concatanation
# print(f"Hello {first_name} {last_name}") # F-string


# --- Slide 9 ACTIVITY
"""
Write a Python program that welcomes somebody to class in two ways:

Directly outputting the string with their name

 “Hello Yuriy, welcome!”

Asking for an input, storing it to a variable, then printing the value
"""
# name = input("Enter your name: ")
# print(f"Hello {name}")


# --- Slide 10 Recasting data types
# age = input("Enter your age: ") # All inputs unless recast to a different type are STRINGS
# print(type(age))

# If we don't convert age to an int, it can cause unexpected results
# print('If you double your age you would be', age + age)


#As long as Python allows it, we can convert one data type into another:
# age_int = int(age)


# print(age_int + age_int) # now the answer is an integer
# print(age_int + age) # int + string is an error

# print(age_int + int(age)) # This is okay because we are converting to an int
#
# age_float = float(age)
# print(f'You are {age_float}')
#
# n = str(15) # Useful if we want to convert BACK into a string
# print(type(n))
#
# print(n[0]) # prints out 1

# --- Slide 11 Outputting Multiple Expressions
first_name = 'James'
last_name = 'Bond'
age = 40

# three ways to output multiple expressions:
"""
It's important to note that string concatenation attempts to create ONE complete string and requires all elements that
are concatanated to be string.

Comma seperated elements can be off any data type and are printed as seperate elements.  
"""

#1) Using string concatenation
# print("Call me" + last_name + first_name + last_name) # Notice the lack of spaces
# print("Call me" + " " + last_name + " " + first_name + last_name)  # Now we have spaces

# print("I am " + age + 'years old') # This gives an error because the age variable is an int, not a string
# print("I am " + str(age) + 'years old') # By recasting the variable to a string, we can use string concatenation



#2) Comma Separated Values

# print("Call me", last_name, first_name, last_name) # Comma separated elements are not limited to strings data types.
# print('I am', age, 'years old.')

#3) F-Strings are often the preferred way to build strings as they can be easiest to work with
# print(f"Call me {last_name} {first_name} {last_name} {age}")



# --- Slide 12 Performing Math Operations
a = 2
b = 4
c = 8
d = 1.2



# Addition and subtraction and multiplication
# print(a + b) # Results in an int
# print(a + b + d) # Results in a float
# print(a * d)
#

# Traditional Division - Always results in a float
# print(c/a) # Answer is 4.0 NOT 4


# Quotient Division (Always rounds DOWN - drops the decimal in the result)
# print(10//9)
# print(99//100)



# Slide 13 --- Modulus (Mod) Operation displays the reminder when the first number is divided by the second.
# print(14 % 3) # Answer: 2
# print(17%5) # Answer: 2
# print(25 % 9)# Answer: 7
#

# Exponents
# print(5**2)
# print(100**0.5)


# Rounding Decimals
r = 25/13
# print(r) # No rounding
# print(round(r, 1)) # Round to one decimal place
# print(round(r, 2)) # Round to two decimal places (and we can keep going)


# --- Slide 15 Comments
# This is a comment
count = 0 # This is also a comment

"""
This is a comment that can last several lines.
It is useful for explaining your program at a high level. 
It can also be used to attribute the author and date the program was written
"""


# --- Slide 16 Escape Characters
"""
Escape Characters are characters that perform an action to a sting rather then conveying information.
"""
# print('Hello. \nHow \nare \nyou?') # The new line character is the most common escape character

# Try Each of the following below to see how the escape characters work
# print("1. hello " + 'there') #Substitute one of the escape chars for the '#'
# print("2. hello\b " + ' there') # backspace
# print("3. hello\n " + ' there') # Newline
# print("4. hello\t\t\t " + ' there') # Tab
# print("5. hello\\ " + ' there') # Single forward slash (\) character
# print("6. hello\' " + ' there') # Single quotation (') character
# print("7.hello\" " + ' there') # Double quotation (") character
# print("hi\n"*100)
#

# --- Slide 17 and 18 End of Line and Seperator Arguments
color1 = 'red'
color2 = 'green'
color3 = 'blue'

# By default, there is a newline character at the end of every print statement
print(color1)
print(color2)

# We can change the newline to another character(s)
print(color1, end = ' ') # Use a space instead of a new line
print(color2, end = ' :) ')
print(color3)



# We can change the seperator using the sep parameter
print(color1, color2, color3) # Puts a space by default
print(color1, color2, color3, sep = ' :) ')# Place two stars between data elements rather than a space


# --- slide 19 Variable Naming
# Example of valid names for variables
count = 0
_count = 0
count100 = 0
count_to_100 = 0

# Invalid variable names
# 1count = 0
# if = 0
# count! = 0

# --- Slide 20 ACTIVITY variable naming
"""
Create three valid variables in three different ways and set them equal to the string ‘hello’. 
Create three INVALID variables in three different ways and set them equal to the string ‘hello’ (Running any of these will give a syntax error) 
"""


# --- Slide 21 Variable Assignment
my_var = "Hey there" # Declare and initialize a variable - it is automatically recognized as a string
my_var = 3.14 # This overwrites my_var into a float
my_var = my_var * 2 # Doubles the value of my_var and stored back into itself


# Variables can be manipulated relative to other variables
x = 25
y = 5

x = x + y
print(x)

y = x/y
print(y)

y = y * y
print(y)

# --- Slide 22 String Multiplication
"""
The ‘*’ operator allows you to build a string by repeating another string a given number of times
"""

s1 = 'waaz'
s2 = 'a'
s3 = 'p'

# print(s1 + s2 * 7 + s3)
# print((s1 + s2 * 7 + s3+ ' ') * 3)


# --- Slide 23 ACTIVITY
"""
Write a print statement that outputs the string seen in slide 23 of the powerpoint
"""
# up = '^'*10
# hashtag = '#'*10
# print(up, hashtag, hashtag, hashtag, up, sep='\n')

print(('^' * 10 + '\n') + (('#' * 10 + '\n')*3) + ('^' * 10 + '\n'))

# --- Slide 24 Errors (Run-Time vs. Syntax)
## Run Time Errors
# animal = "Dog"
# print(animol)

# print(5/0)

# print(int("five"))


## Syntax Errors
#  print("Hi")
# print("hi"
# print("hi')