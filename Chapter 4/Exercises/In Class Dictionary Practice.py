words = {
    "hero": None,
    "creature": None,
    "weapon": None,
    "spell": None,
    "treasure": None,
    "sound": None,
    "location": None,
    "villain": None,
    "number": None
}

'''
Task: Write a loop that goes through each key in the dictionary and asks
the user to enter a word or phrase related to that key.

Use the user's input to update the corresponding value in the dictionary.

For example, if the key is "hero", the program should ask:

    Enter a hero: Sir Waffles

The dictionary should then be updated to include the value "Sie Waffles" for the Key 'Name"

Repeat this process until all dictionary values have been updated.


Note: You should not have to ask for each key separately. 
    Rather, use a single loop that automatically goes through the dictionary, 
    asks the user for input, and updates each corresponding value.

HINT: You can use an f-string in your input command
'''

## YOUR CODE HERE



story = f"""
=== THE DUNGEON OF DOOM ===

Deep beneath {words['location']}, a brave adventurer
named {words['hero']} entered a mysterious dungeon
in search of the legendary {words['treasure']}.

After descending {words['number']} flights of stairs,
our hero encountered a terrifying {words['creature']}
guarding an ancient doorway.

With a mighty shout of "{words['sound']}",
{words['hero']} drew their trusty {words['weapon']}
and prepared for battle!

Suddenly, the evil {words['villain']} appeared
from the shadows and cast a powerful spell.

Thinking quickly, our hero countered with
the forbidden magic of {words['spell']}!

The dungeon shook, the walls crumbled, and
{words['villain']} fled in terror.

Victorious, {words['hero']} claimed the
{words['treasure']} and escaped the dungeon.

Unfortunately, the treasure was cursed...
"""

print(story)