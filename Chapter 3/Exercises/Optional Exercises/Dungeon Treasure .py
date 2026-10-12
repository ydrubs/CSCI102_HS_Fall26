"""
Optional Challenge - Dungeon Treasure Trap

A player is exploring a dungeon containing rooms with different amounts
of treasure. However, collecting treasure from two adjacent rooms
triggers an alarm!

Write a program that determines the maximum amount of treasure the
player can collect without triggering the alarm. Players can explore
any combination of rooms AS LONG AS they don't explore adjacent rooms.


    For example.... a player could collect treasure from Rooms 1, 3, and 5,
    or from Rooms 1 and 4. However, collecting from Rooms 2 and 3 would
    trigger the alarm because those rooms are adjacent.


    Start with the following list (or create your own):

        treasure = [8, 1, 1, 8]

Requirements:

    1. Each number in the list represents the amount of treasure
       in a room. The first number represents Room 1.

    2. Determine the maximum amount of treasure the player can
       collect without collecting from two adjacent rooms.

    3. Display the maximum total treasure that can be collected.

    4. Your program must work for different lists of treasure
       values, not just the example provided.


Example:

    treasure = [8, 1, 1, 8]

    Possible strategies:

        Collect from Rooms 1 and 3: 8 + 1 = 9
        Collect from Rooms 2 and 4: 1 + 8 = 9
        Collect from Rooms 1 and 4: 8 + 8 = 16

Example output:

    Maximum treasure: 16


Hints:

    - You do NOT have to collect treasure from every other room.

    - At each room, you have two choices:
        1. Collect the treasure (but you cannot collect from
           the previous room).
        2. Skip the room.

    - Think about how the best total for the current room
      might depend on the best totals from earlier rooms.

    - You may find max() useful when comparing possible totals.


Challenge:

    Find a solution that works regardless of how many rooms
    are in the dungeon.

    Do not simply compare the total of odd-numbered rooms
    with the total of even-numbered rooms.

    The goal is to develop an efficient algorithm rather
    than writing a large amount of code.
"""

# YOUR CODE HERE