import csv
import numpy as np

def getdataSource(dataPath):
    days_present = []
    marks = []

    with open(dataPath) as csv_file:
        dataFrame = csv.DictReader(csv_file)

        for row in dataFrame:
            days_present.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))

    return {"x": days_present, "y": marks}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("")
    print("Correlation between Marks and No.of days present of students is: ",correlation[0,1])

    if (correlation[0,1] < 0 and correlation[0,1] > -1):
        print("Students need to focus more and attend classes properly")
    elif (correlation[0,1] < 1 and correlation[0,1] > 0):
        print("Students are doing good!!")
        print("")
    else:
        print("Error")


def main():
    dataPath = './studentData.csv'

    dataSource = getdataSource(dataPath)
    findCorrelation(dataSource)

main()