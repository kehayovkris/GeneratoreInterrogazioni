import random

from Classe import *

"""
    :attr __classe: enum che gestisce la __classe di appartenenza 
    :attr __l: lista che contiene gli alunni di una determinata __classe
    :attr __tab: lista di liste che contiene i gruppi di interrogazione
        """
class Generatore:
    __classe: Class = ""
    __l = []
    __tab=[]

    """
    costruttore che inizializza __l'oggetto 
    :param __classe: enum che gestisce la __classe di appartenenza 
    """
    def __init__(self, classe: Class):
        self.__tab = []
        self.__classe: Class = classe
        if self.__classe == Class.QUARTA_F:
            self.popula("quartaF" if self.__classe == Class.QUARTA_F else "quartaMI")
        elif self.__classe == Class.QUARTA_MI:
            self.popula("quartaMI")

    """
    funzione che inizializza la lista __l[] prendendo i valori da un file 
    :param path: percorso relativo del file contenente gli studenti 
    """
    def popula(self, path: str) :
        self.__l.clear()
        with open(path, "r") as file:
            for line in file:
                self.__l.append(line.split(" "))

    """
    funzione che genera la lista di liste contenete la __classe suddivisa in gruppi 
    """
    def genera(self):
        random.shuffle(self.__l)

        # self.__tab = [self.__l[x:x + 5]    for x in range(0, len(self.__l), 5)] ##for brutto

        for x in range(0, len(self.__l), 5):
            self.__tab.append(self.__l[x:x + 5])

        for i in self.__tab:
            print(i)

    """
    funzione get() per gli attributi: tab[],l[] e classe
    """
    def tab(self):
        return self.__tab
    def l(self):
        return self.__l
    def classe(self):
        return self.__classe
