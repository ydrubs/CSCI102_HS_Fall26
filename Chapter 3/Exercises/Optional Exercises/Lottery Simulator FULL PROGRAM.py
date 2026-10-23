"""
A fully completed program that implements a
Monte Carlo simulator using lists

Lottery Simulator - Expected Winnings

Simulate one person buying lottery tickets thousands
of times to estimate their expected winnings.

Skills:
    - Random numbers
    - For loops and nested loops
    - Conditionals
    - Lists and .append()
    - sum(), min(), max(), len()
    - Counters and calculations
"""

from random import randint

# -----------------------------------
# PART 1 - Lottery Settings
# -----------------------------------

tickets = int(input("How many tickets will you buy? "))
ticket_price = float(input("Cost per ticket ($): "))

odds = int(input("Odds of winning (1 in how many?): "))
prize = float(input("Prize amount ($): "))

simulations = int(input("Number of simulations: "))

total_cost = tickets * ticket_price

# -----------------------------------
# PART 2 - Set Up the Simulation
# -----------------------------------

# Store results from each simulation
winnings_list = []
profit_list = []

# Counters
simulations_with_win = 0
profitable_simulations = 0
total_winning_tickets = 0

# -----------------------------------
# PART 3 - Run the Simulations
# -----------------------------------

for simulation in range(simulations):

    winnings = 0
    winning_tickets = 0

    # Simulate buying each ticket
    for ticket in range(tickets):

        # A 1 represents a winning ticket
        result = randint(1, odds)

        if result == 1:
            winnings += prize
            winning_tickets += 1

    # Calculate the net profit or loss
    profit = winnings - total_cost

    # Save the results
    winnings_list.append(winnings)
    profit_list.append(profit)

    # Track winning outcomes
    total_winning_tickets += winning_tickets

    if winning_tickets > 0:
        simulations_with_win += 1

    if profit > 0:
        profitable_simulations += 1

    # Show the outcome of the first simulation
    if simulation == 0:
        print("\n--- First Simulation ---")
        print("Winning tickets:", winning_tickets)
        print(f"Total winnings: ${winnings:.2f}")
        print(f"Net profit/loss: ${profit:.2f}")

# -----------------------------------
# PART 4 - Analyze the Results
# -----------------------------------

average_winnings = sum(winnings_list) / len(winnings_list)
average_profit = sum(profit_list) / len(profit_list)

best_result = max(profit_list)
worst_result = min(profit_list)

win_percentage = simulations_with_win / simulations * 100
profit_percentage = profitable_simulations / simulations * 100

# -----------------------------------
# PART 5 - Calculate Expected Values
# -----------------------------------

# Probability of winning a single ticket
probability = 1 / odds

# Expected total prize money
expected_winnings = tickets * probability * prize

# Expected net profit after ticket costs
expected_profit = expected_winnings - total_cost

# -----------------------------------
# PART 6 - Display the Results
# -----------------------------------

print("\n========== LOTTERY RESULTS ==========")

print("Tickets purchased per simulation:", tickets)
print(f"Cost per simulation: ${total_cost:.2f}")
print("Simulations completed:", simulations)

print("\n--- Simulation Results ---")

print(f"Average winnings: ${average_winnings:.2f}")
print(f"Average net profit/loss: ${average_profit:.2f}")

print(f"Best net result: ${best_result:.2f}")
print(f"Worst net result: ${worst_result:.2f}")

print(f"Chance of winning at least once: {win_percentage:.2f}%")
print(f"Chance of making a profit: {profit_percentage:.2f}%")

print("\n--- Mathematical Expected Values ---")

print(f"Expected winnings: ${expected_winnings:.2f}")
print(f"Expected net profit/loss: ${expected_profit:.2f}")

print("\nTotal winning tickets across all simulations:",
      total_winning_tickets)