"""
This class defines the Cantus Firmi used in Gradus ad Parnassum using the notation scheme defined in MusicFundamentals.py
"""

class CantusFirmus():

    # The modes are defined in such a way that their respective cantus firmus can be stored along side their name.
    Modes = {
        "Ionian": [24, 28, 29, 31, 28, 33, 31, 28, 29, 28, 26, 24],
        "Dorian": [26, 29, 28, 26, 31, 29, 33, 31, 29, 28, 26],
        "Phrygian": [28, 24, 26, 24, 21, 33, 31, 28, 29, 28],
        "Lydian": [17, 19, 21, 17, 14, 16, 17, 24, 21, 17, 19, 17],
        "Mixolydian": [19, 24, 23, 19, 24, 28, 26, 31, 28, 24, 26, 23, 21, 19],
        "Aeolian": [21, 24, 23, 26, 24, 28, 29, 28, 26, 24, 23, 21]
    }

    def GetCantus(self, Species, Mode):
        """
        This function returns the cantus firmus as needed for a given species.  The caller can specify which species and
        which mode is desired.

        For 2/1 or 4/1 counterpoint, the cantus defined above will need to be expanded to accomodate the larger number of 
        pitches.  Rather than associate four counterpoint pitches with one cantus pitch in a 4/1 exercise, the cantus pitch
        will be repeated four times, allowing each counterpoint pitch to be associated with a single cantus pitch.
        """

        # Pull the desired cantus from the dictionary defined aboe
        Cantus = self.Modes[Mode]

        # Expand the cantus to reflect the species
        if Species == 1:
            return Cantus

        elif Species == 2:
            NewCantus = []
            for each in Cantus:
                # Double each pitch
                NewCantus.append(each)
                NewCantus.append(each)
            return NewCantus

        elif Species == 3:
            NewCantus = []
            for each in Cantus:
                # Double eahc pitch
                NewCantus.append(each)
                NewCantus.append(each)
            return NewCantus

        elif Species == 4:
            NewCantus = []
            for each in Cantus:
                # Quadruple each pitch
                NewCantus.append(each)
                NewCantus.append(each)
                NewCantus.append(each)
                NewCantus.append(each)
            return NewCantus

        elif Species == 5:
            NewCantus = []
            for each in Cantus:
                # Quadruple each pitch
                NewCantus.append(each)
                NewCantus.append(each)
                NewCantus.append(each)
                NewCantus.append(each)
            return NewCantus