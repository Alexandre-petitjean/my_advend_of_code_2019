from year_2021.tools import open_file_line_by_line


def nettoyage_input(inputs):
    lignes = []
    for input in inputs:
        lignes.append(list(map(int, input.replace('->', ',').split(','))))
    return lignes


def only_hor_and_ver(lignes):
    new_lignes = []
    for ligne in lignes:
        if ligne[0] == ligne[2] or ligne[1] == ligne[3]:
            new_lignes.append(ligne)
    return new_lignes


def get_max(lignes, index1):
    max = 0
    for ligne in lignes:
        if max < ligne[index1]:
            max = ligne[index1]
    return max


def dessine_carte(lignes):
    # Initilization de la carte.
    carte = []
    max_x = max(get_max(lignes, 0), get_max(lignes, 2))
    max_y = max(get_max(lignes, 1), get_max(lignes, 3))
    for i in range(max_y + 1):
        carte.append([0] * (max_x + 1))

    for ligne in lignes:


        if ligne[0] == ligne[2]:  # Vertical carte[i][ligne[0]]
            marque_carte(carte, ligne[1], ligne[3], ligne[0], 'vertical')
        else:  # Horizontal carte[ligne[1]][i]
            marque_carte(carte, ligne[0], ligne[2], ligne[1], 'horizontal')

    return carte


def marque_carte(carte, i, j, ref, type):
    if i > j:
        i, j = j, i

    if type == 'horizontal':
        while i <= j:
            carte[ref][i] += 1
            i += 1
    else:
        while i <= j:
            carte[i][ref] += 1
            i += 1
    return carte


def count_sup_number(carte, number):
    cmpt = 0
    for ligne in carte:
        for elem in ligne:
            if elem >= number:
                cmpt += 1
    return cmpt


def main():
    lignes = open_file_line_by_line('input.txt')
    lignes = nettoyage_input(lignes)
    lignes = only_hor_and_ver(lignes)

    carte = dessine_carte(lignes)

    print(count_sup_number(carte, 2))


if __name__ == '__main__':
    main()
