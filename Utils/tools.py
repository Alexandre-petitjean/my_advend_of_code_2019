import os


def open_file(filename):
    my_list = []
    if os.path.exists(filename):
        with open(filename) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                my_list.append(line)
                line = fp.readline()
        return my_list
