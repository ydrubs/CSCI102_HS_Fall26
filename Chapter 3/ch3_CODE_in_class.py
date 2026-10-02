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


# --- Slide 6 (Importing Libraries - Random)
"""
There are three ways to import a library or module

Let's look at all three by generating a random number between 1 and 10 using randint
"""

# 1) Import everything organized in a 'toolbox'

pass

"""
In order to use randint (or any function from the random library we have to first reference the library the function is from.
This is similar to knowing which 'toolbox' you are grabbing a specific tool (or function) from
"""

# 2) Import everything dumping out all the tools

pass

"""
Here we do NOT have to reference the toolbox because all our tools are now 'dumped out'.

What actually happens is memory references are created in your program to the functions from the module imported

This is usually not the best practice because:
    1) It makes programs slightly longer to contain extra memory (not a big issue) 
    2) Can accidently overide a function by declaring a variable with the same name as the function (bigger issue) 
"""

# 3) Import a specific tool from the toolbox

pass

"""
Here we only import one function from the 26 or so available in the random module. 

Even though we call randint to use it without the random keyword, if we did use randint as a variable, Python
separates the name of the variable and the name of the function into two completely separate memory locations. 
"""

# --- Slide 7 (Dice Rolling Simulator)
pass




# --- Slide 8 (Guess the number Game)
pass




############################################################
# In-class coin flip simulator (mote carlo simulation)

# Exercise needed
############################################################


# --- Slide 9 Characters
pass



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

pass




# --- Slide 12 Strings - Indexing
pass


# --- Slide 13 Strings - Indexing
pass



#Slide 14 Strings - Looping
pass



pass


#--- Slide 15 Your Turn
pass




# --- Slide 17 Slicing for substrings
some_string = 'The quick brown fox jumped over the lazy dog'

pass # The whole message
pass # Start at character 4 and go till end


pass # Start at character 4 and go till 8
pass # Char 4 till end


pass # Third to last char until end
pass # 8'th to last char until 5 to last

pass # Entire string but only every other character displayed
pass # Entire Sting Backwards

pass # Combine slices (Prints 'The dog')


# --- Slide 18 Your turn - Move Two Letters
pass




# --- Slide 20 String Methods
superhero = 'the incredible hulk'

pass



# --- Slide 21 String Methods
address = '123 Fake St.'

pass

# Check which characters are digits
pass

# Check which characters are uppercase
for char in address:
    pass

# Check which characters are lowercase
for char in address:
    pass


########## In class exercise (string methods) ############################
pass
####################################################################################


# --- Slide 22 String Methods - split
story = "A long time ago in a galaxy far far away."

pass


# --- Slide 23 Testing for a Substring
text = """A long time ago in a galaxy far far away..
It is a period of civil war.
Rebel spaceships, striking
from a hidden base, have won
their first victory against
the evil Galactic Empire."""


pass



# --- Slide 24 - Boolean Flags
"""Check if a string has the letter A and a number in it"""
pass




# --- Slide 26 Mutable vs. Immutable Data
mutable = ['G', 'O', 'O', 'D']
pass

# immutable = 'Good'
# print(immutable)
pass #This command is fine

pass # ..This is not. Can't override the individuals characters
pass #...But you can override the variable itself





# --- Slide 28 Declaring Lists
pass # Three element list
pass # Lists can mix data types
pass # Lists can contain other lists
pass # Lists can be empty

pass # lists have a length
pass # Lists can be indexed
pass


pass  # Elements of sublists can be accessed from within a list

# --- Lists can store the result of other operation
pass


# --- Slide 29 Your turn
pass



# --- Slide 30 Adding Elements to a list
pokemon = ["Pikachu", "Eevee", "Charmander", "Squirtle"]

## 1) Using the ‘append’ method (most common)
    ## Adds the element to the end of a list
pass


## 2) Using the .insert method
    ## Adds the element at the index specified
pass


## 3) Using the .extend method
    ## Adds the elements of the first list to the second to create a combined list
pass



# --- Slide 31 Application - Adding to a list by looping
roster_size = int(input("Enter the number of people to add: ")) #Get input about number
roster_lst = [] #Create an empty list to hold the people

pass #Loop through however many people we said we wanted to add
pass #Get the persons name
pass #Add the person to the end of the roster list

pass #print results


# --- Slide 32 Application – Filtering a list
people = ['Jack', 'Frank', 'Macy', 'Nancy', 'Bill']

revised_people = []

pass


# --- Slide 33 Whole list operations
from random import randint
lst = []
for i in range(10):
    lst.append(randint(1, 100))

print(lst)

pass


# --- Slide 34 Skill Review – Getting Input until break
##Stopping a loop when the 'enter' key is pressed.
pass




# --- Slide 36 Replacing and Removing Elements
lst= [1,2,3,4]
pass



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

