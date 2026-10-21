"""
Chapter 3 key skills

In this chapter, we learn how to:
    - Understand how libraries, modules, and packages extend Python programs.

    - Import modules and specific functions, including using the random module
      to create simulations and games.

    - Work with characters using their numeric values with ord() and chr().

    - Treat strings as data structures and use len() to determine their size.

    - Access and process string characters using positive and negative indexing.

    - Loop through strings using both indexes and individual characters.

    - Create substrings using slicing with start, stop, and step values.

    - Manipulate and test strings using common string methods.

    - Search strings for characters and substrings and use Boolean flags
      to track whether conditions have been met.

    - Understand the difference between mutable and immutable data.

    - Create, index, and work with lists, including nested lists.

    - Add, replace, and remove list elements using common list methods.

    - Build and filter lists using loops and conditional statements.

    - Process list data using functions such as len(), min(), max(), sum(),
      and count().

    - Sort lists and understand the difference between sort() and sorted().
"""
from shlex import join

# --- Slide 6 (Importing Libraries - Random)
"""
There are three ways to import a library or module

Let's look at all three by generating a random number between 1 and 10 using randint
"""

# 1) Import everything organized in a 'toolbox'

# import random
# n = random.randint(1,10)
# print(n)


"""
In order to use randint (or any function from the random library we have to first reference the library the function is from.
This is similar to knowing which 'toolbox' you are grabbing a specific tool (or function) from
"""

# 2) Import everything dumping out all the tools

# from random import *
# n = randint(1,10)
# print(n)

"""
Here we do NOT have to reference the toolbox because all our tools are now 'dumped out'.

What actually happens is memory references are created in your program to the functions from the module imported

This is usually not the best practice because:
    1) It makes programs slightly longer to contain extra memory (not a big issue) 
    2) Can accidently overide a function by declaring a variable with the same name as the function (bigger issue) 
"""

# 3) Import a specific tool from the toolbox

# from random import randint, choice
# n = randint(1,10)
# print(n)

"""
Here we only import one function from the 26 or so available in the random module. 

Even though we call randint to use it without the random keyword, if we did use randint as a variable, Python
separates the name of the variable and the name of the function into two completely separate memory locations. 
"""

# --- Slide 7 (Dice Rolling Simulator)
# from random import randint
#
# rolls = 10
# sides = 6
#
# for i in range(rolls):
#     result = randint(1,sides)
#     print(result)


# --- Slide 8 (Guess the number Game)
# from random import randint
#
# computer_num = randint(1,100)
# player_guess = 0
# print("Welcome to my amazing guess the number game!")
#
# while player_guess != computer_num:
#     player_guess = int(input("Guess the number between 1 and 100: "))
#
#     if player_guess == computer_num:
#         print("You got it right")
#
#     elif player_guess > computer_num:
#         print("You guess too high, silly.")
#
#     elif player_guess < computer_num:
#         print("You guesses too low, silly.")




############################################################
# In-class coin flip simulator (mote carlo simulation)

# from random import randint
#
# simulations = 1000
# sum_of_flips = 0
#
# for i in range(simulations):
#     flip_count = 0
#     head_count = 0
#     desired_heads = 3
#
#     while head_count < desired_heads:
#         flip_count +=1
#         flip_result = randint(0,1) # 0 = HEADS 1 = TAILS
#         # print(flip_result)
#
#         if flip_result == 0:
#             head_count +=1
#
#         else:
#             head_count = 0
#
#     print(f"It took {flip_count} to get {desired_heads} in a row.")
#     sum_of_flips+=flip_count
#
# print(f"It took an average of {sum_of_flips/simulations} flips across {simulations} to get three heads in a row")

############################################################


# --- Slide 9 Characters
# print('A' < 'a')
#
# print(ord('a'))
# print(chr(970))


# --- Slide 10 Characters
"""
Creating a simple Ceaser Cipher
"""
# letter = input("Enter a letter: ")
# shift = int(input("Enter a shift: "))
#
# new_ASCII = ord(letter) + shift
# new_letter = chr(new_ASCII)
# print(new_letter)



# --- Slide 11 Strings - length
message = "hello"
longer_message = "How are you doing today?"

# print(len(message)) # has 5 characters
# print(len(longer_message))  # has has 24 character
#


# --- Slide 12 Strings - Indexing
# print(message[0]) #Prints 'h'
# print(message[2]) # Prints 'l'
# print(message[5]) # ERROR



