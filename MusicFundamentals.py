"""
This class defines the fundamentals needed in order to complete counterpoint exercises:
A list of available pitches, and intervallic relationships.
"""

class Fundamentals():
    """
    This dictionary defines a list of all available pitches.  Similar to the pitch class notation used in post-tonal music,
    each pitch is assigned a number, allowing the computer to calculate the given interval; moreover, enharmonic spellings are 
    ignored.

    Unlike post-tonal notation, however, the machine requires a higher level of specificity than is available through the numbers 
    one through twelve.  For this reason, the numeric scale is extended to 47 to give a precise name to every available pitch on the 
    grand staff.
    """

    Pitches = {
        "C2": 0,
        "C#2": 1,
        "D2": 2,
        "D#2": 3,
        "E2": 4,
        "F2": 5,
        "F#2": 6,
        "G2": 7,
        "G#2": 8,
        "A2": 9,
        "A#2": 10,
        "B2": 11,

        "C3": 12,
        "C#3": 13,
        "D3": 14,
        "D#3": 15,
        "E3": 16,
        "F3": 17,
        "F#3": 18,
        "G3": 19,
        "G#3": 20,
        "A3": 21,
        "A#3": 22,
        "B3": 23,

        "C4": 24,
        "C#4": 25,
        "D4": 26,
        "D#4": 27,
        "E4": 28,
        "F4": 29,
        "F#4": 30,
        "G4": 31,
        "G#4": 32,
        "A4": 33,
        "A#4": 34,
        "B4": 35,

        "C5": 36,
        "C#5": 37,
        "D5": 38,
        "D#5": 39,
        "E5": 40,
        "F5": 41,
        "F#5": 42,
        "G5": 43,
        "G#5": 44,
        "A5": 45,
        "A#5": 46,
        "B5": 47
    }

    """
    The interval of a given pair of pitches can be calculated by subtracting their given values.  For example, subtracting D2 (2)
    from C2 (0) gives the value of 2, which represents a major second and will be saved as a dissonant interval.  For larger intervals,
    one need only reduce a given interval by twelve to find its interval class.  
    D5 (38) - C2 (0) = 38.  
    38 - 12 = 26.  
    26 - 12 = 14. 
    14 - 12 = 2.
    """

    PerfectConsonantIntervals = [0, 5, 7, 12]
    ImperfectConsonantIntervals = [3, 4, 8, 9]
    DissonantIntervals = [1, 2, 6, 10, 11]

    Mode = ["A", "B", "C", "D", "E", "F", "G"]


    def CalculateInterval(self, A, B):
        """
        This function is used to calculate the interval of a given pair of pitches.  It will always return the interval from
        the bass reduced to be within an octave.
        """

        # Find the interval from the bass
        if A >= B:
            Interval = A - B
        else:
            Interval = B - A

        # Continually reduce the interval by twelve until it fits within an octave
        while Interval >= 12:
            Interval = Interval - 12

        # Send the result back to wherever this function was called
        return Interval

    def IntervalClass(self, Interval):
        if Interval in self.PerfectConsonantIntervals:
            return 'P'
        elif Interval in self.ImperfectConsonantIntervals:
            return 'I'
        elif Interval in self.DissonantIntervals:
            return 'D'