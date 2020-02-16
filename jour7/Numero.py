from enum import Enum


class Numero(Enum):

    ZERO = '0'
    UN = '1'
    DEUX = '2'
    TROIS = '3'
    QUATRE = '4'

    def next(self):
        cls = self.__class__
        members = list(cls)
        index = members.index(self) + 1
        if index >= len(members):
            index = 0
        self.nb_transformation += 1
        return members[index]
