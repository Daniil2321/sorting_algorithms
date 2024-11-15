from winsound import Beep


"""
first_octave = {"Do": 261.63, "Do#": 277.18, "Re": 293.66, "Re#": 311.13, "Mi": 329.63,
                "Fa": 349.23, "Fa#": 369.99, "Sol": 392, "Sol#": 415.3, "La": 440, "La#": 466.16, "Ti": 493.88}
"""

first_octave = {"do": 261, "do#": 277, "re": 293, "re#": 311, "mi": 329,
                "fa": 349, "fa#": 369, "sol": 392, "sol#": 415, "la": 440, "la#": 466, "ti": 493}

# notes = list(first_octave.keys())

notes = input("Notes: ").lower().split(" ")

for note in notes:
    octave = note[-1]
    num = 1

    try:
        num = int(octave)

    except ValueError:
        pass

    else:
        note = note.strip(str(num))

    try:
        Beep(first_octave[note]*num, 500)

    except KeyError:
        print("Wrong note")
