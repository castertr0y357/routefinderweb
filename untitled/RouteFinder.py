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
        largest = Point("")
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
        for x in map_order:
            if x == "":
                pass
            else:
                print(str(counter) + ": " + x.address)
                #print(x.address)
                counter += 1
        return

    @staticmethod
    def create_route():
        center = int(map_order.__len__() / 2) - 1
        left = center - 1
        right = left + 1
        left_open = True
        right_open = True

        Point.create_points(input_points)

        # find furthest point

        for x in map_points:
            Point.find_distance(home, x)

        map_order[center] = Point.find_max(map_points)
         # = max_point
        #test_order[center] = max_point.address

        # remove furthest point and add home into map points

        map_points.remove(map_order[center])
        map_points.append(home)

        reference = center

        print(test_order)

        # find left and right points

        for x in range(map_points.__len__()):
            if left_open and right_open:  # If both left and right side do not have home as a point

                # find distances from reference

                for y in map_points:
                    Point.find_distance(map_order[reference], y)

                min_point = Point.find_min(map_points)
                print(min_point.address)

                # if right point is closer, set right point

                if Point.find_distance(min_point, map_order[right]) < min_point.value:
                    right += 1
                    reference = right
                    map_order[right] = min_point
                    test_order[right] = min_point.address
                    map_points.remove(min_point)  # remove the minimum point from the map_points list

                    if min_point == home:
                        map_order.remove(min_point)  # remove home from map order
                        right_open = False  # close the right side of the map_order list

                else:  # Set the point on the left side
                    map_order[left] = min_point
                    test_order[left] = min_point.address
                    map_points.remove(min_point)
                    reference = left
                    left -= 1

                    if min_point == home:
                        map_order.remove(min_point)  # remove home from map order
                        left_open = False  # close the left side of the map order list

            elif left_open:  # if left side only is open

                for y in map_points:
                    Point.find_distance(map_order[reference], y)

                min_point = Point.find_min(map_points)
                print(min_point.address)
                map_order[left] = min_point
                test_order[left] = min_point.address
                map_points.remove(min_point)
                reference = left
                left -= 1

            else:  # if right side only is open

                for y in map_points:
                    Point.find_distance(map_order[reference], y)

                min_point = Point.find_min(map_points)
                print(min_point.address)
                right += 1
                reference = right
                map_order[right] = min_point
                test_order[right] = min_point.address
                map_points.remove(min_point)

            print(test_order)

        Point.print_points()  # Print out the points for the user.


pointa = "12677 newfield drive orlando fl 32837"
pointb = "3030 slater rd morrisville nc 27560"
pointc = "2079 longhunter chase dr spring hill tn"
pointd = "4500 the woods drive san jose ca 95136"

home = Point("141 daneborg rd durham nc 27703")

input_points = [pointa, pointb, pointc, pointd]
map_points = []
map_order = [""] * (input_points.__len__() * 2)
test_order = map_order
Point.create_route()

"""furthest = Point.find_max(arr)
#closest = Point.find_min(arr)
#print(furthest.address)
#print(closest.address)
Point.create_points(input_points)
print(map_points[1].address)
Point.find_distance(map_points[0], map_points[1])
print(map_points[1].value)"""

