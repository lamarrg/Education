import string

alphabet = string.ascii_lowercase + " "

letters = dict(enumerate(alphabet))

message = "hi my name is caesar"

encoding = {}

encryption_key = 3


for x in letters:
    result = (x + encryption_key) % 27
    encoding[letters[x]] = result


def caesar(the_message, the_encryption_key):
    encoded_message = ""
    for x in the_message:
        encoded_message += (letters[encoding[x]])
    print(encoded_message)


caesar(message, encryption_key)

