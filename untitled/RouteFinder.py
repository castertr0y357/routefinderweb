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

    def find_distance(self, point1, point2):
        result = distance(point1, point2, units="imperial")
        point2.value = result
        return point2.value

    def max_find(points):
        largest = Point("", 0)
        for x in points:
            if x.value > largest.value:
                largest = x
        return largest


pointa = Point("123 somewhere", 1)
pointb = Point("456 somewhere", 2)

arr = [pointa, pointb]
print("Initial Array  :",)
biggest = Point.max_find(arr)
print(biggest.address)

