from tinydb import TinyDB

db = TinyDB("./mvc/db.json")
tournament_db = db.table('tournament_db')


class Tournament:
    def __init__(self, name, site, start_date, end_date,
                 description_tournament, choose_time, assign_player,
                 instances_rounds, playerdb_tourna, number_round=4):
        self.name = name
        self.site = site
        self.start_date = start_date
        self.end_date = end_date
        self.description_tournament = description_tournament
        self.choose_time = choose_time
        self.assign_player = assign_player
        self.instances_rounds = instances_rounds
        self.playerdb_tourna = playerdb_tourna
        self.number_round = number_round

    def serialized(tournament):
        serialized_tournament = {
            'name': tournament.name,
            'site': tournament.site,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'description_tournament': tournament.description_tournament,
            'choose_time': tournament.choose_time,
            'assign_player': tournament.assign_player,
            'instances_rounds': tournament.instances_rounds,
            'playerdb_tourna': tournament.playerdb_tourna,
            'number_round': tournament.number_round
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
            'instances_rounds': tournament.instances_rounds,
            'playerdb_tourna': tournament.playerdb_tourna,
            'number_round': tournament.number_round
        }
        tournament_db.insert(serialized_tournament)
        print(db)

    def update(tournament):
        tournament_id = tournament_db.insert(tournament.serialized())
        tournament_db.update({'Id du tournois': tournament_id}, doc_ids=[tournament_id])

    def __str__(self):
        return f"{self.name}, {self.site}"
