"""
Day 3 of the avent of code.
--- Day 3: Crossed Wires ---
"""
from Utils.tools import open_file_explode_array_line_by_line

# Constant
FILENAME = "input_day_3.txt"

RIGHT = 'R'
LEFT = 'L'
UP = 'U'
DOWN = 'D'


def main():
    """
    Main function of the file.
    """
    print("Day 3")

    my_list = open_file_explode_array_line_by_line(FILENAME)
    print("Part 1 : ")
    print(treatment_part1(my_list))
    print("Part 2 : ")
    print(treatment_part2(my_list))


def treatment_part1(my_list):
    """
    Treatement of the part 1.
    :param my_list: The input.
    :return: The part 1 answer.
    """
    wire_path = treatment(my_list)
    intersection = find_intersection(wire_path)
    return manhattan_calcul(intersection)


def treatment_part2(my_list):
    """
    Treatment of the part 2.
    :param my_list: The input.
    :return: The part 2 answer.
    """
    wires_path = treatment(my_list)
    intersection = find_intersection(wires_path)
    return fewest_step(wires_path, intersection)


def treatment(my_list):
    """
    Principal treatment.
    :param my_list: The input.
    :return: The path of the two wires.
    """
    wires_path = [[], []]
    for wire in my_list:
        x = 0
        y = 0
        one_wire_path = []
        for element in wire:
            # Wire direction.
            first_letter = element[0]
            # Distance to run.
            iteration = int(element[1:])
            one_wire_path = calcul_path(first_letter, iteration, x, y, one_wire_path)
            if first_letter == RIGHT:
                x = x + iteration
            elif first_letter == LEFT:
                x = x - iteration
            elif first_letter == UP:
                y = y + iteration
            else:
                y = y - iteration
        wires_path[my_list.index(wire)] = one_wire_path
    return wires_path


def calcul_path(direction, iteration, x, y, one_wire_path):
    """
    Calculation of the wire path.
    Return each coordinate of the wire path.
    :param direction: The wire direction.
    :param iteration: The number of square of the wire path.
    :param x: The actual x coordinate of the wire.
    :param y: The actual y coordinate of the wire.
    :param one_wire_path: The list of each coordinate of the wire path.
    :return: A string with the coordinate x;y of the wire separate with a comma.
    """
    y_str = str(y)
    x_str = str(x)
    if len(one_wire_path) > 0:
        one_wire_path = one_wire_path[:-1]

    if direction == RIGHT:
        target = x + iteration
        while x <= target:
            one_wire_path.append(str(x) + ";" + y_str)
            x = x + 1
    elif direction == LEFT:
        target = x - iteration
        while x >= target:
            one_wire_path.append(str(x) + ";" + y_str)
            x = x - 1
    elif direction == UP:
        target = y + iteration
        while y <= target:
            one_wire_path.append(x_str + ";" + str(y))
            y = y + 1
    else:
        target = y - iteration
        while y >= target:
            one_wire_path.append(x_str + ";" + str(y))
            y = y - 1
    return one_wire_path


def find_intersection(wire_path):
    """
    Find the coordinate of intersection of the two wire.
    :param wire_path: List of coordinate of the wires path.
    :return: The list of intersection coordinate.
    """
    # Delete the first index of each list.
    first_wire = wire_path[0][1:]
    second_wire = wire_path[1][1:]
    # compare the elememt of each list.
    # return the list of similar element.
    return set(first_wire).intersection(second_wire)


def manhattan_calcul(intersection):
    """
    Calcul of Manhattan distance.
    https://en.wikipedia.org/wiki/Taxicab_geometry
    :param intersection: List of coordinate.
    :return: The manhattan distance of the shortest intersection point.
    """
    result: int = None
    for element in intersection:
        position = element.split(";")
        x = abs(int(position[0]))
        y = abs(int(position[1]))
        calcul = x + y
        if result is None or result > calcul:
            result = calcul
    return result


def fewest_step(wires_path, intersections):
    """
    Calcul the fewest step to an intersection.
    :param wires_path: the path of the wires.
    :param intersections: the coordinate of the intersections.
    """
    result: int = None
    for coordinate in intersections:
        step = 0
        for path in wires_path:
            i = 0
            while coordinate != path[i]:
                i = i + 1
            step += i
        if result is None or result > step:
            result = step
    return result


if __name__ == "__main__":
    main()
