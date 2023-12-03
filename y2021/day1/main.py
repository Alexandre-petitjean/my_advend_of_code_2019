# coding=utf-8
import os

from year_2021.tools import open_file_line_by_line, list_str_to_int


def calc_nb_augmentation(sonar_inputs, val_initial):
    val_pre = val_initial
    aug_cpt = 0

    for sonar_input in sonar_inputs:
        if sonar_input > val_pre:
            aug_cpt += 1
        val_pre = sonar_input
    return aug_cpt


def calc_nb_augmentation_by_groupe(sonar_inputs):
    new_sonars = []
    for i in range(len(sonar_inputs)):
        new_sonars.append(sum(sonar_inputs[i:i+3]))

    return calc_nb_augmentation(new_sonars, sum(sonar_inputs[0:3]))


def main():
    sonar_inputs = open_file_line_by_line('input.txt')
    list_str_to_int(sonar_inputs)
    print(calc_nb_augmentation(sonar_inputs, sonar_inputs[0]))  # 1233
    print(calc_nb_augmentation_by_groupe(sonar_inputs))  # 1275


if __name__ == '__main__':
    main()