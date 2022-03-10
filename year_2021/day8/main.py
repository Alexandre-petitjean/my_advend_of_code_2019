from year_2021.tools import open_file_line_by_line, list_str_to_int


def parse_val_p1(lignes):
    cmpt = 0
    for ligne in lignes:
        output_val = ligne.split('|')[1].split(' ')
        output_val.remove('')
        cmpt += count_value(output_val)
    return cmpt


def parse_val_p2(lignes):
    cmpt = 0
    for ligne in lignes:
        output_val = ligne.split('|')[1].split(' ')
        output_val.remove('')
        cmpt += get_output(output_val)
    return cmpt


def count_value(output_val):
    cmpt = 0
    for val in output_val:
        if len(val) in [2, 3, 4, 7]:
            cmpt += 1
    return cmpt


def get_output(output_val):
    output = ''
    for val in output_val:
        if len(val) in [2, 3, 4, 7]:
            if len(val) == 2:
                output += '1'
            elif len(val) == 3:
                output += '7'
            elif len(val) == 4:
                output += '4'
            elif len(val) == 7:
                output += '8'
        elif len(val) == 5:
            if 'e' in val:
                output += '5'
            elif 'a' in val and 'g' in val:
                output += '2'
            else:
                output += '3'
        else:  # 6
            if 'e' in val:
                output += '6'
            else:
                output += '9'
    return int(output)


def main():
    #  open file and parse list.
    lignes = open_file_line_by_line('./input.txt')
    print(f"Nb values : {parse_val_p1(lignes)}")
    print(f"sum values : {parse_val_p2(lignes)}")


if __name__ == '__main__':
    main()
