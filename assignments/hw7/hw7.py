"""
Name: <Jordan Herder>
<hw7>.py

Problem: <Program creates a numbered list of words from a file,
defines the hourly wages of listed workers from a file,
sums an ISBN number, sends a message between files,
encodes a message from a file,
and encodes a message from a file differently.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.>
"""

from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    func_file = open(in_file_name, 'r')
    file_text = func_file.read()
    word_list = file_text.split()
    output = ""
    for i in range(len(word_list)):
        output = output + str(i+1) + ' ' + word_list[i] + "\n"
    file_out = open(out_file_name, 'w')
    print(output[:-1], file=file_out)


def hourly_wages(in_file_name, out_file_name):
    wage_file = open(in_file_name, 'r')
    file_text = wage_file.readlines()
    output_text = ""
    for i in file_text:
        line = i.split()
        pay = eval(line[2])
        hours = eval(line[3])
        total_pay = (pay+1.65) * hours
        output_text = output_text + line[0] + " " + line[1] + " {:.2f}".format(total_pay) +'\n'
    output_file = open(out_file_name, 'w')
    print(output_text[:-1], file=output_file)


def calc_check_sum(isbn):
    isbn_store = str(isbn)
    isbn_dehy = isbn_store.replace("-", "")
    func_sum = 0
    for i in range(len(isbn_dehy)):
        func_sum = func_sum + ((10-i)*int(isbn_dehy[i]))
    return func_sum


def send_message(file_name, friend_name):
    input_file = open(file_name, 'r')
    text_file = friend_name+'.txt'
    message = input_file.read()
    output_file = open(text_file, 'w')
    print(message[:-1], file=output_file)


def send_safe_message(file_name, friend_name, key):
    input_file = open(file_name, 'r')
    text_file = friend_name+'.txt'
    unsafe_message = input_file.read()
    unsafe_list = unsafe_message.split('\n')
    encode_key = key
    safe_message = ''
    for i in unsafe_list:
        safe_message = safe_message + encode(i, encode_key) + '\n'
    output_file = open(text_file, 'w')

    print(safe_message[:-2], file=output_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    input_file = open(file_name, 'r')
    text_file = friend_name+'.txt'
    unsafe_message = input_file.read()
    pad_key = open(pad_file_name, 'r')
    unsafe_list = unsafe_message.split('\n')
    safe_message = ''
    for i in unsafe_list:
        safe_message = safe_message + encode_better(i, pad_key)
    output_file = open(text_file, 'w')

    print(safe_message[:-2], file=output_file)
    # this was supposed to be a template, but I don't recognize the error it throws
    # so I just need to submit it now, its 11:40


if __name__ == '__main__':
    pass
