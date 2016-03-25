# CTD9 SVL - M. Nebut - 03/2016
# property-based testing
"""
SVL 2016
TP banque
Auteur: Honore Nintunze, Antonin Durey

Classes
"""
class Compte:

    def __init__(self):
        self.montant = 0

    def crediter(self, somme):
        if somme <= 0:
            raise ValueError()
        self.montant += somme

    def debiter(self,somme):
        if somme <= 0:
            raise ValueError()
        self.montant -= somme
