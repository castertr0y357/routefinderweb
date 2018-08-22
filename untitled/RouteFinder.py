import googlemaps,json,heapq
gapi = "AIzaSyC2mfL58CI4oSI31dB9afbJZ5EN_wDQirg"
gmaps = googlemaps.Client(key=gapi)
distance = gmaps.distance_matrix


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
        return heapq.nlargest(1, points, Point.value)


arr = [9, 4, 8, 3, 1, 2, 5]
print("Initial Array  :",)
print(arr)
arr = Point.max_find(arr)
print("After Sorting  :",)
print(arr)
