import csv
from package import Package
# from functions import sort

truck1_unsorted = []
truck1_sorted = []
truck1_distance = 0
truck2_unsorted = []
truck2_sorted = []
truck2_distance = 0
truck3_unsorted = []
truck3_sorted = []
truck3_distance = 0
distanceData = []

# -The csv reader below has a single loop, giving it 0(N) time complexity
# -next(csv_reader) is called twice to pass over header rows in the csv file
# -The for loop appends new Package objects to the respective truck lists (instantiated above), converting the data from
# a csv to objects usable by the program
# csv 0id, 1address, 2city, 3state, 4zip, 5deadline, 6weight, 7notes, 8truck
# cla id, address, city, zip, weight, status, truck, deliveryDeadline=None, deliveryTime=None, specialNotes=None
# 4001 South 700 East,
# Salt Lake City, UT 84107
# don't need address in package, set it up based on id, create new object to return index
with open('WGUPS_Package_File.csv') as package_file:
    csv_reader = csv.reader(package_file, delimiter=',')
    next(csv_reader)
    next(csv_reader)
    # truck1_unsorted.append(Package(0, "4001 South 700 East", "Salt Lake City", 84107, 0, "Hub", 0, 1))
    # truck2_unsorted.append(Package(0, "4001 South 700 East", "Salt Lake City", 84107, 0, "Hub", 0, 1))
    # truck3_unsorted.append(Package(0, "4001 South 700 East", "Salt Lake City", 84107, 0, "Hub", 0, 1))
    # truck1_sorted.append(Package(0, "4001 South 700 East", "Salt Lake City", 84107, 0, "Hub", 0, 1))
    # truck2_sorted.append(Package(0, "4001 South 700 East", "Salt Lake City", 84107, 0, "Hub", 0, 1))
    # truck3_sorted.append(Package(0, "4001 South 700 East", "Salt Lake City", 84107, 0, "Hub", 0, 1))
    for row in csv_reader:
        if int(row[8]) == 1:
            truck1_unsorted.append(
                Package(row[0], row[1], row[2], row[4], row[6], "At Hub", row[8], row[5], None, row[7], row[9]))
        elif int(row[8]) == 2:
            truck2_unsorted.append(
                Package(row[0], row[1], row[2], row[4], row[6], "At Hub", row[8], row[5], None, row[7], row[9]))
        else:
            truck3_unsorted.append(
                Package(row[0], row[1], row[2], row[4], row[6], "At Hub", row[8], row[5], None, row[7], row[9]))


# -The csv reader below contains a single loop, giving it O(N) time complexity
# -distanceData is a list that holds the distance table data, allowing the algorithm to discover the closest address
# for each package
with open('WGUPS_Distance_Table.csv') as distance_file:
    csv_reader = csv.reader(distance_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        # separate the distances from the addresses, create a separate object that correlates the address and location
        distanceData.append(row[1:])
    # convert values in distanceData to floats
    for row in distanceData:
        for i in range(0, len(row)):
            row[i] = float(row[i])


def sort(list):
    listCopy = list
    # initialize current address, copy of list (advance past hub), shortest
    currentAddress = 0
    nextAddress = list[0].addressId
    length = len(list)
    # for each row in the list that needs sorting, run the sort algorithm
    for i in range(length):
        nextAddress = getShortest(currentAddress, nextAddress, listCopy)
        # listCopy.remove(currentAddress)
        shortest = getDistance(int(currentAddress), int(nextAddress))
        addToSortedList(nextAddress, shortest, list)
        currentAddress = nextAddress
    for item in truck1_sorted:
        print("Id: " + str(item.addressId))


def getShortest(currentAddress, nextAddress, list):
    shortest = 100.1
    i = 0
    length = len(list)
    while i < length:
        # call getDistance with currentAddress and the item.get_addressId() as params
        distance = getDistance(int(currentAddress), int(list[i].addressId))
        # compare distance to 0 and shortest (0 meaning self, shortest meaning current shortest address
        if 0.0 < float(distance) < shortest:
            shortest = distance
            nextAddress = list[i].addressId
        i += 1
    return nextAddress


def addToSortedList(addressId, shortest, list):
    global truck1_distance
    global truck2_distance
    global truck3_distance
    for item in list:
        if item.addressId == addressId:
            if int(item.get_truck()) == 1:
                truck1_sorted.append(item)
                truck1_distance += shortest
            elif int(item.get_truck()) == 2:
                truck2_sorted.append(item)
                truck2_distance += shortest
            else:
                truck3_sorted.append(item)
                truck3_distance += shortest


def getDistance(addressOne, addressTwo):
    return distanceData[addressOne][addressTwo]


sort(truck1_unsorted)
# sort(truck2_unsorted)
# sort(truck3_unsorted)


