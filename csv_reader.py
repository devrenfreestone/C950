import csv
from package import Package
packageList = []

with open('WGUPS_Package_File.csv') as package_file:
    csv_reader = csv.reader(package_file, delimiter=',')
    for row in csv_reader:
        packageList.append(Package(row[0], row[1], "At Hub", row[5], None, row[6]))
    print(packageList)

with open('WGUPS_Distance_Table.csv') as distance_file:
    csv_reader = csv.reader(distance_file, delimiter=',')
    distanceData = []
    distance = 0
    item = 0.1
    delivered = []
    next(csv_reader)
    column = 0
    j = 1
    for row in csv_reader:
        shortest = float(100.0)
        item = float(0.1)
        length = len(row)
        i = 1

        column = 0
        # print(delivered)

        while i < length:
            if i in delivered:
                pass
            elif float(row[i]) != float(0):
                item = float(row[i])
                if item < shortest:
                    shortest = item
                    column = i
            i += 1
        # print("row " + str(j) + ": " + " shortest: " + str(shortest) + " column: " + str(column))
        delivered.append(column)
        distance += shortest
        j += 1

        # print("shortest distance is package: " + str(column) + " which is: " + str(shortest) + " miles away.")
    # for row in distanceData:
    #     while i < row

print(distance)
