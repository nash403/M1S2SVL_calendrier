#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SVL 2016
TP calendrier
Auteur: Honore Nintunze, Antonin Durey

Classes
"""

class Calendrier:

    def __init__(self):
        pass

    def est_bissextile(self, annee):
        return (annee % 400 == 0) or (annee % 4 == 0) and (annee % 100 != 0)

    def nb_jours(self, mois, annee):

        if mois in [0, 2, 4, 6, 7, 9, 11]:
            return 31

        if mois in [3, 5, 8, 10]:
            return 30

        # Plus que fevrier possible

        if self.est_bissextile(annee):
            return 29

        return 28

    def date_valide(self,jour,mois,annee):
        if jour < 1 or jour > self.nb_jours(mois, annee):
            return False

        if mois < 0 or mois > 11:
            return False

        return True

    def jour_semaine(self,jour,mois,annee):
        ab = annee // 100
        cd = annee % 100
        k = cd // 4
        q = ab // 4
        M = [{False : 4, True : 3}, {False : 0, True : 6}, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]

        if mois == 0 or mois == 1:
            m = M[mois][self.est_bissextile(annee)]
        else:
            m = M[mois]

        return (k + q + cd + m + jour + 2 + 5 *ab) % 7
