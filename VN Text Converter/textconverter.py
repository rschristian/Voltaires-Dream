'''

Voltaire's Nightmare Localization Converter (by Isildur)

Because the game font is changed, it is required to use only characters that are in the old game font.
This program allows to convert normal text into localization that the game can read.

NOTE: You must have a text file named original_text.txt in the same directory as .py file.
If you don't have this file, or original_text.txt is empty the program won't work.

'''

import io
import sys

try:
    test_file = open("original_text.txt")
    test_file.close()
except IOError:
    print("Error: File original_text.txt does not exist!")
    print("Exiting program")
    sys.exit()

def check_if_empty(orig):
    
    orig.seek(0)
    first_char = orig.read(1)
    if not first_char:
        print("File is empty!")
        print("Please make sure your file has some text in to convert")
        return True
    else:
        orig.seek(0)
        return False
    orig.close()

def read_char(orig):
    
    #reads 1 char from original_text
    char = orig.read(1)
    while char:
        yield char
        char = orig.read(1)

def convert_char(char):

    #dozens of if statements here, but I think it's the only way to do this
    #long S doesn't work
    if char == "ſ":
        print("\nſ is not a supported character!")
        print("Terminating program")
        sys.exit()
        
    #All variants of A
    if char == "Ā":
        char = "$"
    elif char == "ā":
        char = "@"
    elif char == "Ă":
        char = "`"
    elif char == "ă":
        char = "{"
    elif char == "Ą":
        char = "}"
    elif char == "ą":
        char = "€"
        
    #All variants of C
    elif char == "Ć":
        char = "‚"
    elif char == "ć":
        char = "ƒ"
    elif char == "Č":
        char = "„"
    elif char == "č":
        char = "…"
        
    #All variants of D
    elif char == "Ď":
        char = "†"
    elif char == "ď":
        char = "‡"
    elif char == "Đ":
        char = "ˆ"
    elif char == "đ":
        char = "‰"
        
    #All variants of E
    elif char == "Ē":
        char = "‹"
    elif char == "œ":
        char = "‘"
    elif char == "ē":
        char = "’"
    elif char == "Ė":
        char = "“"
    elif char == "ė":
        char = "”"
    elif char == "Ę":
        char = "•"
    elif char == "ę":
        char = "–"
    elif char == "Ě":
        char = "—"
    elif char == "ě":
        char = "˜ "
        
    #All variants of G
    elif char == "Ğ":
        char = "™"
    elif char == "ğ":
        char = "›"
        
    #All variants of I
    elif char == "Ī":
        char = "Ÿ"
    elif char == "ī":
        char = "¡"
    elif char == "Į":
        char = "¢"
    elif char == "į":
        char = "£"
    elif char == "İ":
        char = "¤"
    elif char == "ı":
        char = "¥"

    #All variants of L
    elif char == "Ł":
        char = "¦"
    elif char == "ł":
        char = "§"

    #All variants of N
    elif char == "Ń":
        char = "¨"
    elif char == "ń":
        char = "©"
    elif char == "Ň":
        char = "ª"
    elif char == "ň":
        char = "«"

    #All variants of O
    elif char == "Ō":
        char = "¬"
    elif char == "ō":
        char = "®"
    elif char == "Ő":
        char = "¯"
    elif char == "ő":
        char = "°"

    #All variants of R
    elif char == "Ř":
        char = "±"
    elif char == "ř":
        char = "²"

    #All variants of S
    elif char == "Ş":
        char = "³"
    elif char == "ş":
        char = "´"

    #All variants of T
    elif char == "Ţ":
        char = "µ"
    elif char == "ţ":
        char = "¶"
    elif char == "Ť":
        char = "·"
    elif char == "ť":
        char = "¸"

    #All variants of U
    elif char == "Ū":
        char = "¹"
    elif char == "ū":
        char = "º"
    elif char == "Ų":
        char = "»"
    elif char == "ų":
        char = "¼"

    #All variants of Z including yogh
    elif char == "Ź":
        char = "½"
    elif char == "ź":
        char = "¾"
    elif char == "Ż":
        char = "¿"
    elif char == "ż":
        char = "×"
    elif char == "Ȝ":
        char = "÷"
    elif char == "ȝ":
        char = "ÿ"

    print(char, sep="", end="")
        
orig = io.open("original_text.txt", encoding="utf-8")

#check if original_text.txt is empty
emptycheck = check_if_empty(orig)

if emptycheck == True:
    print("Exiting program")
    orig.close()
    sys.exit()

#convert each char one by one and print
for char in read_char(orig):
    convert_char(char)
    
#end of program
#close file
orig.close()
