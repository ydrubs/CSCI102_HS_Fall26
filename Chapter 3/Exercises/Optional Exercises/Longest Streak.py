"""
Optional Challenge - Longest Increasing Streak

Write a program that analyzes a list of game scores to find the longest
streak in which each score is higher than the score immediately before it.

Start with the following list:

        scores = [4, 7, 9, 2, 5, 6, 8, 3]

Requirements:

        1. Use a loop to examine the scores in order.

        2. Find the longest streak of consecutive increasing scores.
           A streak continues only when the next score is greater
           than the previous score.

        3. Display how many scores are in the longest streak.

        4. Display which attempt the longest streak started on.
           (The first attempt is attempt 1.)

        5. If multiple streaks have the same maximum length,
           report the first one.


Example:

        scores = [4, 7, 9, 2, 5, 6, 8, 3]

        The increasing streaks are:

            4, 7, 9       (3 scores, starts at attempt 1)
            2, 5, 6, 8    (4 scores, starts at attempt 4)
            3            (1 score, starts at attempt 8)

Example output:

        Longest increasing streak: 4 scores
        Starting attempt: 4


Hints:

    - Compare each score with the score immediately before it.

    - Think about what should happen when a score is NOT greater
      than the previous score.

    - You may need variables to keep track of the current streak
      and the longest streak found so far.

    - Sorting the list will not work because the original
      order of the scores matters.

    - Try tracing the list on paper before writing your code.

Challenge:

    Your solution should work for any non-empty list of scores,
    not just the example provided.
"""

# YOUR CODE HERE