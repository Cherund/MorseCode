MORSE_CODE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                   '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
                   '-': '-....-', '(': '-.--.', ')': '-.--.-'}


def message_request():
    message = input('Please, print what you want to encrypt: \n')
    print(f'Here is your encrypted message:\n {encrypt(message)}')
    want_to_continue()

def encrypt(message):
    message_list = list(message)
    encrypted_message = ''
    for letter in message_list:
        if letter != ' ':
            encrypted_message += MORSE_CODE_DICT[letter.upper()]
        else:
            encrypted_message += ' '

    return encrypted_message

def want_to_continue():
    contin = input('Do you want to continue? Press Y for Yes and N for No \n')
    if contin.upper() == 'Y':
        message_request()
    else:
        return


print('Welcome to the Morse code encryption!')
message_request()
