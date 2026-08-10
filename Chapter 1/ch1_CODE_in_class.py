"""
Chapter 1: Python Fundamentals

In this chapter, you will learn how to create basic Python programs using variables, input, output, data types,
math operations, comments, and strings. You will also practice formatting output, converting data types,
naming variables correctly, and identifying common syntax and runtime errors.
"""

# --- Slide 2 (First Program)




# --- Slide 4 (Variables)

# 1) Python creates memory containers in physical memory

pass # Shows the memory location of the variable


#2) Variables need to be given an initial value
pass # 'Bob' is the initial value
pass # We get an error if we do not give a value to a variable



#3) Variables with the same data are given the same memory location



#4) Variables can be overwritten





# --- Slide 6 (Data types)
pass # integer (int) data type
pass # decimal (float) value

pass # Character (char)
pass # Text (String) data

pass # Boolean (Bool) data type


# We can check or verify a data type by using the 'type' command
pass # Replace with a variable whose type you want to check (Notice a character is also treated like a string




# --- Slide 7 (Dynamically typed)
# 1) By declaring 'version' as 11, Python knows it is an int




# 2) Two literals that appear similar can be of different types

pass # Both show up as 11 but one is an int literal and another is a string literal



# --- Slide 8 Input
pass

pass # Comma separated values
pass # String concatanation
pass # F-string


# --- Slide 9 ACTIVITY
"""
Write a Python program that welcomes somebody to class in two ways:

Directly outputting the string with their name

 “Hello Yuriy, welcome!”

Asking for an input, storing it to a variable, then printing the value
"""



# --- Slide 10 Recasting data types
pass # All inputs unless recast to a different type are STRINGS


# If we don't convert age to an int, it can cause unexpected results
pass


#As long as Python allows it, we can convert one data type into another:
pass


pass # Useful if we want to convert BACK into a string



# --- Slide 11 Outputting Multiple Expressions
pass

# three ways to output multiple expressions:
"""
It's important to note that string concatenation attempts to create ONE complete string and requires all elements that
are concatanated to be string.

Comma seperated elements can be off any data type and are printed as seperate elements.  
"""

#1) Using string concatenation
pass # Notice the lack of spaces
pass # Now we have spaces

pass # This gives an error because the age variable is an int, not a string
pass # By recasting the variable to a string, we can use string concatenation



#2) Comma Separated Values

pass # Comma separated elements are not limited to strings data types.


#3) F-Strings are often the preferred way to build strings as they can be easiest to work with


# --- Slide 12 Performing Math Operations
pass



# Addition and subtraction
pass # Results in an int
pass # Results in a float


# Traditional Division - Always results in a float



# Quotient Division (Always rounds DOWN - drops the decimal in the result)




# Modulus (Mod) Operation displays the reminder when the first number is divided by the second.
pass # Answer:
pass # Answer:
pass # Answer:


# Exponents



# Rounding Decimals

pass # No rounding
pass # Round to one decimal place
pass # Round to two decimal places (and we can keep going)



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
pass # The new line character is the most common escape character

# Try Each of the following below to see how the escape characters work
# print("1. hello " + 'there') #Substitute one of the escape chars for the '#'
# print("2. hello\b " + ' there') # backspace
# print("3. hello\n " + ' there') # Newlinw
# print("4. hello\t " + ' there') # Tab
# print("5. hello\\ " + ' there') # Single forward slash (\) character
# print("6. hello\' " + ' there') # Single quotation (') character
# print("7.hello\" " + ' there') # Double quotation (") character



# --- Slide 17 End of Line and Seperator Arguments
color1 = 'red'
color2 = 'green'
color3 = 'blue'

# By default, there is a newline character at the end of every print statement
# print(color1)
# print(color2)

# We can change the newline to another character(s)
pass # Use a space instead of a new line



# We can change the seperator using the sep parameter
pass # Puts a space by default
pass # Place two stars between data elements rather than a space


# --- slide 18 Variable Naming
# Example of valid names for variables
pass


# Invalid variable names
pass


# --- Slide 20 ACTIVITY variable naming
"""
Create three valid variables in three different ways and set them equal to the string ‘hello’. 
Create three INVALID variables in three different ways and set them equal to the string ‘hello’ (Running any of these will give a syntax error) 
"""


# --- Slide 21 Variable Assignment
pass # Declare and initialize a variable - it is automatically recognized as a string
pass # This overwrites my_var into a string
pass # Doubles the value of my_var and stored back into itself


# Variables can be manipulated relative to other variables
x = 25
y = 5




# --- Slide 22 String Multiplication
"""
The ‘*’ operator allows you to build a string by repeating another string a given number of times
"""

s1 = 'waaz'
s2 = 'a'
s3 = 'p'

pass


# --- Slide 23 ACTIVITY
"""
Write a print statement that outputs the string seen in slide 23 of the powerpoint
"""




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