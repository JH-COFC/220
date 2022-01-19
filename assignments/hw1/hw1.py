"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)




def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length*width*height
    print("Volume =",volume)




def shooting_percentage():
    totalshots = eval(input("Enter the player's total shots: "))
    madeshots = eval(input("Enter the number of shots the player made: "))
    percentmade = (madeshots/totalshots) * 100
    print("Shooting Percentage: ",percentmade,"%")




def coffee():
    pounds = (eval(input("How many pounds of coffee would you like?")))
    cost = (pounds*10.50)+(pounds*0.86)+1.50
    print("Your total is: ",cost)


def kilometers_to_miles():
    kilometers = eval(input("How many kilometers did you travel?"))
    miles = kilometers / 1.61
    print("That's ",miles,"miles!")


kilometers_to_miles()

if __name__ == '__main__':
    pass
