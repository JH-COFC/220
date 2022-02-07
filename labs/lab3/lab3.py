"Name: Jordan Herder"
"Function gives the average traffic per road, average overall traffic,"
"and total traffic for the surveyed roads and period."


def traffic_pattern():
    roads = eval(input("How many roads were surveyed?"))
    total_cars = 0

    for i in range(1,roads+1):
        cars = 0
        print("How many days was road",i,"surveyed?")
        days = eval(input())
        for j in range(1,days+1):
            print("How many cars traveled on day ",j,"?",sep="")
            cars = cars + eval(input())
        print("Road",i,"average vehicles per day:",cars/days)
        total_cars = total_cars + cars

    print("Total number of vehicles traveled on all roads:",total_cars)
    print("Average number of vehicles per road:",total_cars/roads)


traffic_pattern()

