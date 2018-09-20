CAPITAL_LETTTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PASS1_CODED_VERSION = "#AKRTQIWEVHFYGDZXLPSOUBMNC"  # J
PASS2_CODED_VERSION = None


def user_select_option():
    while True:
        try:
            encode_or_decode = int(input(
                "\nEnter 1 to encode/cipher a message \nEnter 2 to decode/translate a message\nOption: "))
            print("\n")
            type_or_file = int(input(
                "Enter 1 to Type your message on the Terminal\nEnter 2 if you wish to specify the file location of text file(*.txt files only!): "))
        except ValueError:
            print("Non-numeric option found!, Please Try again..")
        except KeyboardInterrupt:
            print("You Cancelled the operation..")
            exit()
        else:
            break
    return encode_or_decode, type_or_file


if __name__ == "__main__":
    user_select_option()
    pass
    # user selects an option to whether encode or decode the message
    # user can type the message on the console or specify
    # location of the text file that contains the message
    # the result will be displayed on the terminal/console
    # window and also be written on the text file.
