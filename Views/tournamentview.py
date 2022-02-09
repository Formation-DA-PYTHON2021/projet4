from tinydb import TinyDB, Query, where
from ..Views.playerview import ViewPlayer
from ..Models.playermdl import Player

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
        if selectournament == i['name']:
            infoselecttournament = tournament_db.search(where('name') == selectournament)[0]
        else:
            print("\n-------------------ERREUR--------------------------\n"
                "Veuillez saisir le bon nom de tournois \n"
                "(attention à l'orthographe)"
                "\n---------------------------------------------------\n")
            return self.info()
        return selectournament

    def choose_player(self, selectournament):
        players = []
        num = 1
        while num <= 4:
            print("\n--------Ajouter le joueur n° "f'{num}'"-------------\n")
            choose = input("[1] Ajouter un nouveau joueur \n[2] Ajouter un joueur existant \n >> ")
            if choose == '1':
                players.append(self.create_player())
            elif choose == '2':
                players.append(self.assign_player())
            else:
                print("Appuiez sur '1' ou '2' \n >> ")
                return self.choose_player(selectournament)
            num += 1
        maj = Query()
        tournament_db.update({'assign_player': players}, maj.name == selectournament)
        newlist = []
        for i in players:
            newlist.extend(player_db.search((where('name') == i)))
        return newlist


    def create_player(self):
        self.createplayer = ViewPlayer()
        info_player = self.createplayer.info()
        print(*info_player)
        player2 = Player(*info_player)
        Player.update(player2)
        return info_player


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
            print("\n-------------ERREUR-------------\n"
                  "Veuillez saisir le bon nom"
                  "(attention à l'orthographe)"
                  "\n--------------------------------\n")
            return self.assign_player()

    def first_round(self, groups):
        print("\n-------------------------------------------------------\n "
              "les rencontres du premier round sont les suivantes : "
              "\n-------------------------------------------------------")
        for i in groups:
            print(f'{i[0]["name"]}' " vs " f'{i[1]["name"]} \n*************')

    def next_round(self, groups):
        print("\n-------------------------------------------------------\n "
              "les rencontres du premier round sont les suivantes : "
              "\n-------------------------------------------------------")
        for i in groups:
            print(f'{i[0]["name"]}' " vs " f'{i[1]["name"]} \n*************')

    def enter_result_match(self, groups, selectournament):
        print("\n---------------------------------------------------------------\n"
              "Veuillez saisir les résultats des matchs de ce round :  "
              "\n(gagant = 1 pt ; perdant = 0 pt ; match nul = 0,5 pt)"
              "\n---------------------------------------------------------------")
        list_score_match = {}
        maj = Query()

        for i in groups:
            base1 = player_db.search((where('name') == f'{i[0]["name"]}'))
            base2 = player_db.search((where('name') == f'{i[1]["name"]}'))
            print("\nMatch " f'{i[0]["name"]}' " vs " f'{i[1]["name"]} : ')
            score1 = input("saisir le score de " f'{i[0]["name"]} : ')
            player_db.update({'number_points': score1}, maj.name == base1)
            score2 = input("saisir le score de " f'{i[1]["name"]} : ')
            player_db.update({'number_points': score2}, maj.name == base2)
            list_score_match[f'{i[0]["name"]}'] = score1
            list_score_match[f'{i[1]["name"]}'] = score2
            if score1 == '1':
                continue
            elif score1 == '0':
                continue
            elif score1 =='0.5':
                continue
            elif score2 == '1':
                continue
            elif score2 == '0':
                continue
            elif score2 =='0.5':
                continue
            else:
                print("\n-------------------ERREUR-------------------------\n"
                      "le nombre de points se distribue ainsi : \n"
                      "gagant = 1 pt ; perdant = 0 pt ; match nul = 0,5 pt \n"
                      "-----------------------------------------------------")
                return self.enter_result_match(groups)
        return list_score_match

    def update_result_match(self, points):
        print(points)