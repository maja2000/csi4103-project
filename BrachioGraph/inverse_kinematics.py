# This file goes over some of the mathematics needed to calibrate the brachiograph, such as calculating angles

from math import sqrt, acos, degrees


# This gives the absolute length from the origin to the specified point
# The inputs are lists, the first one is the origin (where the base of the bracchiograph is),
# and the second is the destination (where the point is)
def pythagorean(origin, destination):
    # These variables are the coordinates, broken down
    x_0 = origin[0]
    y_0 = origin[1]
    x_1 = destination[0]
    y_1 = destination[1]
    return sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)


# This is the Law of Cosines, it gives one of the angles of a triangle based on the lengths of the three sides
# The inputs are lengths of the triangle's arms and the output is an internal angle, either in radians or degrees
# The default output will be in degrees
def coleslaw(opposite, adjacent1, adjacent2, radians_true=False):
    # Calculate the parts of the equation separately for ease
    numerator = adjacent1 ** 2 + adjacent2 ** 2 - opposite ** 2
    denominator = 2 * adjacent1 * adjacent2
    radians_answer = acos(numerator / denominator)
    if radians_true:
        return radians_answer
    else:
        return degrees(radians_answer)

