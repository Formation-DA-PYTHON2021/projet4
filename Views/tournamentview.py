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
            tournaments_info.extend((name, name_site, start_date, end_date, description_tournament,
                                     choose_time, assign_player))
            return tournaments_info

    def assign_player(self):
        addplayer = player_db.all()
        player = []
        for elm in addplayer:
            print(elm['name'])
            player.append(elm['name'])
        assignplayer = str(input("Assigner un joueur au tournoi. Rentrer son nom : "))
        if assignplayer in player:
            return assignplayer
        else:
            print("Entrer le bon nom : ")

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