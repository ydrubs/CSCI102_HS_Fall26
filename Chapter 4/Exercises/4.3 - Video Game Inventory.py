
"""
Exercise 4.3 - Video Game Inventory

Slides to Review (if necessary):
    Slides 16-23: Dictionaries, keys, values, and dictionary methods

You are given a dictionary representing a player's inventory
in a video game. Each key is an item, and its value represents
the quantity the player has. Do the following:

    1. Print the number of Potions currently in the inventory.

    2. Your player discovers a new item! Choose something cool
       to add to the inventory along with a quantity of your choice.

    3. The player uses 2 Potions. Update the quantity of Potions
       remaining in the inventory using its current value.

    4. The player loses their Shield. Remove it from the
       inventory using the .pop() method.

    5. Use dictionary methods to:
       - Print all remaining item names using .keys()
       - Print all remaining quantities using .values()

After completing all tasks, print the updated inventory.

    Example output (assuming you added 3 Dragon Eggs):

        Current Potions: 5

        Updated Inventory:
        {'Potion': 3, 'Sword': 1, 'Arrow': 20, 'Gold': 100, 'Dragon Egg': 3}

        Item Names:
        dict_keys(['Potion', 'Sword', 'Arrow', 'Gold', 'Dragon Egg'])

        Item Quantities:
        dict_values([3, 1, 20, 100, 3])

Note: Your output may look different depending on the item
and quantity you choose to add.
"""

inventory = {
    "Potion": 5,
    "Sword": 1,
    "Shield": 2,
    "Arrow": 20,
    "Gold": 100
}

# --- YOUR SOLUTION HERE
