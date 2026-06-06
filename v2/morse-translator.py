morse_code_dict = {
    # this dictionary was made by Gemini. If you see an error, don't worry. I'm not going to fix it.
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/', ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.", ":": "---...", ";": "-.-.-.", "=": "-...-", "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.", "(": "-.--.", ")": "-.--.-", "@": ".--.-.", "$": "...-..-" # I later added the symbols. I learned that @ is the newest morse code symbol added in 2004.
}

reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

print("MORSE CODE TRANSLATOR\n------------------------------------------\n[1] Translation available for only English\n[2] All invalid characters will be skipped\n")
print("Choose translation type:\n[1] Text to Morse code\n[2] Morse code to Text")
translation_type = input("Write here (1 or 2): ")
match translation_type:
    case "1":
        print("Selected: Text to Morse code\n\n")
        userInput = input("Write here: ").upper()
        result = ''

        for char in userInput:
            if char not in morse_code_dict:
                print(f'"{char}" was skipped. Invalid/no Morse code available.')
                continue
            result += morse_code_dict[char] + ' '
        print(result)
    case "2":
        print('Selected: Morse code to Text\nType "?Help" for instructions\n\n')
        userInput = input("Write here: ").lower()
        result = ''
        while userInput == "?help":
            print("Instructions:\n[1] Separate letters in Morse code with spaces\n[2] Separate words with a slash (/)\n[3] All invalid characters will be skipped\n")
            userInput = input("Write here: ").lower()

        for char in userInput.split():
            if char not in reverse_morse_code_dict:
                print(f'"{char}" was skipped. Invalid/no Text character available.')
                continue
            result += reverse_morse_code_dict[char]
        print(result)
