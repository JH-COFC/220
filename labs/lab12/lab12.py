def find_and_remove_first(list, value):
    index = 0
    replaced = False
    while index < len(list) and not replaced:
        if list[index] == value:
            list.insert(index, 'Jordan')
            list.remove(value)
            replaced = True
        index += 1
    print(list)


def num_digits():
    user_input = eval(input('enter a number (0 or negative to end)'))
    user_input_divided = user_input
    while user_input > 0:
        divisions = 0
        while user_input_divided > 0:
            user_input_divided = user_input_divided//10
            divisions += 1
        print(divisions)
        user_input = eval(input('enter a number (0 or negative to end)'))
        user_input_divided = user_input


def good_input():
    user_input = eval(input('enter a number at least 1 and at most 10'))
    while user_input < 1 or user_input > 10:
        user_input = eval(input('please enter a number at least 1 and at most 10'))
    if 1 <= user_input <= 10:
        return user_input


def hi_lo_game():
    from random import randint
    correct_guess = randint(1, 100)
    guesses = 0
    correct = False
    while guesses < 7 and not correct:
        user_input = eval(input('guess a number between 1 and 100'))
        if user_input < correct_guess:
            print('too low')
        if user_input > correct_guess:
            print('too high')
        if user_input == correct_guess:
            print('correct')
            correct = True
        guesses += 1
    if correct:
        print('You win in {} guesses!'.format(guesses))
    else:
        print('Sorry, you lose. The number was {}.'.format(correct_guess))


if __name__ == "__main__":
    find_and_remove_first([1, 2, 3], 2)
    find_and_remove_first([1, 4, 3], 2)
    from algorithms import read_data, is_in_linear
    data = read_data('data_sorted.txt')
    x = is_in_linear(5, data)
    print(x)
    y = is_in_linear(999, data)
    print(y)
    good_input()
    num_digits()
    hi_lo_game()
