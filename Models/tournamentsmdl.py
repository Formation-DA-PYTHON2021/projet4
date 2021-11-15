

class Tournament:
    def __init__(self, name, site, start_date, end_date, number_round=4):
        tournament = Tournament(name,site,start_date,end_date,number_round)
        serialized_tournament = {
            'name': tournament.name,
            'site': tournament.site,
            'start_date':tournament.start_date,
            'end_date':tournament.end_date,
            'number_round': tournament.number_round
        }
        self.name = serialized_tournament['name']
        self.site = serialized_tournament['site']
        self.start_date = serialized_tournament['start_date']
        self.end_date = serialized_tournament['end_date']
        self.number_round = serialized_tournament['number_round']

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
