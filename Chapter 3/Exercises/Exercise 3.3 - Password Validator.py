"""
Exercise 3.3 - Password Validator

Slides to Review (if necessary):

    Slide 11: String length
    Slide 14: Looping through strings
    Slides 20-21: String methods and testing characters
    Slide 24: Boolean flags

Write a program that asks the user to create a password and determines whether the password meets all the requirements.

1. Ask the user to enter a password.
2. Create Boolean flags to keep track of the password requirements.

Loop through the password one character at a time.

The password is valid if:
    - It contains at least 8 characters
    - It contains at least 1 uppercase letter
    - It contains at least 1 lowercase letter
    - It contains at least 1 number

As the loop checks each character:
    - Determine if the character is uppercase
    - Determine if the character is lowercase
    - Determine if the character is a number
    - Update the appropriate Boolean flag when a requirement is found

After checking the password:
    - Display "Valid Password" if ALL requirements are met
    - Otherwise, display "Invalid Password"
    - KEEP ASKING UNTIL the user enters something valid



Optional features (Not required):
    1) Add a fifth condition in which a special character (!,@,#,$,%,^,&,*,(, or ))
       needs to be included before a password is valid

    2) If the password is valid, ask the user to confirm the password by re-entering
        it before accepting. If the confirmed password is different then the original,
        the process starts over (asks the user for a password, does validity check,
        asks for confirmation).


Hint:

    You do not need to count how many uppercase letters, lowercase letters,
    or numbers are in the password.

    You only need to remember whether each type of character was found.

Example input:
    Enter a password: Python123

Example output:
    Valid Password

"""
# --- YOUR SOLUTION HERE