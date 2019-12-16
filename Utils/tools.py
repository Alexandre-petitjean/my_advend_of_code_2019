import os


def open_file_line_by_line(filename):
    my_list = []
    if os.path.exists(filename):
        with open(filename) as fp:
            line = fp.readline()
            while line:
                my_list.append(line)
                line = fp.readline()
        return my_list


def open_file_explode_array(filename):
    if os.path.exists(filename):
        with open(filename) as fp:
            line = fp.readline()
            my_list = line.split(',')
        return my_list
