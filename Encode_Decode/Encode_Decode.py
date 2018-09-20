PRINTABLE_LETTTER = (' ', 'a', 'b', 'c', 'd', 'e', 'f',
                     'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
                     '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '[', ']', ';', '\\', '"', ',', '.', '/', '=', '-', '+', '_',
                     ')', '(', '*', '&', '^', '%', '$', '#', '@', '!', '{', '}', '|', ':', '?', '>', '<', '`', '~', '\'')
CODED_VERSION = ()


def user_select_option():
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
            break
    return encode_or_decode


def cipher(text):
    pass


def decipher(text):
    pass


if __name__ == "__main__":
    text = ""
    mode = user_select_option()
    if mode == 1:
        cipher(text)
    elif mode == 2:
        decipher(text)

    # user selects an option to whether encode or decode the message
    # user can type the message on the console or specify
    # location of the text file that contains the message
    # the result will be displayed on the terminal/console
    # window and also be written on the text file.
