#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SVL 2016
TP calendrier
Auteur: Honore Nintunze, Antonin Durey

Classes
"""

import unittest

from hypothesis import given, assume, example, settings
from hypothesis.strategies import integers

from calendrier import *

class TestCalendrier(unittest.TestCase):


    @given(annee=integers(min_value=1582))
    def test_annee_bissextile_annee_suivante_ne_l_est_pas(self, annee):
        calendrier = Calendrier()

        self.assertTrue(not (calendrier.est_bissextile(annee) and calendrier.est_bissextile(annee+1)))

    @given(annee=integers(min_value=1582))
    def test_annee_bissextile_annee_plus_4_l_est_aussi_sauf_si_modulo_100(self, annee):

        calendrier = Calendrier()
        bissextile_annee = calendrier.est_bissextile(annee)
        bissextile_annee_plus_4 = calendrier.est_bissextile(annee+4)
        modulo_annee_plus_4 = (annee+4)%100 == 0

        # self.assertTrue(not (bissextile_annee and (bissextile_annee_plus_4 or modulo_annee_plus_4)))


    @given(mois=integers(min_value=0, max_value=11), annee=integers(min_value=1582))
    def test_mois_30_jours_suivant_31_jours(self, mois, annee):
        calendrier = Calendrier()

        self.assertTrue(not (calendrier.nb_jours(mois, annee) == 30 and calendrier.nb_jours(mois+1, annee) != 31))


    @given(mois=integers(min_value=0, max_value=11), annee=integers(min_value=1582))
    def test_mois_30_jours_precedant_31_jours(self, mois, annee):
        calendrier = Calendrier()

        self.assertTrue(not (calendrier.nb_jours(mois, annee) == 30 and calendrier.nb_jours(mois-1, annee) != 31))




    @given(jour=integers(min_value=1,max_value=31),mois=integers(min_value=0, max_value=11), annee=integers(min_value=1582))
    def test_date_valide_alors_date_avec_31_jours_de_plus_pas_valide_et_pareil_pour_mois_plus_12(self, jour,mois, annee):
        calendrier = Calendrier()

        self.assertTrue(not (calendrier.date_valide(jour,mois, annee) and calendrier.date_valide(jour+31,mois, annee)))
        self.assertTrue(not (calendrier.date_valide(jour,mois, annee) and calendrier.date_valide(jour,mois+12, annee)))

    @given(jour=integers(min_value=1,max_value=31),mois=integers(min_value=0, max_value=11), annee=integers(min_value=1582))
    @settings(max_examples=800)
    def test_jour_semaine_plus_1_ou_moins_1_quand_date_plus_1_jour_ou_date_moins_1_jour(self, jour,mois, annee):
        calendrier = Calendrier()

        assume(calendrier.date_valide(jour, mois, annee))
        assume(calendrier.date_valide(jour+1, mois, annee))
        assume(calendrier.date_valide(jour-1, mois, annee))


        self.assertEqual((calendrier.jour_semaine(jour,mois, annee)+1)%7, (calendrier.jour_semaine(jour+1,mois, annee))%7)
        self.assertEqual((calendrier.jour_semaine(jour,mois, annee)-1)%7, (calendrier.jour_semaine(jour-1,mois, annee))%7)
