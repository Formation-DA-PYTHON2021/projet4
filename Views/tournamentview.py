from ..Models.playermdl import Player
from ..Views.playerview import ViewPlayer
from ..Models.tournamentsmdl import Tournament

from tinydb import TinyDB, Query, where
db = TinyDB("./mvc/db.json")
player_db = db.table('player_db')


class ViewTournament:
    def info (self):
            name = input("Entrez le nom du tournoi : ")
            name_site = input("Entrez le lieu du tournoi : ")
            start_date = input("Entrez la date de début du tournois (JJ/MM/AAA) : ")
            end_date = input("Entrez la date de fin du tournois (JJ/MM/AAA): ")
            description_tournament = input("Description du tournois : ")
            choose_time = self.choose_time()
            assign_player = self.assign_player()
            tournaments_info = []
            tournaments_info.extend((name, name_site, start_date, end_date, description_tournament, choose_time, assign_player))
            return tournaments_info()

    def assign_player(self, tournament=Tournament):
        assignplayer=int(input("Voulez vous assigner un joueur au tournoi ? : [1] Oui creér un joueur, "
                                   "[2] Oui choisir dans la liste, "
                                   "[3] Non :  "))
        if assignplayer == 1:
            pass
        elif assignplayer == 2:
            pass
        elif assignplayer ==3:
            pass
        else:
            print("Vous devez entrer le numéro de votre choix.")
            return self.assign_player()


    def choose_time(self):
        choosetime = int(input("Entrez le contrôle du temps : [1] Bullet , [2] Blitz, [3] Coup rapide : "))
        if choosetime == 1:
            return "Bullet"
        elif choosetime == 2:
            return "Blitz"
        elif choosetime == 3:
            return "Coup rapide"
        else:
            print("Vous devez entrer le numéro de votre choix.")
            return self.choose_time()

