import googlemaps,json
from MaxHeap import *
gapi = "AIzaSyC2mfL58CI4oSI31dB9afbJZ5EN_wDQirg"
gmaps = googlemaps.Client(key=gapi)
distance = gmaps.distance_matrix


class Point:
    address = ""
    value = 0

    def __init__(self, address, value):
        self.address = address
        self.value = value

    def findDistance(self, point1, point2):
        result = distance(point1, point2, units="imperial")
        point2.value = result
        return point2.value


arr = [9, 4, 8, 3, 1, 2, 5]
print("Initial Array  :",)
MaxHeap.heapsort(arr)
MaxHeap.printArray(arr)
print("After Sorting  :",)
MaxHeap.printArray(arr)
