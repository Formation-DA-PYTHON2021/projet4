from tinydb import TinyDB, Query, where
db = TinyDB("./mvc/db.json")

tournament_db = db.table('tournament_db')


class Tournament:
    def __init__(self, name, site, start_date, end_date,
                 description_tournament, number_round=4,
                 tournament_id=0):
        self.name = name
        self.site = site
        self.start_date = start_date
        self.end_date = end_date
        self.description_tournament = description_tournament
        self.number_round = number_round
        self.tournament_id = tournament_id
        self.instances_match = []
        self.instance_playeurs = []


    def choose_time (self, bullet, blitz, coup_rapide):
        self.bullet = bullet
        self.blitz = blitz
        self.coup_rapide = coup_rapide

    def serialized(tournament):
        serialized_tournament = {
            'name': tournament.name,
            'site': tournament.site,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'description_tournament': tournament.description_tournament,
            'number_round': tournament.number_round,
            'tournament_id': tournament.tournament_id
        }
        return serialized_tournament

    def add(tournament):
        serialized_tournament = {
            'name': tournament.name,
            'site': tournament.site,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'description_tournament': tournament.description_tournament,
            'number_round': tournament.number_round,
            'tournament_id': tournament.tournament_id
        }

        tournament_db.insert(serialized_tournament)

        print(tournament_db)



    def update(tournament):
        tournament_id = tournament_db.insert(tournament.serialized())
        tournament_db.update({'Id du tournois': tournament_id}, doc_ids=[tournament_id])


    def __str__(self):
        return f"{self.name}, {self.site}"
