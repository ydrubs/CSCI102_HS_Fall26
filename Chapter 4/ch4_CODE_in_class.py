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
# import random
#
# suit_tuple = ('hearts', 'diamomds', 'spades', 'clubs')
# rank_tuple = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace')
#
# deck = []
# for suit in suit_tuple:
#     for rank in rank_tuple:
#         card = (rank, suit)  # Temporary variable to store the current card in loop
#         # print(card) # Show the card for debugging
#         deck.append(card)  # Add this card to the deck list
#
# print(deck)
# print(len(deck))
#
# random.shuffle(deck)
# print(deck)
#
# hand = []
# my_card = deck.pop()
# hand.append(my_card)
# print(hand)
#
# print(random.choice(deck))
# print(random.choices(deck, k = 5))

# --- Slide 8 Defining Functions
# def greeting():
#     print("Hi Everyone")
#
# greeting() # Call The function
# greeting()
#
# greeting  # Calling greeting without parenthesis (), does NOT run the function
# print(greeting)  # printing greeting without parenthesis, shows where the function is stored in computer memory
# print(greeting())  # Prints None because our function (greeting) does not return anything



# --- Slide 9 The return statement
def greeting():
    # return "Hi Everyone"
    print('Hi Everyone')
    return 'a'

# greeting()  # Does not display anything

# message = greeting()  # Call the function and save what it returns to a variable
# print(message)

# print(greeting())

# if greeting() == 'a':
#     print('Yay Ayden')

# ANOTHER EXAMPLE
# def add():
#     a = 2
#     b = 3
#     return a + b
#
# add() # It does something but you can't see it in the terminal
#
# print(add()) # Displays 5
# answer = add()
# print(answer)

# print(answer ** 2)





# --- Slide 10 Defining Functions with POSITIONAL PARAMETERS
# def greeting(first_name):
#     print(first_name)
#     return f'Hi {first_name} '

# my_greeting = (greeting()) # ERROR
# print(my_greeting)

# my_greeting = greeting(15)
# print(my_greeting)
# my_greeting = greeting('Yuriy')
#
# print(my_greeting)

# def another_greeting(first_name, last_name):
#
#     return f'Call me {last_name}, {first_name}, {last_name}'
#
# my_greeting = another_greeting('Bond', 'James')
# print(my_greeting)

# --- Slide 11 Defining Functions with KEYWORD PARAMETERS
# def greeting(first_name = 'Jon', last_name = 'Doe'):
#     return f'Call me {last_name}, {first_name}, {last_name}'

# my_greeting = greeting()
# print(my_greeting)
#
# my_greeting = greeting(last_name='Bond')
# print(my_greeting)

# my_greeting = greeting(last_name='Bond', first_name='James')
# print(my_greeting)
#
# my_greeting = greeting("James", 'Bond')
# print(my_greeting)

# my_greeting = greeting('James', last_name='Bond')
# print(my_greeting)
#
# my_greeting = greeting(last_name = 'Bond', 'james')
# print(my_greeting)


# def my_function():
#     n = 67
#     # return n + 3
#     print(f"The answer is {n}")
#     return n + 3
#
# answer = my_function()
# print(answer)

# --- Slide 12 Defining Functions with positional AND keyword parameters
# def add(a, b = 67, c = 69):
#     answer = a + b + c
#     return answer
#
# n = add(41, b = 1)
# print(n)

"""
IMPORTANT NOTE! 
When defining a function - 
    POSITIONAL parameters HAVE to come before KEYWORD parameters 
"""




# --- Slide 13 Your Turn
"""
Write a function called find_bigger that takes two float values as parameters 
and returns the larger of the two. 
"""
# def find_bigger(a,b):
#     if a > b:
#         return a
#
#     return b
#
# bigger = find_bigger(7.1, 17.1)
# print(bigger)




# --- Slide 14 Function Application 1
"""
Write a function called no_ints that accepts a string that may contain letters and/or numbers.
The function returns the string with the digits removed.

For example, if the string is pass123word the return value is password

Hint: Use a string method you learned in the previous chapter
"""
# def no_ints(my_string):
#     new_string = ""
#     for char in my_string:
#         if not char.isnumeric():
#             new_string += char
#
#     return new_string
#
# result = no_ints('pass123word')
# print(result)



# --- slide 15 Function Application 2
"""
Write function called factors that accepts an integer and returns a list of its factors 
(integers divisisble by that number).
"""
# def factors(n):
#     my_factors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             my_factors.append(i)
#
#     return my_factors
#
# result = factors(71)
# print(result)




# --- Slide 18 The Dictionary Data Type
cars = {} # Empty Dictionary we can add entries to
# print(type(cars))
#
cars = {'Ford': 'Fusion', 'Toyota':"Camry"}  # Example dictionary of car makes and models


# Dictionary KEYS can be any IMMUTABLE data type (int, string, float, tuple), while VALUES can be of ANY type
character = {
    "names": ["Arin", "Luna", "Thorin"],
    "races": ["Elf", "Human", "Dwarf", 'Orc'],
    "classes": ["Wizard", "Rogue", "Fighter"],
    "weapons": ["Staff", "Dagger", "Axe"]
}

# print(character['races']) # prints a list of races from dictionary
# print(character['races'][1]) # prints human

