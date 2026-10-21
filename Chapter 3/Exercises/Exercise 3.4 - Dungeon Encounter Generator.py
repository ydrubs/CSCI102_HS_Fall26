"""
Exercise 3.4 - Dungeon Encounter Generator

Slides to Review (if necessary):

    Slides 1-8: Random numbers and randint()
    Slides 27-28: Lists and list indexing
    Slides 30-31: Adding elements to lists with append() and loops
    Slide 36: The pop() method 

Write a program that randomly places enemies into the rooms of a dungeon.

Start with the following list:

    enemies = ["Slime", "Skeleton", "Goblin", "Spider", "Ghost"]

    1. Ask the user how many rooms the dungeon should have.
    2. Create an empty list called encounters.
    3. Use one for loop to fill each room with a random enemy:

       For each room:
           - Use randint() to generate a random number from 0 to the last index of the enemies list
           - Use that number to select an enemy
           - Add the selected enemy to the encounters list

       FOR EXAMPLE, after the loop finishes, the encounters list generated might look like this:

           encounters = ["Skeleton", "Slime", "Ghost", "Skeleton", "Goblin"]

    4. After all rooms have been filled, loop through the completed
       encounters list and display the enemy found in each room using the pop() method.


    Example input:

        How many rooms are in the dungeon? 5

    Example output:

        Room 1: Skeleton
        Room 2: Slime
        Room 3: Ghost
        Room 4: Skeleton
        Room 5: Goblin

Hint:

    Think about how you access an item in a list using its index.
    Instead of choosing the index yourself, generate it randomly.

    Remember that len() can help you determine the last valid
    index of a list.
"""
enemies = ["Slime", "Skeleton", "Goblin", "Spider", "Ghost"]
# YOUR CODE HERE