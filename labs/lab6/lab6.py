from graphics import *


def vigenere():
    height = 400
    width = 400
    win = GraphWin("Vigenere", width, height)
    win.setCoords(0, 0, 400, 400)
    message_prompt = Text(Point(80, 300), "Message to code")
    key_prompt = Text(Point(80, 270), "Enter Keyword")
    button_text = Text(Point(200, 200), "Encode")
    button_frame = Rectangle(Point(170, 170), Point(230, 230))
    message_box = Entry(Point(250, 300), 20)
    key_box = Entry(Point(250, 270), 10)
    message_prompt.draw(win)
    key_prompt.draw(win)
    button_text.draw(win)
    button_frame.draw(win)
    message_box.draw(win)
    key_box.draw(win)

    win.getMouse()
    message_entry = message_box.getText()
    key_entry = key_box.getText()
    message_store = message_entry.split()
    key_store = key_entry.split()
    message = ""
    key = ""
    for i in message_store:
        message = message+i.upper()
    for j in key_store:
        key = key+j.upper()

    encoded = []
    for current in range(len(message)):
        ord_store = ((ord(message[current])-65) + (ord(key[current % len(key)])-65)) % 26
        encoded = encoded + [ord_store]

    output = ""
    for number in encoded:
        output = output + chr(number+65)

    button_text.undraw()
    button_frame.undraw()
    resulting_message = Text(Point(200, 200), "Resulting Message")
    output_display = Text(Point(200, 180), output)
    resulting_message.draw(win)
    output_display.draw(win)
    close_prompt = Text(Point(200, 20), "Click Anywhere to Close Window")
    close_prompt.draw(win)
    win.getMouse()
    win.close()
    

vigenere()
