"""
    - Tuples
    - Functions
    - Dictionaries
    - File Operations
    - OS Module (if time)
"""

# --- Slide 3 Tuples
cards = ()  # Empty tuple container
# print(type(cards))
#
# cards = (6,7,10, 'queen', 'king')
# cards_full = ((2,'hearts'), (3, 'spades'))
#
# print(cards_full[0])
# print(cards_full[0][1]) # first cards suit
#
# cars = ([2020, 'Chevy', 'Corvette'], [2023, 'Toyota', 'Prius'] )

# Get element info from a tuple (similar to lists and string)
# print(cars[1][2]) # Prius


# --- Demonstrates you can't modify a tuple like you can a list
# cards[0] = 'Ace'




# cards_full = list(cards_full) # If we change the cards tuple to a list we can manipulate elements
# print(cards_full)
# cards_full.append(('4', 'Diamonds'))
# print(cards_full)
#
# cards_full = tuple(cards_full)
# print(cards_full)

# cars[0][2] = 'Chevelle'  # Since the third element [2] in the first tuple is a list, it can be modified. We are not modifying the tuple itself
# print(cars)

# print(hash(cards_full))
# l = [1,2]
# print(hash(l))

# print(dir(cards_full))
# print(dir(l))

# --- Slide 4 Tuple Quick task
"""
Create a tuple named student containing:

    - Your first name (String)
    - Number of hours of sleep you got last night (Float)
    - Your current caffeine level from 0–10  (Int)
    - Your favorite food  (String) 

Then:
    - Print your entire student profile. 
    - Use an index to print your caffeine level. 
    - Use an index to print your favorite food. 
    - Try to change your hours of sleep to 10 unless it is already 10 then change it to something okay Tyler?!.,'"~ 
    - Explain: What happens? Why?
"""
pass




# --- Slide 6 Tuple Application - Building a Card deck for a game
import random

suit_tuple = ('hearts', 'diamomds', 'spades', 'clubs')
rank_tuple = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace')

deck = []
for suit in suit_tuple:
    for rank in rank_tuple:
        card = (rank, suit)  # Temporary variable to store the current card in loop
        # print(card) # Show the card for debugging
        deck.append(card)  # Add this card to the deck list

print(deck)
print(len(deck))

random.shuffle(deck)
print(deck)

hand = []
my_card = deck.pop()
hand.append(my_card)
print(hand)

print(random.choice(deck))
print(random.choices(deck, k = 5))

# --- Slide 8 Defining Functions
pass

pass # Call The function

pass  # Calling greeting without parenthesis (), does NOT run the function
pass  # printing greeting without parenthesis, shows where the function is stored in computer memory
pass  # Prints None because our function (greeting) does not return anything



# --- Slide 9 The return statement



pass  # Does not display anything

pass  # Call the function and save what it returns to a variable



# ANOTHER EXAMPLE






# --- Slide 10 Defining Functions with POSITIONAL PARAMETERS





# --- Slide 11 Defining Functions with KEYWORD PARAMETERS






# --- Slide 12 Defining Functions with positional AND keyword parameters





# ANOTHER EXAMPLE





# --- Slide 13 Your Turn
"""
Write a function called find_bigger that takes two float values as parameters and returns the larger of the two. 
"""






# --- Slide 14 Function Application 1
"""
Write a function called no_ints that accepts a string that may contain letters and/or numbers.
The function returns the string with the digits removed.

For example, if the string is pass123word the return value is password

Hint: Use a string method you learned in the previous chapter
"""








# --- slide 15 Function Application 2
"""
Wrtie a function that accepts an integer and returns a list of its factors (integers divisisble by that number).
"""






# --- Slide 18 The Dictionary Data Type
pass  # Empty Dictionary we can add entries to
pass  # Example dictionary of car makes and models


