from tinydb import TinyDB, Query, where
from tinydb.operations import add
from ..Views.playerview import ViewPlayer
from ..Models.playermdl import Player
from operator import itemgetter

db = TinyDB("./mvc/db.json")
player_db = db.table('player_db')
tournament_db = db.table('tournament_db')

class ViewTournament:
    def info(self):
        print("-------------------------------------------------\n"
              "                 Créer un tournois               \n"
              "-------------------------------------------------\n")
        name = input("Entrez le nom du tournoi : \n => ")
        name_site = input("Entrez le lieu du tournoi : \n => ")
        start_date = input("Entrez la date de début du tournois (JJ/MM/AAAA) : \n => ")
        end_date = input("Entrez la date de fin du tournois (JJ/MM/AAAA): \n => ")
        description_tournament = input("Description du tournois : \n => ")
        choose_time = self.choose_time()
        assign_players = []
        tournaments_info = []
        tournaments_info.extend((name, name_site, start_date, end_date, description_tournament,
                                 choose_time, assign_players))
        return tournaments_info

    def choose_time(self):
        choosetime = int(input("Entrez le contrôle du temps : [1] Bullet , [2] Blitz, [3] Coup rapide : \n => "))
        if choosetime == 1:
            return "Bullet"
        elif choosetime == 2:
            return "Blitz"
        elif choosetime == 3:
            return "Coup rapide"
        else:
            print("Vous devez entrer le numéro de votre choix. \n => ")
            return self.choose_time()


