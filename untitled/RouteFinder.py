import googlemaps
gapi = "AIzaSyC2mfL58CI4oSI31dB9afbJZ5EN_wDQirg"
gmaps = googlemaps.Client(key=gapi)
distance = gmaps.distance_matrix
input_points = [""] * 20
map_points = []
map_order = []


class Point:
    address = ""
    value = 0

    def __init__(self, address):
        self.address = address
        self.value = 0

    @staticmethod
    def find_distance(point1, point2):
        result = distance(point1.address, point2.address, units="imperial")
        point2.value = result["rows"][0]["elements"][0]["duration"]["value"]  #Value in seconds
        return point2.value

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

    @staticmethod
    def create_points(points_list):
        for x in points_list:
            map_points.append(Point(x))
        return


pointa = "141 daneborg rd durham nc 27703"
pointb = "3030 slater rd morrisville nc 27560"

input_points[10] = pointb
"""furthest = Point.find_max(arr)
#closest = Point.find_min(arr)
#print(furthest.address)
#print(closest.address)
Point.create_points(input_points)
print(map_points[1].address)
Point.find_distance(map_points[0], map_points[1])
print(map_points[1].value)"""

print(input_points)