# --- Slide 13 Strings - Indexing
# print(message[-1])
# print(message[-2])



#Slide 14 Strings - Looping
# Two ways to loop
    # 1) Using the index
    # 2) Use the character itself

# for i in range(len(message)):
#     print(i, message[i])
#
# for c in message:
#     print(c)
#
# # DON'T HAVE TO KNOW IT FOR THE TEST
# for i,c in enumerate(message):
#     print(message[i], c)
#


#--- Slide 15 Your Turn
pass




# --- Slide 17 Slicing for substrings
# some_string = 'The quick brown fox jumped over the lazy dog'
#
# print(some_string[0:len(some_string)]) # The whole message
# print(some_string[:]) # SAME THING as above
#
# print(some_string[4:]) # Start at character 4 and go till end


# print(some_string[4:9]) # Start at character 4 and go till 8 ('quick')


# print(some_string[-3:]) # Third to last char until end ('dog')
#
# print(some_string[-8:-4]) # 8'th to last char until 5 to last
#
# print(some_string[::2]) # Entire string but only every other character displayed
# print(some_string[::-1]) # Entire Sting Backwards
# print("racecar"[::-1]) # backwards (kind of)
#
# print(some_string[0:3] + some_string[-4:]) # Combine slices (Prints 'The dog')


# --- Slide 18 Your turn - Move Two Letters
# thing = input("enter a word son: ")
# print(thing[2:] + thing[0:2])


# --- Slide 20 String Methods
# superhero = 'the incredible hulk'
#
# print(superhero.upper())
# print(superhero.upper)
#
# print(superhero.title())
# print(superhero.lower())



# --- Slide 21 String Methods
# address = '123 Fake St.'

# print(address.isupper())
# print(address.isdigit())



# Check which characters are digits
# for c in address:
#     print(c.isdigit())

# Check which characters are uppercase
# for c in address:
#     print(c, c.isupper())

# Check which characters are lowercase
# for c in address:
#     print(c, c.isalnum())


########## In class exercise (string methods) ############################
"""

Ask the user for an input string.

The program should:
    1) Count and display how many lower-case letters the string has
    2) print a new string that only contains the uppercase letters from the string 
        the user entered.


For example:
    If the user enters: 'The Quick Brown Fox Jumped Over the Lazy Dog'
        1) The lower-case letter count would be 28
        2) The string printed should be: 'TQBFJOLD'

                Since those are the capital letters in the first string
"""
# my_message = input("Enter your password: ")
# lower_case_count = 0
# upper_string = ''
#
#
# for c in my_message:
#     if c.islower():
#         lower_case_count +=1
#
#     elif c.isupper():
#         upper_string +=c
#
# print(f"There are {lower_case_count} lower case letters")
# print(f"The upper case string is {upper_string}")



####################################################################################


# --- Slide 22 String Methods - split
# story = "A long time ago in a galaxy far far away."
#
# words = story.split()
# print(words)
#
# print(words[1]) # long

# --- Slide 23 Testing for a Substring
# text = """A long time ago in a galaxy far far away..
# It is a period of civil war.
# Rebel spaceships, striking
# from a hidden base, have won
# their first victory against
# the evil Galactic Empire."""
#
#
# print('time' in text) # TRUE
# print('galactic' in text) # FALSE
# print('galactic' in text.casefold()) # TRUE
#
# print(text.index('Time')) # Brendon was right - this is an error



# --- Slide 24 - Boolean Flags
"""Check if a string has the letter A"""
# while True:
#     my_string = input("Please enter a string")
#
#     # Set flag
#     has_a = False
#
#     if 'A' in my_string:
#         has_a = True
#
#     # Check all your flags for True in order to not repeat the loop
#     if has_a:
#         print("Nice you have an A in your string.")
#         break
#     else:
#         print("No A you goof!")





# --- Slide 26 Mutable vs. Immutable Data
# mutable = ['G', 'O', 'O', 'D']
# print(mutable[0]) # Print 'G'

# mutable[0] = 'hello'
# print(mutable)


# immutable = 'Good'
# print(immutable[0])
# immutable[0] = 'hello' #This command is NOT fine

# immutable = 'BAD' #...But you can override the variable itself
# print(immutable)




# --- Slide 28 Declaring Lists
# my_list = [] # EMPTY LIST
# print(type(my_list))
# print(len(my_list))
#
# fruits = ['apple', 'orange', 'Kiwi'] # Three element list
#
# profile = ['jon', 30, True] # Lists can mix data types

