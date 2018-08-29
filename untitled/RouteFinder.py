import googlemaps
gapi = "AIzaSyC2mfL58CI4oSI31dB9afbJZ5EN_wDQirg"
gmaps = googlemaps.Client(key=gapi)
distance = gmaps.distance_matrix


class Point:
    address = ""
    value = 0

    def __init__(self, address):
        self.address = address
        self.value = 0

    @staticmethod
    def find_distance(point1, point2):
        result = distance(point1.address, point2.address, units="imperial")
        point2.value = result["rows"][0]["elements"][0]["duration"]["value"]  # Value in seconds
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

    @staticmethod
    def print_points():
        counter = 1
        for x in map_points:
            if x == "":
                pass
            else:
                print(counter + " : ")
                print(x.address)
        return

    @staticmethod
    def create_route():
        center = (map_order.__len__() / 2) - 1
        reference = center
        left = reference - 1
        right = left + 1
        left_open = True
        right_open = True

        Point.create_points(input_points)

        # find furthest point

        for x in map_points:
            Point.find_distance(home, x)
        map_order[center] = Point.find_max(map_points)

        # remove furthest point and add home into map points

        map_points.remove(map_order[center])
        map_points.append(home)

        # find left and right points

        for x in map_points.__len__():
            if left_open and right_open:

                # find distances from reference

                for y in map_points:
                    Point.find_distance(reference, y)

                min_point = Point.find_min(map_points)

                # if right point is closer, set right point

                if Point.find_distance(min_point, map_order[right]) < min_point.value:
                    right += 1
                    map_order[right] = min_point

                    if min_point == home:
                        right_open = False
                else:
                    map_order[left] = min_point
                    left -= 1

                    if min_point == home:
                        left_open = False

            else if left_open:
                





pointa = "12677 newfield drive orlando fl 32837"
pointb = "3030 slater rd morrisville nc 27560"

home = Point("141 daneborg rd durham nc 27703")

input_points = [pointa,pointb]
map_points = []
map_order = [""] * (input_points.__len__() * 2)
Point.create_route()

"""furthest = Point.find_max(arr)
#closest = Point.find_min(arr)
#print(furthest.address)
#print(closest.address)
Point.create_points(input_points)
print(map_points[1].address)
Point.find_distance(map_points[0], map_points[1])
print(map_points[1].value)"""

