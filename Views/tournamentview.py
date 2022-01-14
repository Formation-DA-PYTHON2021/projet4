from tinydb import TinyDB, Query, where

db = TinyDB("./mvc/db.json")
player_db = db.table('player_db')
tournament_db = db.table('tournament_db')


class ViewTournament:
    def info(self):
        print("-------------------------------------------------\n"
              "                 Créer un tournois               \n"
              "-------------------------------------------------\n")
        name = input("Entrez le nom du tournoi : ")
        name_site = input("Entrez le lieu du tournoi : ")
        start_date = input("Entrez la date de début du tournois (JJ/MM/AAAA) : ")
        end_date = input("Entrez la date de fin du tournois (JJ/MM/AAAA): ")
        description_tournament = input("Description du tournois : ")
        choose_time = self.choose_time()
        assign_players = []
        tournaments_info = []
        tournaments_info.extend((name, name_site, start_date, end_date, description_tournament,
                                 choose_time, assign_players))
        return tournaments_info

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


class ViewResumingTournament:
    def info(self):
        print("-------------------------------------------------\n"
              "             Continuer un tournois               \n"
              "-------------------------------------------------\n")
        dispalytournament = tournament_db.all()
        for i in dispalytournament:
            print(i['name'])
        selectournament = str(input("Pour choisir un tournoi, rentrer son nom : "))
        infoselecttournament = tournament_db.search(where('name') == selectournament)[0]
        print([infoselecttournament])
        # return self.players_match(infoselecttournament)
        # doit retourner le tournois ou il s'est arrêté
        assign_players = []
        cmpt = 0
        while cmpt < 8:
            choose_player = self.choose_player()
            assign_players.append(choose_player)
            cmpt += 1

    def choose_player(self):
        print("--------Ajouter le joureur n°1-------------\n")
        choose = str(input("[1] Ajouter un nouveau joueur \n " \
                           "[2] Ajouter un joueur existant \n"))

        for i in choose:
            if i == 1:
                return self.create_player()
            elif i == 2:
                return self.assign_player()
        else:
            return self.choose_player()

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

    def create_player(self):
        name = input("Entrez le nom : ")
        first_name = input("Entrez le prénom : ")
        date_birth = input("Entrez la date de naissance (JJ/MM/AAA) : ")
        sexe = input("Entrez le sexe (F/M) : ")
        ranking = input("Entrez le classement : ")
        assign_players = []
        assign_players.extend((name, first_name, date_birth, sexe, ranking))
        return assign_players
