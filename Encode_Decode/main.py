from datetime import datetime

PRINTABLE_CHARACTERS = (
    ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3',
    '4', '5', '6', '7', '8', '9', '0', '[', ']', ';',
    '\\', '"', ',', '.', '/', '=', '-', '+', '_', ')',
    '(', '*', '&', '^', '%', '$', '#', '@', '!', '{',
    '}', '|', ':', '?', '>', '<', '`', '\'', '~', '\n'
)

CODED_VERSION = (
    ' ', '7', 'm', 'q', '8', 'a', '%', '+', 'x', '$',
    'c', '`', '@', '4', ':', '3', 't', '9', 'y', '!',
    'o', '.', '2', 'h', 'p', '^', '6', '<', 'd', '_',
    'f', '-', 'n', 'w', '(', '"', '0', '#', ')', 'v',
    'g', 'i', ']', '>', ',', ';', '[', '{', '|', 'u',
    'k', '~', '=', 'e', 'z', '&', '?', '1', 's', 'r',
    '5', '*', "'", '}', '/', 'j', 'l', '\\', 'b', '\n'
)


class RangeError(Exception):
    message = 'Invalid Option Please Try Again..'


def cipher_or_decipher():
    while True:
        try:
            encode_or_decode = int(input(
                "\nEnter 1 to encode/cipher a message \nEnter 2 to decode/translate a message\nOption: "))
        except ValueError:
            print("Non-numeric option found!, Please Try again..")
        except KeyboardInterrupt:
            print("You Cancelled the operation..")
            exit()
        else:
            if encode_or_decode > 2:
                print("Invalid Option Please Try Again..")
            else:
                break
    return encode_or_decode


def console_or_text_file():
    while True:
        try:
            console_or_file = int(input(
                '\nEnter 1 to enter the message in the console\nEnter 2 to specify the file name of the text file: '))
        except ValueError:
            print('Non-numeric option found! Please Try again..')
        except KeyboardInterrupt:
            print("You Cancelled the Operation..")
            exit()
        else:
            if console_or_file > 2 or console_or_file < 1:
                print("Invalid Option Please Try Again..")
            else:
                break
    return console_or_file


def cipher(raw_text):
    no_char = len(raw_text)
    counter = 0
    raw_text = list(raw_text)
    while counter < no_char:
        for idx in range(no_char):
            raw_text[idx] = CODED_VERSION[PRINTABLE_CHARACTERS.index(raw_text[idx])]
        counter = counter + 1
    return "".join(raw_text)


def decipher(secret_text):
    no_char = len(secret_text)
    counter = 0
    secret_text = list(secret_text)
    while counter < no_char:
        for idx in range(no_char):
            secret_text[idx] = PRINTABLE_CHARACTERS[CODED_VERSION.index(secret_text[idx])]
        counter = counter + 1
    return "".join(secret_text)


if __name__ == "__main__":
    text = ""
    mode = cipher_or_decipher()
    method = console_or_text_file()
    if mode == 1:  # cipher the message
        if method == 1:  # console
            text = input('Enter your Message: ')
            result = cipher(text.strip().lower())
            print(result.title())
        elif method == 2:  # text file
            file_name = input("Enter the file name: ")
            with open(file_name, 'r') as text_file:
                content = text_file.read()
                content = content.split('CIPHERED MESSAGE', 1)[0]
                result = cipher(content.strip().lower())
            with open(file_name, 'a') as file_result:
                file_result.write('\n\nCIPHERED MESSAGE, Date: ')
                file_result.write(str(datetime.now()) + '\n')
                file_result.write(result.title())
            print('Result is Saved in', file_name)
    elif mode == 2:  # decipher the message
        if method == 1:  # console
            text = input('Enter the message: ')
            result = decipher(text.strip().lower())
            print(result.title())
        elif method == 2:  # text file
            file_name = input('Enter the file name: ')
            with open(file_name, 'r') as text_file:
                content = text_file.read()
                content = content.split('DECIPHERED MESSAGE', 1)[0]
                result = decipher(content.strip().lower())
            with open(file_name, 'a') as file_result:
                file_result.write('\n\nDECIPHERED MESSAGE, Date: ')
                file_result.write(str(datetime.now()) + '\n')
                file_result.write(result.title())
            print('Result is Saved in', file_name)
