import googlemaps,json,heapq
gapi = "AIzaSyC2mfL58CI4oSI31dB9afbJZ5EN_wDQirg"
gmaps = googlemaps.Client(key=gapi)
distance = gmaps.distance_matrix
final_list = []


class Point:
    address = ""
    value = 0

    def __init__(self, address, value):
        self.address = address
        self.value = value

    @staticmethod
    def find_distance(point1, point2):
        result = distance(point1.address, point2.address, units="imperial")
        return result

    @staticmethod
    def find_max(points):
        largest = Point("", 0)
        for x in points:
            if x.value > largest.value:
                largest = x
        return largest

    @staticmethod
    def find_min(points):
        smallest = Point.find_max(points)
        for x in points:
            if x.value < smallest.value:
                smallest = x
        return smallest

    #@staticmethod


pointa = Point("123 somewhere", 3)
pointb = Point("456 somewhere", 2)

arr = [pointa, pointb]
furthest = Point.find_max(arr)
closest = Point.find_min(arr)
print(furthest.address)
print(closest.address)

