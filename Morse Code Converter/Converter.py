morse_code = \
 {
 "A": ".-"  , "N": "-."  , "1": ".----",
 "B": "-...", "O": "---" , "2": "..---",
 "C": "-.-.", "P": ".--.", "3": "...--",
 "D": "-.." , "Q": "--.-", "4": "....-",
 "E": "."   , "R": ".-." , "5": ".....",
 "F": "..-.", "S": "..." , "6": "-....",
 "G": "--." , "T": "-"   , "7": "--...",
 "H": "....", "U": "..-" , "8": "---..",
 "I": ".."  , "V": "...-", "9": "----.",
 "J": ".---", "W": ".--" , "0": "-----",
 "K": "-.-" , "X": "-..-",
 "L": ".-..", "Y": "-.--",
 "M": "--"  , "Z": "--.."
 }

def converter(sentence):
    morse_sentence = []

    for letter in sentence:
        if letter.upper() in morse_code:
            morse_sentence.append(morse_code[letter.upper()])
        else:
            morse_sentence.append("/")

    morse_coded_sentence = " ".join(morse_sentence)
    return morse_coded_sentence













