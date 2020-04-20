"""
This class handles the generation of contrapuntal lines.
"""

# The music fundamentals previously defined will be needed by this class.
from MusicFundamentals import Fundamentals

# This class will also need to select the appropriate Cantus Firmus for an exercise, so the class defined in CantusFirmi.py 
# need to be imported
from CantusFirmi import CantusFirmus

# A random number generator will also be needed for the computer to make 'choices'
from random import randint

class Exercise():
    # This initiates the Fundamentals class
    fundamentals = Fundamentals()

    def __init__(self, Version, Species, Mode):
        # This empty variable will eventually be filled with the pitches of a contrapuntal line
        self.Counterpoint = []

        # This empty variable will eventually be filled with the pitches of a cantus firmus
        self.Cantus = []

        # Initialize the Cantus Firmi class
        CF = CantusFirmus()
        self.Cantus = CF.GetCantus(Species, Mode)

        # Depending on which version the user has selected, a contrapuntal line will be generated
        if Version == "FirstIteration":
            self.FirstIteration()
        elif Version == "SecondIteration":
            self.SecondIteration()
        elif Version == "ThirdIteration":
            self.ThirdIteration()
        elif Version == "FourthIteration":
            self.FourthIteration()
        elif Version == "FifthIteration":
            self.FifthIteration()

    def Clear(self):
        # Resets the counterpoint variable for repetitive use
        self.Counterpoint = []


    """
    Since there are many elements to Fux's instructions that lack the specificity required for software development, several
    versions of counterpoint generators have been made.  By examining what does and does not work in each iteration, one can 
    develop a final algorithm that encompasses the strongest aspects of each one.  The final result is a highly accurate and 
    precise algorithm for generating counterpoint exercises in the style of Fux.

    Each algorithm will have an accompanying function that contains the rules for checking if a given pitch satisfies the requirements
    laid out by Fux.  They will share the same name, with 'Rules' added to the end of the confirmation function.  While this could all be
    done in a single function, it will be much clearer to keep them separate.
    """
    def FuxImperfectConsonanceStrictUpperRules(self, i, NewPitch):
        print(None)
            # Checks a given pitch to see if it satisfies the rules given by Fux
            

    def FirstIteration(self):
        # The variable 'i' will be used to mark the algorithm's current location within the line
        # For each pitch in the cantus firmus, a counterpoint pitch will be chosen based on the following conditions
        for i in range(len(self.Cantus)):
            # The first interval must be a perfect consonance
            # Note that the index of the algorithm's position is zero based
            if i == 0:
                # Select the first pitch from the list of possible perfect consonant intervals at random
                NewPitch = self.Cantus[i] + self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                # Add the new pitch to the counterpoint melody
                self.Counterpoint.append(NewPitch)
            
            # Special care is needed at the cadence
            # Since the index is zero based, the index of the final pitch is the length of the cantus firmus minus one
            elif i == len(self.Cantus) - 2:
                self.Counterpoint.append(self.Cantus[i] + 9)
            elif i == len(self.Cantus) - 1:
                self.Counterpoint.append(self.Cantus[i] + 12)
            
            # For the remaining pitches, the algorithm will prioritize imperfect consonances in contrary motion, then perfect
            # consonances in contrary motion, and finally imperfect consonances in parallel motion - note that perfect consonances in 
            # parallel motion cannot be used and oblique motion arises as a byproduct of following this heirarchy.
            else:
                # Ascertain the direction of motion in the cantus (positive for ascending, negative for descending, zero for static)
                CantusDirection = self.Cantus[i] - self.Cantus[i - 1]

                # The algorithm will also need to know what the previous interval
                PreviousInterval = self.Counterpoint[i - 1] - self.Cantus[i - 1]

                # The algorithm will stop searching once a suitable pitch has been found
                PitchFound = False

                # Imperfect Consonance in Contrary Motion
                if not PitchFound:
                    for each in self.fundamentals.ImperfectConsonantIntervals:
                        PitchToCheck = self.Cantus[i] + each
                        ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                        # Confirm that the pitch is within the given mode
                        PitchInMode = False
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck:
                                if each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                else:
                                    PitchInMode = False
                        
                        if PitchInMode:
                            if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break
                
                # Perfect Consonance in Contrary Motion
                if not PitchFound:
                    for each in self.fundamentals.PerfectConsonantIntervals:
                        PitchToCheck = self.Cantus[i] + each
                        ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                        # Confirm that the pitch is within the given mode
                        PitchInMode = False
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck:
                                if each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                else:
                                    PitchInMode = False

                        if PitchInMode:
                            if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break


                # Imperfect Consonances in Parallel Motion
                if not PitchFound and PreviousInterval not in self.fundamentals.PerfectConsonantIntervals:
                    for each in self.fundamentals.ImperfectConsonantIntervals:
                        PitchToCheck = self.Cantus[i] + each
                        ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                    # Confirm that the pitch is within the given mode
                        PitchInMode = False
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck:
                                if each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                else:
                                    PitchInMode = False
                        if PitchInMode:
                            if CantusDirection < 0 and ResultingCounterpointDirection < 0:
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection > 0 and ResultingCounterpointDirection > 0:
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection == 0 and ResultingCounterpointDirection == 0:
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                if not PitchFound:
                    print("Failed to find a pitch")
                    self.Counterpoint.append(0)

        
    def SecondIteration(self):
        # The variable 'i' will be used to mark the algorithm's current location within the line
        # For each pitch in the cantus firmus, a counterpoint pitch will be chosen based on the following conditions
        for i in range(len(self.Cantus)):
            # The first interval must be a perfect consonance
            # Note that the index of the algorithm's position is zero based
            if i == 0:
                # Select the first pitch from the list of possible perfect consonant intervals at random
                NewPitch = self.Cantus[i] + self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                # Add the new pitch to the counterpoint melody
                self.Counterpoint.append(NewPitch)
            
            # Special care is needed at the cadence
            # Since the index is zero based, the index of the final pitch is the length of the cantus firmus minus one
            elif i == len(self.Cantus) - 2:
                self.Counterpoint.append(self.Cantus[i] + 9)
            elif i == len(self.Cantus) - 1:
                self.Counterpoint.append(self.Cantus[i] + 12)
            
            # For the remaining pitches, the algorithm will prioritize imperfect consonances in contrary motion, then perfect
            # consonances in contrary motion, and finally imperfect consonances in parallel motion - note that perfect consonances in 
            # parallel motion cannot be used and oblique motion arises as a byproduct of following this heirarchy.
            else:
                # Ascertain the direction of motion in the cantus (positive for ascending, negative for descending, zero for static)
                CantusDirection = self.Cantus[i] - self.Cantus[i - 1]

                # The algorithm will also need to know what the previous interval
                PreviousInterval = self.Counterpoint[i - 1] - self.Cantus[i - 1]

                # The algorithm will stop searching once a suitable pitch has been found
                PitchFound = False

                # Imperfect Consonance in Contrary Motion
                if not PitchFound:
                    TestedIntervals = []
                    while len(TestedIntervals) < len(self.fundamentals.ImperfectConsonantIntervals) and not PitchFound:
                        # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                        IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                        while IntervalToCheck in TestedIntervals:
                            IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                        TestedIntervals.append(IntervalToCheck)

                        PitchToCheck = self.Cantus[i] + IntervalToCheck
                        ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                        # Confirm that the pitch is within the given mode
                        PitchInMode = False
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck:
                                if each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                else:
                                    PitchInMode = False
                        
                        if PitchInMode:
                            if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break
                
                # Perfect Consonance in Contrary Motion
                if not PitchFound:
                    TestedIntervals = []
                    while len(TestedIntervals) < len(self.fundamentals.PerfectConsonantIntervals) and not PitchFound:
                        # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                        IntervalToCheck = self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                        while IntervalToCheck in TestedIntervals:
                            IntervalToCheck = self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                        TestedIntervals.append(IntervalToCheck)

                        PitchToCheck = self.Cantus[i] + IntervalToCheck
                        ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                        # Confirm that the pitch is within the given mode
                        PitchInMode = False
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck:
                                if each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                else:
                                    PitchInMode = False

                        if PitchInMode:
                            if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break


                # Imperfect Consonances in Parallel Motion
                if not PitchFound and PreviousInterval not in self.fundamentals.PerfectConsonantIntervals:
                    TestedIntervals = []
                    while len(TestedIntervals) < len(self.fundamentals.ImperfectConsonantIntervals) and not PitchFound:
                        # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                        IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                        while IntervalToCheck in TestedIntervals:
                            IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                        TestedIntervals.append(IntervalToCheck)

                        PitchToCheck = self.Cantus[i] + IntervalToCheck
                        ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                    # Confirm that the pitch is within the given mode
                        PitchInMode = False
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck:
                                if each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                else:
                                    PitchInMode = False
                        if PitchInMode:
                            if CantusDirection < 0 and ResultingCounterpointDirection < 0:
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection > 0 and ResultingCounterpointDirection > 0:
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                            elif CantusDirection == 0 and ResultingCounterpointDirection == 0:
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                                break

                if not PitchFound:
                    print("Failed to find a pitch")
                    self.Counterpoint.append(0)


    def ThirdIteration(self):
        # This iteration will prioritize pitches in stepwise motion, first looking for contrary and oblique motion (either perfect or
        # imperfect consonances), then parallel motion.
        for i in range(len(self.Cantus)):
            # The first interval must be a perfect consonance
            # Note that the index of the algorithm's position is zero based
            if i == 0:
                # Select the first pitch from the list of possible perfect consonant intervals at random
                NewPitch = self.Cantus[i] + self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                # Add the new pitch to the counterpoint melody
                self.Counterpoint.append(NewPitch)
            
            # Special care is needed at the cadence
            # Since the index is zero based, the index of the final pitch is the length of the cantus firmus minus one
            elif i == len(self.Cantus) - 2:
                self.Counterpoint.append(self.Cantus[i] + 9)
            elif i == len(self.Cantus) - 1:
                self.Counterpoint.append(self.Cantus[i] + 12)
            
            # For the remaining pitches, the algorithm will prioritize stepwise motion, first looking at the adjacent pitch in
            # contrary motion, then parallel motion.
            else:
                # Again, it ascertains the direction of the cantus
                CantusDirection = self.Cantus[i] - self.Cantus[i - 1]

                # This boolean allows the algorithm to stop once a suitable pitch has been found
                PitchFound = False

                if CantusDirection <= 0:
                    # If the cantus is descending, it will first check the next ascending pitch in the counterpoint
                    PitchToCheck = self.Counterpoint[i - 1] + 1
                    # Simply adding one half step to the previous counterpoint pitch may not yeild a pitch within the mode,
                    # so it will continue to add half steps until the selected pitch is within the mode.
                    # Confirm that the pitch is within the given mode
                    PitchInMode = False
                    while PitchInMode == False:
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                PitchInMode = True
                                break
                        PitchToCheck += 1

                    # Now it checks the interval of the given pitch to confirm if obeys the rules
                    IntervalToCheck = PitchToCheck - self.Cantus[i]
                    PreviousInterval = self.Counterpoint[i - 1] - self.Cantus[i - 1]

                    if IntervalToCheck in self.fundamentals.PerfectConsonantIntervals or IntervalToCheck in self.fundamentals.ImperfectConsonantIntervals:
                        self.Counterpoint.append(PitchToCheck)
                        PitchFound = True

                    # If the first guess was not suitable, it will try parallel motion
                    if not PitchFound:
                        PitchToCheck = self.Counterpoint[i - 1] - 1
                        PitchInMode = False
                        while PitchInMode == False:
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                    break
                            PitchToCheck -= 1

                        IntervalToCheck = PitchToCheck - self.Cantus[i]
                        PreviousInterval = self.Counterpoint[i - 1] - self.Cantus[i - 1]

                        # Parallel motion can only be used when moving to imperfect consonances
                        if IntervalToCheck in self.fundamentals.ImperfectConsonantIntervals:
                            self.Counterpoint.append(PitchToCheck)
                            PitchFound = True

                    # If no suitable stepwise pitch has been found, the SecondIteration algorithm will be run in order
                    # to find a suitable pitch.
                    # Ascertain the direction of motion in the cantus (positive for ascending, negative for descending, zero for static)
                    CantusDirection = self.Cantus[i] - self.Cantus[i - 1]

                    # The algorithm will also need to know what the previous interval
                    PreviousInterval = self.Counterpoint[i - 1] - self.Cantus[i - 1]

                    # # The algorithm will stop searching once a suitable pitch has been found
                    # PitchFound = False

                    # Imperfect Consonance in Contrary Motion
                    if not PitchFound:
                        TestedIntervals = []
                        while len(TestedIntervals) < len(self.fundamentals.ImperfectConsonantIntervals) and not PitchFound:
                            # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                            IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                            while IntervalToCheck in TestedIntervals:
                                IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                            TestedIntervals.append(IntervalToCheck)

                            PitchToCheck = self.Cantus[i] + IntervalToCheck
                            ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                            # Confirm that the pitch is within the given mode
                            PitchInMode = False
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck:
                                    if each[:-1] in self.fundamentals.Mode:
                                        PitchInMode = True
                                    else:
                                        PitchInMode = False
                            
                            if PitchInMode:
                                if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break
                    
                    # Perfect Consonance in Contrary Motion
                    if not PitchFound:
                        TestedIntervals = []
                        while len(TestedIntervals) < len(self.fundamentals.PerfectConsonantIntervals) and not PitchFound:
                            # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                            IntervalToCheck = self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                            while IntervalToCheck in TestedIntervals:
                                IntervalToCheck = self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                            TestedIntervals.append(IntervalToCheck)

                            PitchToCheck = self.Cantus[i] + IntervalToCheck
                            ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                            # Confirm that the pitch is within the given mode
                            PitchInMode = False
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck:
                                    if each[:-1] in self.fundamentals.Mode:
                                        PitchInMode = True
                                    else:
                                        PitchInMode = False

                            if PitchInMode:
                                if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break


                    # Imperfect Consonances in Parallel Motion
                    if not PitchFound and PreviousInterval not in self.fundamentals.PerfectConsonantIntervals:
                        TestedIntervals = []
                        while len(TestedIntervals) < len(self.fundamentals.ImperfectConsonantIntervals) and not PitchFound:
                            # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                            IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                            while IntervalToCheck in TestedIntervals:
                                IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                            TestedIntervals.append(IntervalToCheck)

                            PitchToCheck = self.Cantus[i] + IntervalToCheck
                            ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                        # Confirm that the pitch is within the given mode
                            PitchInMode = False
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck:
                                    if each[:-1] in self.fundamentals.Mode:
                                        PitchInMode = True
                                    else:
                                        PitchInMode = False
                            if PitchInMode:
                                if CantusDirection < 0 and ResultingCounterpointDirection < 0:
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection > 0 and ResultingCounterpointDirection > 0:
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection == 0 and ResultingCounterpointDirection == 0:
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break
                
                # This part of the algorithm is the same as the previous section, only for when the cantus is ascending
                if CantusDirection >= 0:
                    # If the cantus is descending, it will first check the next ascending pitch in the counterpoint
                    PitchToCheck = self.Counterpoint[i - 1] - 1
                    # Simply adding one half step to the previous counterpoint pitch may not yeild a pitch within the mode,
                    # so it will continue to add half steps until the selected pitch is within the mode.
                    PitchInMode = False
                    while PitchInMode == False:
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                PitchInMode = True
                                break
                        PitchToCheck -= 1

                    # Now it checks the interval of the given pitch to confirm if obeys the rules
                    IntervalToCheck = PitchToCheck - self.Cantus[i]
                    PreviousInterval = self.Counterpoint[i - 1] - self.Cantus[i - 1]

                    if IntervalToCheck in self.fundamentals.PerfectConsonantIntervals or IntervalToCheck in self.fundamentals.ImperfectConsonantIntervals:
                        self.Counterpoint.append(PitchToCheck)
                        PitchFound = True

                    # If the first guess was not suitable, it will try parallel motion
                    if not PitchFound:
                        PitchToCheck = self.Counterpoint[i - 1] + 1
                        PitchInMode = False
                        while PitchInMode == False:
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                    break
                            PitchToCheck += 1

                        IntervalToCheck = PitchToCheck - self.Cantus[i]
                        PreviousInterval = self.Counterpoint[i - 1] - self.Cantus[i - 1]

                        # Parallel motion can only be used when moving to imperfect consonances
                        if IntervalToCheck in self.fundamentals.ImperfectConsonantIntervals:
                            self.Counterpoint.append(PitchToCheck)
                            PitchFound = True

                    # If no suitable stepwise pitch has been found, the SecondIteration algorithm will be run in order
                    # to find a suitable pitch.
                    # Ascertain the direction of motion in the cantus (positive for ascending, negative for descending, zero for static)
                    CantusDirection = self.Cantus[i] - self.Cantus[i - 1]

                    # The algorithm will also need to know what the previous interval
                    PreviousInterval = self.Counterpoint[i - 1] - self.Cantus[i - 1]

                    # # The algorithm will stop searching once a suitable pitch has been found
                    # PitchFound = False

                    # Imperfect Consonance in Contrary Motion
                    if not PitchFound:
                        TestedIntervals = []
                        while len(TestedIntervals) < len(self.fundamentals.ImperfectConsonantIntervals) and not PitchFound:
                            # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                            IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                            while IntervalToCheck in TestedIntervals:
                                IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                            TestedIntervals.append(IntervalToCheck)

                            PitchToCheck = self.Cantus[i] + IntervalToCheck
                            ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                            # Confirm that the pitch is within the given mode
                            PitchInMode = False
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck:
                                    if each[:-1] in self.fundamentals.Mode:
                                        PitchInMode = True
                                    else:
                                        PitchInMode = False
                            
                            if PitchInMode:
                                if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break
                    
                    # Perfect Consonance in Contrary Motion
                    if not PitchFound:
                        TestedIntervals = []
                        while len(TestedIntervals) < len(self.fundamentals.PerfectConsonantIntervals) and not PitchFound:
                            # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                            IntervalToCheck = self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                            while IntervalToCheck in TestedIntervals:
                                IntervalToCheck = self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                            TestedIntervals.append(IntervalToCheck)

                            PitchToCheck = self.Cantus[i] + IntervalToCheck
                            ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                            # Confirm that the pitch is within the given mode
                            PitchInMode = False
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck:
                                    if each[:-1] in self.fundamentals.Mode:
                                        PitchInMode = True
                                    else:
                                        PitchInMode = False

                            if PitchInMode:
                                if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break


                    # Imperfect Consonances in Parallel Motion
                    if not PitchFound and PreviousInterval not in self.fundamentals.PerfectConsonantIntervals:
                        TestedIntervals = []
                        while len(TestedIntervals) < len(self.fundamentals.ImperfectConsonantIntervals) and not PitchFound:
                            # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                            IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                            while IntervalToCheck in TestedIntervals:
                                IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                            TestedIntervals.append(IntervalToCheck)

                            PitchToCheck = self.Cantus[i] + IntervalToCheck
                            ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                        # Confirm that the pitch is within the given mode
                            PitchInMode = False
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck:
                                    if each[:-1] in self.fundamentals.Mode:
                                        PitchInMode = True
                                    else:
                                        PitchInMode = False
                            if PitchInMode:
                                if CantusDirection < 0 and ResultingCounterpointDirection < 0:
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection > 0 and ResultingCounterpointDirection > 0:
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                                elif CantusDirection == 0 and ResultingCounterpointDirection == 0:
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                    break

                if not PitchFound:
                    print("Failed to find a pitch")
                    self.Counterpoint.append(0)

    
    def FourthIteration(self):
        # This iteration also prefers stepwise motion; however, it holds imperfect consonances as its second order priority
        # over contrary motion.
        # Much of the code in this iteration is the same as ThirdIteration, so repetitive comments will be removed.
        for i in range(len(self.Cantus)):
            # The first interval must be a perfect consonance
            # Note that the index of the algorithm's position is zero based
            if i == 0:
                # Select the first pitch from the list of possible perfect consonant intervals at random
                NewPitch = self.Cantus[i] + self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                # Add the new pitch to the counterpoint melody
                self.Counterpoint.append(NewPitch)
            
            # Special care is needed at the cadence
            # Since the index is zero based, the index of the final pitch is the length of the cantus firmus minus one
            elif i == len(self.Cantus) - 2:
                self.Counterpoint.append(self.Cantus[i] + 9)
            elif i == len(self.Cantus) - 1:
                self.Counterpoint.append(self.Cantus[i] + 12)
            
            # For the remaining pitches, the algorithm will prioritize stepwise motion, first looking at the adjacent pitch in
            # contrary motion, then parallel motion.
            else:
                CantusDirection = self.Cantus[i] - self.Cantus[i - 1]
                PreviousInterval = self.Counterpoint[i - 1] - self.Cantus[i - 1]
                PitchFound = False

                if CantusDirection >= 0:
                    PitchToCheck = self.Counterpoint[i - 1] + 1

                    PitchInMode = False
                    while PitchInMode == False:
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                PitchInMode = True
                                break
                        PitchToCheck += 1

                    # The algorithm will check if the pitch is a perfect consonance, imperfect consonance, or dissonance
                    if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals:
                        self.Counterpoint.append(PitchToCheck)
                        PitchFound = True
                    else:
                        # Save the first guess.  If neither contrary nor similar motion yeild an imperfect consonance the
                        # algorithm will use the first pitch if it is a perfect consonance.
                        FirstPitch = PitchToCheck
                        PitchToCheck = self.Counterpoint[i - 1] - 1

                        while PitchInMode == False:
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                    break
                            PitchToCheck -= 1

                        if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals:
                            self.Counterpoint.append(PitchToCheck)
                            PitchFound = True
                        elif FirstPitch - self.Cantus[i] in self.fundamentals.PerfectConsonantIntervals:
                            self.Counterpoint.append(FirstPitch)
                            PitchFound = True
                        else:
                            # Since neither direction yeilded a suitable pitch, the algorithm will resort to finding
                            # one as was done in previous iterations
                            if not PitchFound:
                                TestedIntervals = []
                                while len(TestedIntervals) < len(self.fundamentals.ImperfectConsonantIntervals) and not PitchFound:
                                    # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                                    IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                                    while IntervalToCheck in TestedIntervals:
                                        IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                                    TestedIntervals.append(IntervalToCheck)

                                    PitchToCheck = self.Cantus[i] + IntervalToCheck
                                    ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                                    # Confirm that the pitch is within the given mode
                                    PitchInMode = False
                                    for each in self.fundamentals.Pitches:
                                        if self.fundamentals.Pitches[each] == PitchToCheck:
                                            if each[:-1] in self.fundamentals.Mode:
                                                PitchInMode = True
                                            else:
                                                PitchInMode = False
                                    
                                    if PitchInMode:
                                        if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break
                            
                            # Perfect Consonance in Contrary Motion
                            if not PitchFound:
                                TestedIntervals = []
                                while len(TestedIntervals) < len(self.fundamentals.PerfectConsonantIntervals) and not PitchFound:
                                    # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                                    IntervalToCheck = self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                                    while IntervalToCheck in TestedIntervals:
                                        IntervalToCheck = self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                                    TestedIntervals.append(IntervalToCheck)

                                    PitchToCheck = self.Cantus[i] + IntervalToCheck
                                    ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                                    # Confirm that the pitch is within the given mode
                                    PitchInMode = False
                                    for each in self.fundamentals.Pitches:
                                        if self.fundamentals.Pitches[each] == PitchToCheck:
                                            if each[:-1] in self.fundamentals.Mode:
                                                PitchInMode = True
                                            else:
                                                PitchInMode = False

                                    if PitchInMode:
                                        if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break


                            # Imperfect Consonances in Parallel Motion
                            if not PitchFound and PreviousInterval not in self.fundamentals.PerfectConsonantIntervals:
                                TestedIntervals = []
                                while len(TestedIntervals) < len(self.fundamentals.ImperfectConsonantIntervals) and not PitchFound:
                                    # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                                    IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                                    while IntervalToCheck in TestedIntervals:
                                        IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                                    TestedIntervals.append(IntervalToCheck)

                                    PitchToCheck = self.Cantus[i] + IntervalToCheck
                                    ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                                # Confirm that the pitch is within the given mode
                                    PitchInMode = False
                                    for each in self.fundamentals.Pitches:
                                        if self.fundamentals.Pitches[each] == PitchToCheck:
                                            if each[:-1] in self.fundamentals.Mode:
                                                PitchInMode = True
                                            else:
                                                PitchInMode = False
                                    if PitchInMode:
                                        if CantusDirection < 0 and ResultingCounterpointDirection < 0:
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection > 0 and ResultingCounterpointDirection > 0:
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection == 0 and ResultingCounterpointDirection == 0:
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                    if not PitchFound:
                        print("Failed to find a pitch")
                        self.Counterpoint.append(0)

                # Same as before, now for descending lines
                else:
                    PitchToCheck = self.Counterpoint[i - 1] - 1

                    PitchInMode = False
                    while PitchInMode == False:
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                PitchInMode = True
                                break
                        PitchToCheck -= 1

                    # The algorithm will check if the pitch is a perfect consonance, imperfect consonance, or dissonance
                    if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals:
                        self.Counterpoint.append(PitchToCheck)
                        PitchFound = True
                    else:
                        # Save the first guess.  If neither contrary nor similar motion yeild an imperfect consonance the
                        # algorithm will use the first pitch if it is a perfect consonance.
                        FirstPitch = PitchToCheck
                        PitchToCheck = self.Counterpoint[i - 1] + 1

                        while PitchInMode == False:
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                    break
                            PitchToCheck += 1

                        if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals:
                            self.Counterpoint.append(PitchToCheck)
                            PitchFound = True
                        elif FirstPitch - self.Cantus[i] in self.fundamentals.PerfectConsonantIntervals:
                            self.Counterpoint.append(FirstPitch)
                            PitchFound = True
                        else:
                            # Since neither direction yeilded a suitable pitch, the algorithm will resort to finding
                            # one as was done in previous iterations
                            if not PitchFound:
                                TestedIntervals = []
                                while len(TestedIntervals) < len(self.fundamentals.ImperfectConsonantIntervals) and not PitchFound:
                                    # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                                    IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                                    while IntervalToCheck in TestedIntervals:
                                        IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                                    TestedIntervals.append(IntervalToCheck)

                                    PitchToCheck = self.Cantus[i] + IntervalToCheck
                                    ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                                    # Confirm that the pitch is within the given mode
                                    PitchInMode = False
                                    for each in self.fundamentals.Pitches:
                                        if self.fundamentals.Pitches[each] == PitchToCheck:
                                            if each[:-1] in self.fundamentals.Mode:
                                                PitchInMode = True
                                            else:
                                                PitchInMode = False
                                    
                                    if PitchInMode:
                                        if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break
                            
                            # Perfect Consonance in Contrary Motion
                            if not PitchFound:
                                TestedIntervals = []
                                while len(TestedIntervals) < len(self.fundamentals.PerfectConsonantIntervals) and not PitchFound:
                                    # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                                    IntervalToCheck = self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                                    while IntervalToCheck in TestedIntervals:
                                        IntervalToCheck = self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                                    TestedIntervals.append(IntervalToCheck)

                                    PitchToCheck = self.Cantus[i] + IntervalToCheck
                                    ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                                    # Confirm that the pitch is within the given mode
                                    PitchInMode = False
                                    for each in self.fundamentals.Pitches:
                                        if self.fundamentals.Pitches[each] == PitchToCheck:
                                            if each[:-1] in self.fundamentals.Mode:
                                                PitchInMode = True
                                            else:
                                                PitchInMode = False

                                    if PitchInMode:
                                        if CantusDirection < 0 and (ResultingCounterpointDirection > 0 or ResultingCounterpointDirection == 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection > 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection == 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection == 0 and (ResultingCounterpointDirection < 0 or ResultingCounterpointDirection > 0):
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break


                            # Imperfect Consonances in Parallel Motion
                            if not PitchFound and PreviousInterval not in self.fundamentals.PerfectConsonantIntervals:
                                TestedIntervals = []
                                while len(TestedIntervals) < len(self.fundamentals.ImperfectConsonantIntervals) and not PitchFound:
                                    # Now that randomness has been added, the algorithm will need to keep a running list of each tested interval to prevent itself from testing the same one multiple times
                                    IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                                    while IntervalToCheck in TestedIntervals:
                                        IntervalToCheck = self.fundamentals.ImperfectConsonantIntervals[randint(0, len(self.fundamentals.ImperfectConsonantIntervals) - 1)]
                                    TestedIntervals.append(IntervalToCheck)

                                    PitchToCheck = self.Cantus[i] + IntervalToCheck
                                    ResultingCounterpointDirection = PitchToCheck - self.Counterpoint[i - 1]

                                # Confirm that the pitch is within the given mode
                                    PitchInMode = False
                                    for each in self.fundamentals.Pitches:
                                        if self.fundamentals.Pitches[each] == PitchToCheck:
                                            if each[:-1] in self.fundamentals.Mode:
                                                PitchInMode = True
                                            else:
                                                PitchInMode = False
                                    if PitchInMode:
                                        if CantusDirection < 0 and ResultingCounterpointDirection < 0:
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection > 0 and ResultingCounterpointDirection > 0:
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                                        elif CantusDirection == 0 and ResultingCounterpointDirection == 0:
                                            self.Counterpoint.append(PitchToCheck)
                                            PitchFound = True
                                            break

                        if not PitchFound:
                            print("Failed to find a pitch")
                            self.Counterpoint.append(0)
                

    def FifthIteration(self):
        for i in range(len(self.Cantus)):
            if i == 0:
                NewPitch = self.Cantus[i] + self.fundamentals.PerfectConsonantIntervals[randint(0, len(self.fundamentals.PerfectConsonantIntervals) - 1)]
                self.Counterpoint.append(NewPitch)
            elif i == len(self.Cantus) - 2:
                self.Counterpoint.append(self.Cantus[i] + 9)
            elif i == len(self.Cantus) - 1:
                self.Counterpoint.append(self.Cantus[i] + 12)
            else:
                CantusDirection = self.Cantus[i] - self.Cantus[i - 1]

                # First try stepwise motion (with stepwise defined as less than a major third)
                if CantusDirection >= 0:
                    PitchToCheck = self.Counterpoint[i - 1] + 1

                    PitchInMode = False
                    while PitchInMode == False:
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                PitchInMode = True
                                break
                        PitchToCheck += 1

                    if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals or PitchToCheck - self.Cantus[i] in self.fundamentals.PerfectConsonantIntervals:
                        self.Counterpoint.append(PitchToCheck)
                        PitchFound = True
                    else:
                        # Add 1 again to see if a third works
                        PitchToCheck = self.Counterpoint[i - 1] + 1

                        PitchInMode = False
                        while PitchInMode == False:
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                    break
                            PitchToCheck += 1
                        
                        if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals or PitchToCheck - self.Cantus[i] in self.fundamentals.PerfectConsonantIntervals:
                            self.Counterpoint.append(PitchToCheck)
                            PitchFound = True
                        else:
                            # Try parallel motion in stepwise motion
                            PitchToCheck = self.Counterpoint[i - 1] + 1

                            PitchInMode = False
                            while PitchInMode == False:
                                for each in self.fundamentals.Pitches:
                                    if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                        PitchInMode = True
                                        break
                                PitchToCheck -= 1

                            if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals:
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                            else:
                                # Subtract 1 again to see if a third works
                                PitchToCheck = self.Counterpoint[i - 1] - 1

                                PitchInMode = False
                                while PitchInMode == False:
                                    for each in self.fundamentals.Pitches:
                                        if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                            PitchInMode = True
                                            break
                                    PitchToCheck -= 1
                                
                                if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals:
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                else:
                                    # If no suitable pitch has been found, the algorithm will cycle through all possible imperfect consonances
                                    for n in self.fundamentals.ImperfectConsonantIntervals:
                                        PitchToCheck = self.Cantus[i] + n
                                        if not PitchFound:
                                            for each in self.fundamentals.Pitches:
                                                if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                                    PitchFound = True
                                                    self.Counterpoint.append(self.Cantus[i] + n)
                                                    break
                                        
                                    if not PitchFound:
                                        for n in self.fundamentals.PerfectConsonantIntervals:
                                            if not PitchFound:
                                                PitchToCheck = self.Cantus[i] + n
                                                for each in self.fundamentals.Pitches:
                                                    if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode and self.Counterpoint[i - 1] - PitchToCheck < 0:
                                                        PitchFound = True
                                                        self.Counterpoint.append(self.Cantus[i] + n)
                                                        break
                                            
                                            if not PitchFound:
                                                self.Counterpoint.append(0)
                                                print("No suitable pitch found")
                
                elif CantusDirection < 0:
                    PitchToCheck = self.Counterpoint[i - 1] - 1

                    PitchInMode = False
                    while PitchInMode == False:
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode and (PitchToCheck in self.fundamentals.ImperfectConsonantIntervals or PitchToCheck in self.fundamentals.PerfectConsonantIntervals):
                                PitchInMode = True
                                break
                        PitchToCheck -= 1

                    if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals or PitchToCheck - self.Cantus[i] in self.fundamentals.PerfectConsonantIntervals:
                        self.Counterpoint.append(PitchToCheck)
                        PitchFound = True
                    else:
                        # Add 1 again to see if a third works
                        PitchToCheck = self.Counterpoint[i - 1] - 1

                        PitchInMode = False
                        while PitchInMode == False:
                            for each in self.fundamentals.Pitches:
                                if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                    PitchInMode = True
                                    break
                            PitchToCheck -= 1
                        
                        if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals or PitchToCheck - self.Cantus[i] in self.fundamentals.PerfectConsonantIntervals:
                            self.Counterpoint.append(PitchToCheck)
                            PitchFound = True
                        else:
                            # Try parallel motion in stepwise motion
                            PitchToCheck = self.Counterpoint[i - 1] + 1

                            PitchInMode = False
                            while PitchInMode == False:
                                for each in self.fundamentals.Pitches:
                                    if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                        PitchInMode = True
                                        break
                                PitchToCheck += 1

                            if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals:
                                self.Counterpoint.append(PitchToCheck)
                                PitchFound = True
                            else:
                                # Subtract 1 again to see if a third works
                                PitchToCheck = self.Counterpoint[i - 1] + 1

                                PitchInMode = False
                                while PitchInMode == False:
                                    for each in self.fundamentals.Pitches:
                                        if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                            PitchInMode = True
                                            break
                                    PitchToCheck += 1
                                
                                if PitchToCheck - self.Cantus[i] in self.fundamentals.ImperfectConsonantIntervals:
                                    self.Counterpoint.append(PitchToCheck)
                                    PitchFound = True
                                else:
                                    # If no suitable pitch has been found, the algorithm will cycle through all possible imperfect consonances
                                    for n in self.fundamentals.ImperfectConsonantIntervals:
                                        PitchToCheck = self.Cantus[i] + n
                                        for each in self.fundamentals.Pitches:
                                            if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode:
                                                PitchFound = True
                                                self.Counterpoint.append(self.Cantus[i] + n)
                                        
                                    if not PitchFound:
                                        for n in self.fundamentals.PerfectConsonantIntervals:
                                            PitchToCheck = self.Cantus[i] + n
                                            for each in self.fundamentals.Pitches:
                                                if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode and self.Counterpoint[i - 1] - PitchToCheck >= 0:
                                                    PitchFound = True
                                                    self.Counterpoint.append(self.Cantus[i] + n)
                                            
                                            if not PitchFound:
                                                self.Counterpoint.append(0)
                                                print("No suitable pitch found")
                                        




    def Smoothing(self):
        for i in range(len(self.Counterpoint) - 3):
            if abs(self.Counterpoint[i] - self.Counterpoint[i + 1]) > 7:
                median = round(sum(self.Counterpoint[i] + self.Counterpoint[i + 2])/2, 0)

                if self.Counterpoint[i] > self.Counterpoint[i + 2]:
                    PitchToCheck = self.Counterpoint[i] - median

                    PitchInMode = False
                    while PitchInMode == False:
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode and PitchToCheck in self.fundamentals.ImperfectConsonantIntervals:
                                PitchInMode = True
                                break
                        PitchToCheck -= 1

                    self.Counterpoint[i + 1] = PitchToCheck

                else:
                    PitchToCheck = self.Counterpoint[i] + median

                    PitchInMode = False
                    while PitchInMode == False:
                        for each in self.fundamentals.Pitches:
                            if self.fundamentals.Pitches[each] == PitchToCheck and each[:-1] in self.fundamentals.Mode and PitchToCheck in self.fundamentals.ImperfectConsonantIntervals:
                                PitchInMode = True
                                break
                        PitchToCheck += 1

                    self.Counterpoint[i + 1] = PitchToCheck