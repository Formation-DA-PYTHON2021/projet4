

class Tournament :
    def __init__(self, nom, lieu, date_debut, date_fin, nbtour=4,
             tournee, nbjoueur=8, controle_temps, decription):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nbtour = nbtour
        self.tournee = tournee
        self.nbjoueur = nbjoueur
        self.controle_temps = controle_temps
        self.description = decription

    def __str__(self):
        return f"{self.nom} {self.lieu} {self.nbtour} {self.tournee} {self.nbjoueur}" \
               f"{self.controle_temps} {self.description} {self.date_debut} {self.date_fin}"
