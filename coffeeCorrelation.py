import csv
import numpy as np

def getData(dataPath):
    amount_of_Coffee = []
    hoursOfSleep = []

    with open(dataPath) as csv_file:
        dataFrame = csv.DictReader(csv_file)

        for row in dataFrame:
            amount_of_Coffee.append(float(row["Coffee In ml"]))
            hoursOfSleep.append(float(row["sleep in hours"]))

    return {"x": amount_of_Coffee, "y": hoursOfSleep}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("")
    print("Correlation between hours Of Sleep and amout of coffee is: ",correlation[0,1])

    if (correlation[0,1] < 0 and correlation[0,1] > -1):
        print("You need to drink less coffee so that")
        print("you can sleep enough and maintain your health")
        print("")
    elif (correlation[0,1] < 1 and correlation[0,1] > 0):
        print("You are drinking a perfect amount of coffee")
        print("")
    else:
        print("Error")


def main():
    dataPath = './coffeeData.csv'

    dataSource = getData(dataPath)
    findCorrelation(dataSource)

main()