"""
Day 3 of the avent of code.
https://adventofcode.com/2019/day/3
Problem : Two wires cross each other, we need to find the closest intersection of wire.
"""
from Utils.tools import open_file_explode_array_line_by_line

# Constant
RIGHT = 'R'
LEFT = 'L'
UP = 'U'
DOWN = 'D'


def main():
    print("Jour 3")
    filename = "input_jour_3.txt"
    my_list = open_file_explode_array_line_by_line(filename)
    # print(treatment_part1(my_list))
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
            # Direction du fil.
            first_letter = element[0]
            # Distance a parcourir.
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
    Calcule Le chemin parcouru par le fil et renvoi les coordonnées de chaque case ou est passé le morceaux fil.
    :param direction: La direction du fil.
    :param iteration: Le nombre de case que le fil a parcouru.
    :param x: La position x actuelle du fil.
    :param y: La position y actuelle du fil.
    :return: Retourne une chaine de caratere, avec les positions x;y du morceaux de fil chaque case est séparé par une virgule.
    """
    result = ""
    y_str = str(y)
    x_str = str(x)
    if len(one_wire_path) > 0:
        one_wire_path = one_wire_path[:-1]

    if direction == RIGHT:
        target = x + iteration
        while x <= target:
            one_wire_path.append(str(x) + ";" + y_str)
            # result += "," + str(x) + ";" + y_str
            x = x + 1
    elif direction == LEFT:
        target = x - iteration
        while x >= target:
            one_wire_path.append(str(x) + ";" + y_str)
            # result += "," + str(x) + ";" + y_str
            x = x - 1
    elif direction == UP:
        target = y + iteration
        while y <= target:
            one_wire_path.append(x_str + ";" + str(y))
            # result += "," + x_str + ";" + str(y)
            y = y + 1
    else:
        target = y - iteration
        while y >= target:
            one_wire_path.append(x_str + ";" + str(y))
            # result += "," + x_str + ";" + str(y)
            y = y - 1
    return one_wire_path


def find_intersection(wire_path):
    """
    Find the coordinate of intersection of the two wire.
    :param wire_path: List of coordinate of the wires path.
    :return: The list of intersection coordinate.
    """
    # On retire le premier element de chaque list qui est 0;0
    first_wire = wire_path[0][1:]
    second_wire = wire_path[1][1:]
    # compare les element de la list fist_wire avec celle de second_wire
    # et retourne une liste des elements qui sont commun aux 2 listes.
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
