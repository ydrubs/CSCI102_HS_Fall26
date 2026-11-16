"""
Exercise 4.4 - Alien Planet Exploration Log

IMPORTANT! In order for the program to work you need to download (or create)
           a file called planets.txt whose contents are found in github.
           It needs to be placed in the same directory as this exercise.


Slides to Review (if necessary):
    Slides 27-37: Reading, writing, and processing text files

You are programming a spacecraft that explores distant planets.
The spacecraft has collected data about each planet and stored
the information in a text file named planets.txt.

Each line in the file contains:

        Planet Name, Temperature (C), Resource Level (1-10)

Your task is to analyze the data and identify planets that
are suitable for establishing a research station.

    Requirements:

    1. Open and read the data from planets.txt.

    2. Display the name and temperature of each planet.
       Separate the information using .split() as that's how it is stored in planets.txt

    3. Identify planets that meet BOTH of these conditions:
       - Temperature is between 0 and 40 degrees (inclusive).
       - Resource level is at least 5.

    4. Create a new file named exploration_report.txt.
       Write the names of all suitable planets to this file.

Example console output:

    Kepler-186f 22 C
    Proxima-b -15 C
    Gliese-667C 35 C
    TRAPPIST-1e 18 C
    Nova-Prime 42 C
    Zorgon-5 -48 C
    Pandora 27 C

Example exploration_report.txt:

    Kepler-186f
    TRAPPIST-1e
    Pandora

Note: Remember that data read from a text file is stored
as strings. Convert values to numbers when necessary.
"""

# --- YOUR SOLUTION HERE
