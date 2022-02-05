from tinydb import TinyDB

db = TinyDB("./mvc/db.json")
tournament_db = db.table('tournament_db')



class Tournament:
    def __init__(self, name, site, start_date, end_date,
                 description_tournament, choose_time, assign_player, number_round=4, isend=False):
        self.name = name
        self.site = site
        self.start_date = start_date
        self.end_date = end_date
        self.description_tournament = description_tournament
        self.choose_time = choose_time
        self.assign_player = assign_player
        self.number_round = number_round
        self.isend = isend
        self.instances_rounds = []
        self.instances_match = []
        self.instance_players = []

    def serialized(tournament):
        serialized_tournament = {
            'name': tournament.name,
            'site': tournament.site,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'description_tournament': tournament.description_tournament,
            'choose_time': tournament.choose_time,
            'assign_player': tournament.assign_player,
            'number_round': tournament.number_round,
            'isend': tournament.isend
        }
        return serialized_tournament

    def add(tournament):
        serialized_tournament = {
            'name': tournament.name,
            'site': tournament.site,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'description_tournament': tournament.description_tournament,
            'choose_time': tournament.choose_time,
            'assign_player': tournament.assign_player,
            'number_round': tournament.number_round,
            'isend': tournament.isend
        }

        tournament_db.insert(serialized_tournament)

        print(db)


    def update(tournament):
        tournament_id = tournament_db.insert(tournament.serialized())
        tournament_db.update({'Id du tournois': tournament_id}, doc_ids=[tournament_id])

    def addMatch(self, match):
        self.instances_match.append(match)

    def __str__(self):
        return f"{self.name}, {self.site}"

class Round:
    def __init__(self, name=None, begin_time=None, end_time=None,
                     list_score_matchs=None):
        self.name = name
        self.begin_time = begin_time
        self.end_time = end_time
        self.list_score_matchs = list_score_matchs
        self.instances_rounds = []

class Match:
    pass
