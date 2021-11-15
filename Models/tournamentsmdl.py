

class Tournament:
    def __init__(self, name, site, start_date, end_date, number_round=4):
        self.name = name
        self.site = site
        self.start_date = start_date
        self.end_date = end_date
        self.number_round = number_round

    def choose_time (self, bullet, blitz, coup_rapide):
        self.bullet = bullet
        self.blitz = blitz
        self.coup_rapide = coup_rapide

    def instances_match(self):
        pass # ??

    def instance_playeurs(self):
        pass # ??

    def description_tournament (self):
        pass# doit pouvoir inclure du texte par l'utilisateur

    def __str__(self):
        return f"{self.name}, {self.site}"
