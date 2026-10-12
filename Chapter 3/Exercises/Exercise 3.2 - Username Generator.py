"""
Exercise 3.2 - Username Generator

Slides to Review (if necessary):

    Slides 11-13: String length and indexing
    Slides 14-15: Looping through strings
    Slides 16-17: Substrings and slicing


Write a program that creates a username from information entered by the user.

1. Ask the user to enter their first name.
2. Ask the user to enter their last name.
3. Ask the user to enter a four-digit number.
4. Ask the user to enter a character that is not allowed in the username.

Create a new username using:
    - The first 3 characters of the first name
    - The last 3 characters of the last name
    - The last 2 characters of the four-digit number

Next, loop through the username one character at a time.

If the forbidden character is found:
    - Replace it with a * in the final username

Otherwise:
    - Keep the original character

Hint:

    Think of the program in two parts: build first, check second.

    First, use slicing to build the username.
    Then, loop through the completed username one character at a time
    to check for the forbidden character.

Example input:
    Enter your first name: Samantha
    Enter your last name: Jefferson
    Enter a four-digit number: 1987
    Enter a forbidden character: a

Example output:
    Your username is: S*mson87
"""
# --- YOUR SOLUTION HERE
