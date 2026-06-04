# Today I learned about dictionaries in python through DataCamp
# So, I decided to make this
morse_code_dict = {
    # this dictionary was made by Gemini. If you see an error, don't worry. I'm not going to fix it.
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/', ".": ".-.-.-", 
    ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", ":": "---...", ";": "-.-.-.", "=": "-...-", 
    "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.", "(": "-.--.", ")": "-.--.-", "@": ".--.-.", "$": "...-..-"
    # I later added the symbols. I learned that @ is the newest morse code symbol added in 2004.
}
print("TRANSLATE to MORSE CODE\n------------------------------------------\n[1] Translation available for only English\n[2] All invalid characters will be skipped\n")
userInput = input("Write here: ").upper()
result = ''

for char in userInput:
    if char not in morse_code_dict:
        print(f'"{char}" was skipped. Invalid/no Morse code')
        continue
    result += morse_code_dict[char] + ' '
print(result)
