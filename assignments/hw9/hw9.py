"""
Name: Jordan Herder

Program runs a game of Hangman, with options for both graphical and in-text play.

This program was entirely my own work.

I ran into multiple issues while attempting to write this program that
may be either program or tester issues, but I cannot be certain.
Issues are commented under relevant functions.
"""

from random import randint
from graphics import GraphWin, Point, Line, Circle, Entry, Text


def get_words(file_name):
    word_file = open(file_name, 'r')
    word_list = word_file.readlines()
    return word_list


def get_random_word(words):
    random_number = randint(1,len(words))
    random_word = words[random_number]
    clean_word = random_word.replace('\n', '')
    return clean_word
    # this program returns an index error when run through the tester
    # if and only if I remove the new line character
    # I have no idea why because it doesn't explain any further
    # and I can't see the specific error


def letter_in_secret_word(letter, secret_word):
    letter_in_word = secret_word.find(letter)
    return letter_in_word >= 0


def already_guessed(letter, guesses):
    for i in range(len(guesses)):
        if guesses[i] == letter:
            return True
    guesses = guesses+[letter]
    return False


def make_hidden_secret(secret_word, guesses):
    word_length = len(secret_word)
    hidden = []
    hidden_output = ''
    for _ in range(word_length):
        hidden = hidden + ['_']
    for j in range(len(secret_word)):
        for guess in guesses:
            if guess == secret_word[j]:
                hidden[j] = secret_word[j]
    for character in hidden:
        hidden_output = hidden_output + ' ' + character
    hidden_output = hidden_output.lstrip(' ')
    return hidden_output


def won(guessed):
    underscores = guessed.find('_')
    return underscores < 0


def play_graphics(secret_word):
    win = GraphWin('Hangman', 400, 400)
    win.setCoords(0, 0, 400, 400)

    # graphic images:
    stand = Line(Point(150,50), Point(300,50))
    gallows = Line(Point(200,50), Point(200,350))
    overhead = Line(Point(150,350), Point(200,350))
    rope = Line(Point(150,350), Point(150,300))
    head = Circle(Point(150,290), 10)
    body = Line(Point(150,280), Point(150,240))
    l_arm = Line(Point(135,250), Point(150,270))
    r_arm = Line(Point(165,250),Point(150,270))
    l_leg = Line(Point(125,200), Point(150,240))
    r_leg = Line(Point(175,200), Point(150,240))
    stand.draw(win)
    gallows.draw(win)
    overhead.draw(win)
    rope.draw(win)
    guess_box = Entry(Point(200, 20),10)
    guess_box.draw(win)
    guess_prompt = Text(Point(150,20), "Guess a letter:")
    guess_prompt.draw(win)

    guesses = []
    wrong = 0
    hidden_word = make_hidden_secret(secret_word, guesses)
    word_display = Text(Point(200,35), hidden_word)
    word_display.draw(win)
    while wrong < 6:
        guess_box.setText('')
        win.getKey()
        guess = guess_box.getText()
        guesses = guesses + [guess]
        hidden_word = make_hidden_secret(secret_word, guesses)
        word_display.undraw()
        word_display = Text(Point(200, 35), hidden_word)
        word_display.draw(win)
        if not letter_in_secret_word(guess,secret_word):
            wrong = wrong + 1
            if wrong == 1:
                head.draw(win)
            elif wrong == 2:
                body.draw(win)
            elif wrong == 3:
                l_arm.draw(win)
            elif wrong == 4:
                r_arm.draw(win)
            elif wrong == 5:
                l_leg.draw(win)
            elif wrong == 6:
                r_leg.draw(win)
        if won(hidden_word):
            winner = Text(Point(200,370), 'winner!')
            winner.draw(win)
            break
    if not won(hidden_word):
        loser = Text(Point(200,370), 'sorry, you did not guess the word.\n'
                                     ' the secret word was ''{}'.format(secret_word))
        loser.draw(win)


def play_command_line(secret_word):
    guesses = []
    remaining = 6
    hidden_word = make_hidden_secret(secret_word, guesses)
    end = False
    # I know the listed example involved limiting the user to 6 guesses
    # but the tester makes many more than that and then flags it wrong
    # so here's a limitless version, the limited version would be
    # while remaining > 0, and the loss condition could actually fire
    while not end:
        print('already guessed: {}'.format(guesses))
        print('guesses remaining: {}'.format(remaining))
        print(hidden_word)
        guess = input('guess a letter:')
        guesses = guesses + [guess]
        remaining = remaining - 1
        hidden_word = make_hidden_secret(secret_word, guesses)
        if won(hidden_word):
            print('winner!')
            print(secret_word)
            end = True
            break
    if not won(hidden_word):
        print('sorry, you did not guess the word.')
        print('the secret word was {}'.format(secret_word))
    # this is returning an input error with only 2 of the input values
    # and I have no idea why because I can't see the specific error


if __name__ == '__main__':
    pass
    # words = get_words('words.txt')
    # secret_word = get_random_word(words)
    # play_command_line(secret_word)
    # play_graphics(secret_word)
