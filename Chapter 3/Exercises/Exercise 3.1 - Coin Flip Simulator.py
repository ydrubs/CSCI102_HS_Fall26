"""
Exercise 3.1 - Coin Flip Simulator

Slides to Review (if nececessary):

    Slides 5-6: Random module and importing libraries
    Slide 7: Generating random numbers in a for loop
    Slide 8: Using random numbers with conditionals

Write a program that simulates flipping a coin multiple times.

1. Ask the user how many times they would like to flip the coin.
2. Create two counters to keep track of the number of heads and tails.

Use a for loop to simulate the number of coin flips entered by the user.

Each time the loop runs:
    - Generate a random number that is either 0 or 1
    - Treat 0 as heads and 1 as tails
    - Increase the appropriate counter by 1

After all flips are complete:
    - Display the total number of heads
    - Display the total number of tails
    - Display whether heads or tails occurred more often
    - If they occurred the same number of times, display that it was a tie

Example input:
    How many times would you like to flip the coin? 10

Example output:
    Heads: 6
    Tails: 4

    Heads occurred more often.

"""
# --- YOUR SOLUTION HERE