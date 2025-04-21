

dit = "*"
dah = "-"

morse_traslator = {
    'a': dit+dah,
    'b': dah+3*dit,
    'c': (dah+dit)*2,
    'd': dah+2*dit, 
    'e': dit, 
    'f': dit*2+dah+dit, 
    'g': dah*2+dit, 
    'h': dit*4, 
    'i': dit*2, 
    'j': dit+dah*3, 
    'k': dah+dit+dah, 
    'l': dit+dah+dit*2, 
    'm': dah*2, 
    'n': dah+dit, 
    'o': dah*3, 
    'p': dit+dah*2+dit, 
    'q': dah*2+dit+dah, 
    'r': dit+dah+dit, 
    's': dit*3, 
    't': dah, 
    'u': dit*2+dah, 
    'v': dit*3+dah, 
    'w': dit+dah*2, 
    'x': dah+dit*2+dah, 
    'y': dah+dit+dah*2, 
    'z': dah*2+dit*2,
    '1': dit+dah*4,
    '2': dit*2+dah*3,
    '3': dit*3+dah*3,
    '4': dit*4+dah,
    '5': dit*5,
    '6': dah+dit*4,
    '7': dah*2+dit*3,
    '8': dah*3+dit*2,
    '9': dah*4+dit,
    '0': dah*5,
    ' ': " "
        
}

unit = " "
space_between_letters = 3*unit
space_between_words = 7*unit



def translate_to_morse(word):
    translation = ""
    for letter in word:
        if letter != " ":
            translation = translation + morse_traslator[f'{letter}'] + space_between_letters
        else: 
            translation += space_between_words
    print(translation)
        
def morse_to_normal(word):
    if word[-1] != " ":
        word += " "
    translation = ""
    one_letter = ""
    for symbol in word:
        if symbol != " ":
            one_letter += symbol
        else:
            for letter, value in morse_traslator.items():
                if value == one_letter:
                    translation = translation + letter
            one_letter = ""
        
    print(translation)
    
    
translate_to_morse("ivan is the best")
morse_to_normal("**   ***-   *-   -*          **   ***          -   ****   *          -***   *   ***   - ")

def start_fun():
    which_type = input("Do you wnat to translate 1. To Morse, or 2. From Morse? (1 or 2 or 'end' only answers): ")
    if which_type == "1":
        word = input("Please, write your sentence: ").strip(".").strip(",").strip("!").strip("?").lower()
        translate_to_morse(word)
        start_fun()
    elif which_type == "2":
        word = input("Please, write your sentence: ").strip(".").strip(",").strip("!").strip("?").lower()
        morse_to_normal(word)
        start_fun()
    elif which_type == "end":
        print("Good Luck!")
    else:
        print("1 or 2 or 'end' only answers")
        start_fun()
        

start_fun()