# Dictionary KEYS can be any IMMUTABLE data type (int, string, float, tuple), while VALUES can be of ANY type
character = {
    "names": ["Arin", "Luna", "Thorin"],
    "races": ["Elf", "Human", "Dwarf"],
    "classes": ["Wizard", "Rogue", "Fighter"],
    "weapons": ["Staff", "Dagger", "Axe"]
}


"""
What happens if a dictionary key is a mutable type such as a list?
"""
# character = {["Arin", "Luna", "Thorin"] : 'names'}



# ---Slide 19 Your Turn
"""
Weekly Schedule

Create a dictionary to store your weekly activities with: 

    Keys: Tuples containing (day, time) 
    Values: Strings describing the activity 
    Include at least 3 activities

For example, one entry could say: 
	("Mon", "4 PM"): "Soccer Practice"
"""




# --- Slide 20 Dictionaries Are Unordered
pass #This gives an Error because we can't use indexes

pass  # This is okay because we reference a key



# --- Slide 21 Dictionary Keys Must Be Unique
# fords = {'Ford': 'Mustang', 'Ford': 'Fusion', 'Ford': 'F150'}

# print(fords)  # Only returns ('Ford': 'F150')


# BETTER
# fords = {'Fords': ["Mustang", "Fusion", "F150"]}




# --- Slide 22 Adding and Removing Dictionary Entries
# cars = {'Ford':"Fusion", 'Toyota': "Camry", 'Jeep':"Wrangler"}
# cars["Honda"] = "Accord"
# print(cars)
#
# cars.pop("Toyota")
# print(cars)
#
# cars.pop("Ferrari")
# print(cars)

"""
Your turn 
    1) Add Chevy Camaro to the list
    2) Remove Jeep Wrangler from the list and print a message saying that it was purchased 
       (Save the pop to a varaible). 
"""

# --- Slide 23 Getting all keys and values in a dictionary
pass  # Use the .keys method to see all the .keys in a given dictionary

pass  # Use the .values method to see all the values in a given dictionary

pass  # Use the .items method to see all the key-value pairs in a dictionary as tuples

# --- Slide 24 Looping over dictionary entries
pass





# --- Slide 25 You Try 1
"""
Given the dictionary below, each key represents a character class.

Each value is a tuple containing "HP" and the character's health.

Use a for loop and conditional to print the class (key) of every character class whose HP is greater than 70.
"""
characters = {
    "warrior": ("HP", 100),
    "wizard": ("HP", 60),
    "archer": ("HP", 80),
    "rogue": ("HP", 65),
    "paladin": ("HP", 110),
    "bard": ("HP", 55),
    "ranger": ("HP", 75)
}






# --- Slide 26 You Try 2
"""
Given lists l1, and l2 below, create a dictionary where for each entry the key is the elements in the first list 
and the values are the elements in the second list. 

For example, one of your dictionary entries would be ‘a’:1
"""

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]







# --- Slide 30 Writing Text to a file
pass  # Open file in write mode

pass  # Write first record and start a new line
pass  # Write second record and start a new line
pass  # Write final record

pass  # Close the file





# --- Slide 33 Writing Numbers to a file






# --- Slide 34 Reading Text from a file



pass  # Writes each line into a list
pass




pass  # Individually show each score that is read




# --- Slide 36 Parsing data from a file
# f = open("myfile.txt", "r")
# lines = f.readlines()
# f.close()



# for line in lines:
pass
pass  # Separate name and score using the colon (:) as the seperator character
pass  # First item is the name
pass  # Convert score to an integer

    #DEBUG INFO
pass  # Add score to running total
pass

pass  # Calculate class average




# --- Slide 37  You try
"""
Modify the myfile.txt program created earlier program to identify the student with the highest score.

    Print the name of the student and the score 
"""
# f = open("myfile.txt", "r")
# lines = f.readlines()
# f.close()
#
#


# --- Slide 38 OS Module
"""
    Place-holder for future code
"""