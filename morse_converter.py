import time
import winsound

morse_alphabet = {"A": "● ▬", "B": "▬ ● ● ●", "C": "▬ ● ▬ ●", "D": "▬ ● ●", "E": "●", "F": "● ● ▬ ●", "G": "▬ ▬ ●",
                  "H": "● ● ● ●", "I": "● ●", "J": "● ▬ ▬ ▬ ", "K": "▬ ● ▬ ", "L": "● ▬ ● ● ", "M": "▬ ▬ ",
                  "N": "▬ ●", "O": "▬ ▬ ▬", "P": "● ▬ ▬ ●", "Q": "▬ ▬ ● ▬", "R": "● ▬ ●", "S": "● ● ●", "T": "▬",
                  "U": "● ● ▬", "V": "● ● ● ▬", "W": "● ▬ ▬", "X": "▬ ● ● ▬", "Y": "▬ ● ▬ ▬", "Z": "▬ ▬ ● ●",
                  " ": "SPACE", "1": "● ▬ ▬ ▬ ▬ ", "2": "● ● ▬ ▬ ▬ ", "3": "● ● ● ▬ ▬ ", "4": "● ● ● ● ▬ ",
                  "5": "● ● ● ● ● ", "6": "▬ ● ● ● ●", "7": "▬ ▬ ● ● ●", "8": "▬ ▬ ▬ ● ●", "9": "▬ ▬ ▬ ▬ ●",
                  "0": "▬ ▬ ▬ ▬ ▬"}
MORSE_FREQUENCY = 1000
SHORT_SOUND = 120
LONG_SOUND = 360


def text_to_morse(user_input):
    """Converts Users text input to Morse code"""
    user_text = user_input
    # check every letter in user's input
    for letter in user_text:
        # if letter is blank space it will pause
        if letter.isspace():
            time.sleep(0.84)
            print("space")
        else:
            # checks the library for that letters value in morse code
            morse_code = morse_alphabet[letter.capitalize()]
            # checks the morse code unit and plays the corresponding sound
            for char in morse_code:
                print(char)
                if char == "●":
                    winsound.Beep(frequency=MORSE_FREQUENCY, duration=SHORT_SOUND)
                elif char == "▬":
                    winsound.Beep(frequency=MORSE_FREQUENCY, duration=LONG_SOUND)
                time.sleep(0.12)
            print("end_letter")
        time.sleep(0.36)