# print(character[0]) # Error because you can access dictionaries with int indexes

# print(len(character)) # Shows how many associations in the dictionary
#
# print(character.keys())
#
# print(len(character['races']))

"""
What happens if a dictionary key is a mutable type such as a list?
"""
# character = {'player #' : 1, ["Arin", "Luna", "Thorin"] : 'names'}
# print(character)


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
# my_schedule = {("Mon", "4 PM"): "Soccer Practice"}



# --- Slide 20 Dictionaries Are Unordered
cars = {'Ford': 'Fusion', 'Toyota':"Camry"}
# print(cars[0]) #This gives an Error because we can't use indexes

# print(cars['Ford']) # This is okay because we reference a key
# print(cars['ford']) # This will be an ERROR

# print(character.get('Porche'))

# --- Slide 21 Dictionary Keys Must Be Unique
# fords = {'Ford': 'Mustang', 'Ford': 'Fusion', 'Ford': 'F150'}

# print(fords)  # Only returns ('Ford': 'F150')


# BETTER
# fords = {'Fords': ["Mustang", "Fusion", "F150", "Model T"]}


# --- Slide 22 Adding and Removing Dictionary Entries
cars = {'Ford':"Fusion", 'Toyota': "Camry", 'Jeep':"Wrangler"}
# cars["Honda"] = "Accord"
# print(cars)
# print(len(cars))

# cars.pop('Toyota')
# print(cars)
#
# if cars.get('Ferrari') != None:
#     cars.pop("Ferrari")
#     print(cars)
# else:
#     print("No Ferrari")

"""
Your turn 
    1) Add Chevy Camaro to the list
    2) Remove Jeep Wrangler from the list and print a message saying that it was purchased 
       (Save the pop to a varaible). 
"""

# new_car_make = input("What make of car did you buy: ")
#
# new_car_model = cars.pop(new_car_make)
# print(f"The {new_car_make} {new_car_model} was purchased")


# --- Slide 23 Getting all keys and values in a dictionary
cars = {'Ford':"Fusion", 'Toyota': "Camry", 'Jeep':"Wrangler"}
# print(cars.keys())  # Use the .keys method to see all the .keys in a given dictionary
#
# print(cars.values())  # Use the .values method to see all the values in a given dictionary
#
# print(cars.items())  # Use the .items method to see all the key-value pairs in a dictionary as tuples

# --- Slide 24 Looping over dictionary entries
# for makes in cars.keys():
#     print(makes)


# for models in cars.values():
#     print(models)
#
# for both in cars.items():
#     print(both)
#
# for make, model in cars.items():
#     print(make, model)


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

# for value in characters.values():
#     # print(value)
#     if value[1] > 70:
#         print(value)

# for key, value in characters.items():
#     # print(key, value)
#     if value[1] > 70:
#         print(key)

# --- Slide 26 You Try 2
"""
Given lists l1, and l2 below, create a dictionary where for each entry the key is the elements in the first list 
and the values are the elements in the second list. 

For example, one of your dictionary entries would be ‘a’:1
"""

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]







# --- Slide 30 Writing Text to a file
# f = open("myfile.txt", 'w')  # Open file in write mode
#
# f.write("Alex: 95\n") # Write first record and start a new line
# f.write("Jordan: 87\n")  # Write second record and start a new line
# f.write("Taylor: 92\n")  # Write final record
#
# f.close()  # Close the file


# --- Slide 33 Writing Numbers to a file
# import random
#
# f = open('integers.txt', 'w')
#
# for count in range(500):
#     number = random.randint(1,500)
#     f.write(str(number) + '\n')
#
# f.close()
#



# --- Slide 34 Reading Text from a file
# f = open('myfile.txt', 'r')
#
#
# lines = f.readlines()  # Writes each line into a list
# print(lines)
# print(lines[0][3]) # Print the letter e
#

# for line in lines:  # Individually show each score that is read
#     print(line, end = "")



# --- Slide 36 Parsing data from a file
f = open("myfile.txt", "r")
lines = f.readlines()
f.close()

print(len(lines)) # prints 3 because there are three entries

total = 0

for line in lines:
    data = line.split(':')  # Separate name and score using the colon (:) as the seperator character
    # print(data[1])
    name = data[0]  # First item is the name
    score = int(data[1]) # Convert score to an integer

    #DEBUG INFO
    total += score   # Add score to running total
    print(name, 'scored', score)

class_avg = total/len(lines)  # Calculate class average
print(f'The class average was {class_avg}')

if class_avg > 90:
    print("Yay you all did great!")


# --- Slide 37  You try
"""
Modify the myfile.txt program created earlier program to identify the student with the highest score.

    Print the name of the student and the score 
"""
f = open("myfile.txt", "r")
lines = f.readlines()
f.close()

high_score = 0 # Keep track of high score
name_high = '' # Keep track of name for high score


for line in lines:

    data = line.split(":")  # Separate name and score using the colon (:) as the seperator character
    score = int(data[1])

    if score > high_score: # Check if the current score is higher then the previous
        high_score = score # if it is store the score
        name_high = data[0] # and the name to go with it

print(f"{name_high} had the highscore of {high_score}.") # Display result for high score

# --- Slide 38 OS Module
"""
    Place-holder for future code
"""