import string

alphabet = string.ascii_lowercase + " "

letters = dict(enumerate(alphabet))



encoding = {}

encryption_key = 3

for x in letters:
    result = (x + encryption_key) % 27
    print(result)
    encoding[letters[x]] = result

message = "hi my name is caesar"



def caesar(the_message, the_encryption_key):
    encoded_message = ""
    for x in the_message:
        #encoded_message += str(encoding[x] + the_encryption_key)
        encoded_message += (letters[encoding[x]])
    print(encoded_message)


caesar(message, encryption_key)


# Here is my code that the site did not accept, but works

# def caesar(message, encryption_key):
#     # return the encoded message as a single string!
#     coded_message = ""
#     for x in message:
#         coded_message += str(encoding[x] + 3)
#     return coded_message
#
#
# encoded_message = caesar(message, encryption_key)
# print(encoded_message)
# --------------------------------------------