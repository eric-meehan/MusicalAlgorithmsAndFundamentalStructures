"""
This is the main function that will run all of the algorithms needed to generate a counterpoint exercise in the style of Fux.
It is quite simple, and will simply run until stopped.
"""

# This file will need the Counterpoint class and the graphing function
from Counterpoint import Exercise

# The graphing function will also be needed
from Graphs import Graph

def Main():
    """
    This function is a continuous loop that asks the user for a version of the instruction set, the desired species, 
    and desired mode.  It then uses this information to generate a counterpoint exercise and display it as a 
    scatterplot.
    """

    # These dictionaries help prevent bugs by checking the input of the user before sending it to the functions
    Versions = ["FirstIteration", "SecondIteration", "ThirdIteration", "FourthIteration", "FifthIteration"]
    PossibleSpecies = [1, 2, 3, 4, 5]
    Modes = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian"]

    while True:
        # Ask the user to specify a version of the code, the desired species, and the desired mode for an exercise
        # The 'while' statements help prevent bugs
        Version = input("Algorithm Version: ")
        while Version not in Versions:
            Version = input("Invalid version.  Enter a true version: ")

        Species = int(input("Species: "))
        while Species not in PossibleSpecies:
            Species = int(input("Invalid Species.  Enter a true species: "))

        Mode = input("Mode: ")
        while Mode not in Modes:
            Mode = input("Invalid Mode.  Enter a true mode: ")

        # Use that information to generate a counterpoint exercise
        EX = Exercise(Version, Species, Mode)

        # Extract the data from CP
        Counterpoint = EX.Counterpoint
        Cantus = EX.Cantus

        # Generate a graph of the results
        Graph(Version, Species, Mode, Counterpoint, Cantus)

        # These lines keep the output clean for repeated use
        print(Version + ": " + "Species " + str(Species) + " in " + Mode + " Mode Completed")
        print("\n\n")


# This calls the main function
Main()