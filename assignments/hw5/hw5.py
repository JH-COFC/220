"""
Name: <Jordan Herder>
<hw5>.py

Problem: <Contains functions which reverse the order of a first and last name,
provide the name of a company from a three-part web address,
provide the initials of entered students,
provide the initials from a list of names provided,
give every third character of a set of sentences,
give the average word length of an entered sentence,
and translate a sentence into a simplified pig latin.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("enter a name (first last):")
    split_name = name.split(' ')
    print(split_name[1],split_name[0],sep=', ')


def company_name():
    domain = input("enter a domain:")
    three_parts = domain.split('.')
    print(three_parts[1])


def initials():
    student_num = eval(input("how many students are in the class?"))
    for i in range(1,student_num+1):
        name = input("What is the name of student "+str(i)+"?")
        split_name = name.split()
        output = ""
        for j in split_name:
            output = output+str(j)[0]
        print(output)


def names():
    name_string = input("enter a list of names:")
    name_list = name_string.split(", ")
    initial = ""
    for i in name_list:
        split_names = i.split()
        for j in split_names:
            initial = initial + j[0]
        initial = initial + " "
    print(initial[:-1])


def thirds():
    sentence_num = eval(input("enter the number of sentences:"))
    output = ""
    for i in range(1,sentence_num+1):
        sentence = input("enter sentence "+str(i)+":")
        output = output + "\n" + sentence[0::3]
    print(output[1::])


def word_average():
    sentence = input("enter a sentence:")
    split_sentence = sentence.split()
    letters = 0
    for i in split_sentence:
        letters = letters + len(i)
    print(letters/len(split_sentence))


def pig_latin():
    sentence = input("enter a sentence to convert to pig latin:")
    split_sentence = sentence.split()
    output = ""
    for i in split_sentence:
        word_body = i[1:]
        first_letter = i[0]
        output = output+word_body.lower()+first_letter.lower()+"ay "
    print(output[:-1])


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    # pig_latin()
    pass