# coordinates = [[-3,1], [0,4], [3.5, 2.6]] # Lists can contain other lists
# print(coordinates[1])
# print(coordinates[1][0]) # Returns the first element of the second list
#
#
# print(len(coordinates)) # lists have a length
# print(len(coordinates[0]))
#
#  # Lists can be indexed
# print(coordinates[-1]) # The last element
#


# --- Lists can store the result of other operation
# x = 2
#
# lst = [x, x**0.5, x+1]
# print(lst)
#



# --- Slide 29 Your turn
pass



# --- Slide 30 Adding Elements to a list
pokemon = ["Pikachu", "Eevee", "Charmander", "Squirtle"]

## 1) Using the ‘append’ method (most common)
    ## Adds the element to the end of a list
# pokemon.append('Mew')
# print(pokemon)
#
#
# ## 2) Using the .insert method
#     ## Adds the element at the index specified
# pokemon.insert(1, 'Snoralax')
# print(pokemon)


## 3) Using the .extend method
    ## Adds the elements of the first list to the second to create a combined list
# new_pokemon = ['Articuno', 'Zapdos', 'Moltres']
#
# pokemon.extend(new_pokemon)
# print(pokemon)



# --- Slide 31 Application - Adding to a list by looping
# roster_size = int(input("Enter the number of people to add: ")) #Get input about number
# roster_lst = [] #Create an empty list to hold the people
#
# for i in range(roster_size): #Loop through however many people we said we wanted to add
#     name = input("Please enter the name of the person: ") #Get the persons name
#     roster_lst.append([name]) #Add the person to the end of the roster list
#
# print(roster_lst) #print results



# --- Slide 32 Application – Filtering a list
people = ['Jack', 'Frank', 'Macy', 'Nancy', 'Bill']

second_a = []
at_least_5 = []

"""
Your task
    1) Print a new list with only the people who have ‘a’ as the second letter in their name.
    2) Print ANOTHER new list with people whose name has 5 or more characters in it
"""
# print(people[0].index('a')) # Probably inefficient here
# for i in range(len(people)):
#     test = people[i]
#     print(test)
#     if test[1] == 'a':
#         second_a.append(people[i])

# for person in people:
#     # print(person)
#     if person[1] == 'a':
#         second_a.append(person)
#
# print(second_a)

# for person in people:
#     if len(person) >= 5:
#         at_least_5.append(person)
# print(at_least_5)



# --- Slide 33 Whole list operations
# from random import randint
# lst = []
# for i in range(100):
#     lst.append(randint(1, 100))
#
# print(lst)
#
# print(max(lst))
# print(min(lst))
# print(sum(lst))




# --- Slide 36 Replacing and Removing Elements
lst= [1,2,3,4]
# lst[5] = 100 # Index Error, thanks Brenden!

lst[2] = 1000
print(lst)

n = lst.pop() # Removes the last element
print(lst)
print(n)

n2 = lst.pop(0)
print(lst)



# --- Slide 37 Manipulating List Elements With Loops
"""
Square each integer in the list and overwrite the original in that position
"""
numbers = [2,3,4,5]
pass


"""
Remove the space character and capitalize the first letter of each name
"""
names = ["  alice", "bob  ", "  charlie  "]
cleaned_names = []

pass




# --- Slide 38 Sorting
high_NFL_scores = [99, 101, 95, 113, 98, 96, 105, 101, 97, 103, 95, 106, 99, 98, 96]
"""
We can use <list>.sort() to re-order the original list in order.
By default, it sorts the list from low to high. 

This is called sort-in-place because it changes the original lsit so we cannot reference it in the original (unsorted) way anymore
"""
pass



"""
Comment out the sort method above to compare.

Notice that if we use the sorted() method, we get the orignal list with nothing sorted. 

This happens because sorted() returns a NEW list that is sorted, leaving the orignal one intact. 
In order to see it we need to save it to a variable.
"""
pass


pass


"""
To sort in reverse we can add the 'reverse' parameter to our command. This works with both methods. 
"""
pass


# --- Slide 39 Searching and Filtering
# high_NFL_scores = [99, 101, 95, 113, 98, 96, 105, 101, 97, 103, 95, 106, 99, 98, 96]
# high_NFL_scores.sort(reverse=True)

"""
Task 1:
Create a new list with only scores that are 100 or more
"""
pass


"""
Task 2:
Create a new list that has elements that show up at least twice on the original list 
"""
pass

