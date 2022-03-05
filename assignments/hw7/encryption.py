def encode(message, key):
    coded_message = []
    output = ""
    for i in message:
        coded_message = coded_message + [(ord(i) + key)]
    for j in coded_message:
        output = output + chr(j)
    return output


def encode_better(message, key):
    coded_message = []
    output = ""
    for i in range(len(message)):
        coded_message = coded_message + [((ord(message[i])-65) + (ord(key[i])-65)) % 58]
    for j in coded_message:
        output = output+chr(j+65)
    return output
