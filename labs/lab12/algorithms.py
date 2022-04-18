def read_data(filename):
    file = open(filename, 'r').read()
    file = file.replace('\n', ' ')
    split_file = file.split()
    index = 0
    while index < len(split_file):
        split_file[index] = eval(split_file[index])
        index += 1
    return split_file


def is_in_linear(search_val, values):
    index = 0
    while index < len(values):
        if search_val == values[index]:
            return True
        index += 1
    return False
