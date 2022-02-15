import copy

from year_2021.tools import open_file_line_by_line


class Plateau:

    def __init__(self, liste_case) -> None:
        super().__init__()
        self.cases = {}
        for case in liste_case:
            self.cases[int(case)] = '0'
        self.nb_pion = 0

    def est_dans_plateau(self, nombre):
        if nombre in self.cases.keys():
            return True
        else:
            return False

    def ajoute_pion(self, nombre):
        if self.est_dans_plateau(nombre):
            self.cases[nombre] = '*'
            self.nb_pion += 1

    def bingo_ligne(self):
        indexs = [[0, 5], [5, 10], [10, 15], [15, 20], [20, 25]]

        for index in indexs:
            ligne = list(self.cases.values())[index[0]:index[1]]
            if '*' in ligne and ligne.count('*') == 5:
                return True
        return False

    def bingo_col(self):
        for i in range(5):
            compt = 0
            for j in range(5):
                if list(self.cases.values())[i + (j*5)] == '*':
                    compt += 1
            if compt == 5:
                return True
        return False

    def is_bingo(self):
        if self.nb_pion >= 5:
            if self.bingo_ligne() or self.bingo_col():
                return True
        return False

    def get_somme_cases_vide(self):
        somme = 0
        for k, v in self.cases.items():
            if v == '0':
                somme += k
        return somme

    def __str__(self) -> str:
        return f'Nb de pion : {self.nb_pion}, Somme des cases : {self.get_somme_cases_vide()}'


def get_plateaux(lignes):
    les_plateaux = []
    for i in range(0, len(lignes), 6):
        cases = []
        for j in range(5):
            cases += (lignes[i + j].split())
        les_plateaux.append(Plateau(cases))
    return les_plateaux


def partie(les_plateaux, tirage):
    for num in tirage:
        for plateau in les_plateaux:
            plateau.ajoute_pion(num)
            if plateau.is_bingo():
                return plateau.get_somme_cases_vide() * num


def dernier_a_gagner(les_plateaux, tirage):
    gagnants = []
    result = []
    for num in tirage:
        for plateau in les_plateaux:
            plateau.ajoute_pion(num)
            if plateau.is_bingo() and plateau not in gagnants:
                gagnants.append(plateau)
                result.append(plateau.get_somme_cases_vide() * num)
    return result[-1]


def main():
    lignes = open_file_line_by_line('input.txt')
    tirage = [int(val) for val in lignes[0].split(',')]
    les_plateaux = get_plateaux(lignes[2:])

    print('--- part 1 ---')
    print(partie(les_plateaux, tirage))
    print('--- part 2 ---')
    print(dernier_a_gagner(les_plateaux, tirage))


if __name__ == '__main__':
    main()