class ViewResumingTournament:
    def info(self):
        print("-------------------------------------------------\n"
              "             Continuer un tournois               \n"
              "-------------------------------------------------\n")
        dispalytournament = tournament_db.all()
        for i in dispalytournament:
            print(i['name'])
        selectournament = str(input("Pour choisir un tournoi, rentrer son nom : \n => "))
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
        while num <= 8:
            print("\n--------Ajouter le joueur n° "f'{num}'"-------------\n")
            choose = input("[1] Ajouter un nouveau joueur \n[2] Ajouter un joueur existant \n => ")
            if choose == '1':
                players.append(self.create_player())
            elif choose == '2':
                players.append(self.assign_player())
            else:
                print("Appuiez sur '1' ou '2' \n => ")
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
        return info_player[0]

    def assign_player(self):
        addplayer = player_db.all()
        player = []
        for elm in addplayer:
            print(elm['name'])
            player.append(elm['name'])
        assignplayer = str(input("Assigner un joueur au tournoi. Rentrer son nom : \n => "))
        if assignplayer in player:
            return assignplayer
        else:
            print("\n-------------ERREUR-------------\n"
                  "Veuillez saisir le bon nom"
                  "(attention à l'orthographe)"
                  "\n--------------------------------\n")
            return self.assign_player()

    def players_tournament(self):
        addplayer = player_db.all()
        players = []
        for elm in addplayer:
            players.append(elm['name'])
        newlistupdate = []
        for i in players:
            newlistupdate.extend(player_db.search((where('name') == i)))
        return newlistupdate


    def display_round(self, matches, selectournament):
        print("\n-------------------------------------------------------\n "
              "les matches du round sont les suivantes : "
              "\n-------------------------------------------------------")
        matches_round = []
        for i in matches:
            maj = Query()
            print(f'{i[0]["name"]}' " vs " f'{i[1]["name"]} \n*************')
            matches_round.append((f'{i[0]["name"]}', f'{i[1]["name"]}'))
        tournament_db.update(add('instances_match', matches_round), maj.name == selectournament)
        return matches_round

    def enter_result_match(self, matches):
        print("\n---------------------------------------------------------------\n"
              "Veuillez saisir les résultats des matchs de ce round :  "
              "\n(gagant = 1 pt ; perdant = 0 pt ; match nul = 0.5 pt)"
              "\n---------------------------------------------------------------")
        maj = Query()
        list_score_match = []
        for i in matches:
            score_matchs = ()
            print("\nMatch " f'{i[0]["name"]}' " vs " f'{i[1]["name"]} : ')
            score1 = float(input("saisir le score de " f'{i[0]["name"]} : '))
            score2 = float(input("saisir le score de " f'{i[1]["name"]} : '))
            player_db.update(add('number_points', score1), maj.name == f'{i[0]["name"]}')
            player_db.update(add('player_played', [f'{i[1]["name"]}']), maj.name == f'{i[0]["name"]}')
            player_db.update(add('number_points', score2), maj.name == f'{i[1]["name"]}')
            player_db.update(add('player_played', [f'{i[0]["name"]}']), maj.name == f'{i[1]["name"]}')
            score_matchs = (f'{i[0]["name"]}', score1, f'{i[1]["name"]}', score2)
            list_score_match.append(score_matchs)
            if score1 == 1 and score2 == 0:
                continue
            elif score1 == 0 and score2 == 1:
                continue
            elif score1 == 0.5 and score2 == 0.5:
                continue
            else:
                print("\n-------------------ERREUR-------------------------\n"
                      "le nombre de points se distribue ainsi : \n"
                      "gagant = 1 pt ; perdant = 0 pt ; match nul = 0.5 pt \n"
                      "-----------------------------------------------------")
                return self.enter_result_match(matches)
        return list_score_match

    def view_round_results(self, list_score_matchs):
        print("\n---------------------\n"
              " Résultats des matches du round : "
              "\n---------------------")
        for i in list_score_matchs:
            print("\n""Match : " f'{i[0]}' " vs " f'{i[2]}:')
            print(f'{i[0]}' ": "f'{i[1]}'" point")
            if i[1] == 1 :
                print('-> vainqueur')
            elif i[1] == 0:
                print('-> perdant')
            elif i[1] == 0.5:
                print("match nul")
            print(f'{i[2]}' ": "f'{i[3]}'" point")
            if i[3] == 1 :
                print('-> vainqueur')
            elif i[3] == 0:
                print('-> perdant')
            elif i[3] == 0.5:
                print("match nul")
        return 'fin de match'


    def display_tournament_results(self, selectouna, players):
        print("-------------------------------------------------\n"
              "             Résultat du tournois               \n"
              "-------------------------------------------------\n")
        tourna = []
        tourna.extend(tournament_db.search((where('name') == selectouna)))
        for elm in tourna:
            name = elm['name']
            site = elm['site']
            date1 = elm['start_date']
            date2 = elm['end_date']

        print("-------------------------\n"
              "      TOURNOIS :\n"
              ,name," à ",site,"\n",
              date1, " / ", date2, "\n"
              "---------------------------")
        playersort = sorted(players, key=itemgetter('number_points'), reverse=True)
        print('le joueur à obtenir le plus grand nombre de point\n'
              ' remportera le tournois \n'
              '----------------------------')
        for i in playersort:
            print(i['name'], 'nombre de point : ', i['number_points'])
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
              'le vainqueur du tournois est : ', playersort[0]['name'],
              '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


    def update_ranking(self):
        ''' le gestionnaire devrait pouvoir modifier le classement d'un joueur à tout moment, et pas
                seulement après un tournoi.'''
        print("-------------------------------------------------\n"
              "           Mise à jour du classement             \n"
              "-------------------------------------------------\n")
        players = player_db.all()
        player = []
        maj = Query()
        update_ranking = input("---------- Voulez-vous mettre à jour le classement des joueurs ? ----------\n"
                               "[1] oui / [2] non\n=> ")
        for i in update_ranking:
            if i == '1':
                for elm in players:
                    print(elm['name'])
                    player.append(elm['name'])
                chooseplayer = str(input("\n---------- Choisir un joueur ----------\n"
                                 "Rentrez son nom =>  "))
                if chooseplayer in player:
                    newranking = int(input("\n---------- Rentrez son nouveau numéro de classement : ----------\n  => "))
                    safenewranking= str(input("\n---------- Veuillez confirmer votre choix : ----------\n "
                                            "nouveau classement : joueur: "f'{chooseplayer}'" - classement : "f'{newranking}'" ?\n"
                                            " [1] oui / [2] non\n => "))
                    if safenewranking == '1':
                        player_db.update({'ranking': newranking}, maj.name == chooseplayer)
                        print("le classement est mis à jour")
                        newranking = str(input("\n---------- Voulez-vous affichier le nouveau classement ? ----------\n"
                                    "[1] oui / [2] non\n => "))
                        if newranking == '1':
                            print("Nouveau classement à l'issu du tournois :")
                            playersort = sorted(player_db, key=itemgetter('ranking'))
                            for elm in playersort:
                                print(elm['name'], ": ", elm['ranking'])
                        else:
                            return self.update_ranking()
                    else:
                            print("annulation de la demande de modification du classement du joueur")
                            return self.update_ranking()
            else:
                print("Le classement n'a pas été mis à jour")
