from tinydb import TinyDB, Query, where
db = TinyDB("./mvc/db.json")

tournament_db = db.table('tournament_db')



class Tournament:
    def __init__(self, name, site, start_date, end_date,
                 description_tournament, choosetime, assignplayer, number_round=4):
        self.name = name
        self.site = site
        self.start_date = start_date
        self.end_date = end_date
        self.description_tournament = description_tournament
        self.choosetime = choosetime
        self.assignplayer = assignplayer
        self.number_round = number_round
        self.instances_match = []
        self.instance_players = []


    def serialized(tournament):
        serialized_tournament = {
            'name': tournament.name,
            'site': tournament.site,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'description_tournament': tournament.description_tournament,
            'choosetime': tournament.choosetime,
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
            'number_round': tournament.number_round,
        }

        tournament_db.insert(serialized_tournament)

        print(tournament_db)



    def update(tournament):
        tournament_id = tournament_db.insert(tournament.serialized())
        tournament_db.update({'Id du tournois': tournament_id}, doc_ids=[tournament_id])


    def __str__(self):
        return f"{self.name}, {self.site}"


    def addplayer(self):
        nouveau = ViewPlayer.info(self)
        nouveauplayer = tournament.update(nouveau)


    def showlistplayer(self):
            for k, Player in enumerate(player_db):
                print("[",k,"]", Player)
            choosenameplayer=int(input("Entrez le numéro du joueur : "))
            return choosenameplayer
