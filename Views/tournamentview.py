from operator import itemgetter

from tinydb import TinyDB, Query, where
from tinydb.operations import add

from ..Models.playermdl import Player
from ..Views.playerview import ViewPlayer
from ..Controllers import tournamentcll

db = TinyDB("./mvc/db.json")
player_db = db.table('player_db')
tournament_db = db.table('tournament_db')
maj = Query()


class ViewTournament:
    def info(self):
        print("-------------------------------------------------\n"
              "                 Créer un tournois               \n"
              "-------------------------------------------------\n")
        name = input("Entrez le nom du tournoi : \n => ")
        name_site = input("Entrez le lieu du tournoi : \n => ")
        start_date = ''
        end_date = ''
        description_tournament = input("Description du tournois : \n => ")
        choose_time = self.choose_time()
        assign_players = []
        instances_rounds = []
        playerdb_tourna = []
        tournaments_info = []
        tournaments_info.extend((name, name_site, start_date, end_date,
                                 description_tournament, choose_time,
                                 assign_players, instances_rounds, playerdb_tourna))
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
    def menu(self):
        print("-------------------------------------------------\n"
              "             Continuer un tournois               \n"
              "-------------------------------------------------\n")

    def selectourna(self):
        dispalytournament = tournament_db.all()
        nametourna = []
        print('les tournois disponible : ')
        for elm in dispalytournament:
            print(elm['name'])
            nametourna.append(elm['name'])
        selectournament = str(input("Pour sélectionner un tournoi, rentrer son nom : \n => "))
        if selectournament in nametourna:
            return selectournament

        else:
            print("\n------------- ERREUR -------------\nVeuillez saisir le bon nom (attention à l'orthographe)"
                  "\n--------------------------------\n")
            return self.selectourna()
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
            print(elm['name'], elm['first_name'])
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

    def players_name_tournament(self, playertourna):
        nameplayertourna = []
        for elm in playertourna:
            nameplayertourna.append(elm['name'])
        return nameplayertourna

    def update_players_tourna(self, playernametourna):
        newlistupdate = []
        for i in playernametourna:
            newlistupdate.extend(player_db.search((where('name') == i)))
        return newlistupdate

    def display_round(self, matches):
        print("\n-------------------------------------------------------\n "
              "les matchs du round sont les suivantes : "
              "\n-------------------------------------------------------")
        for i in matches:
            print(f'{i[0]["name"]} ' f'{i[0]["first_name"]}' " vs " f'{i[1]["name"]} ' f'{i[1]["first_name"]}\n'
                  ">> le joueur "f'{i[0]["name"]} ' f'{i[0]["first_name"]}' " aura les pions blanc, "
                  "le joueur "f'{i[1]["name"]} ' f'{i[1]["first_name"]}' " les pions noir. \n*************")

    def enter_result_match(self, matches):
        print("\n---------------------------------------------------------------\n"
              "Veuillez saisir les résultats des matchs de ce round :  "
              "\n(gagant = 1 pt ; perdant = 0 pt ; match nul = 0.5 pt)"
              "\n---------------------------------------------------------------")
        list_score_match = []
        for i in matches:
            score_matchs = ()
            print("\nMatch " f'{i[0]["name"]} {i[0]["first_name"]}' " vs " f'{i[1]["name"]} {i[1]["first_name"]}: ')
            score1 = float(input("saisir le score de " f'{i[0]["name"]} {i[0]["first_name"]} : '))
            score2 = float(input("saisir le score de " f'{i[1]["name"]} {i[1]["first_name"]} : '))
            player_db.update(add('number_points', score1), maj.name == f'{i[0]["name"]}')
            player_db.update(add('player_played', [f'{i[1]["name"]}']), maj.name == f'{i[0]["name"]}')
            player_db.update(add('number_points', score2), maj.name == f'{i[1]["name"]}')
            player_db.update(add('player_played', [f'{i[0]["name"]}']), maj.name == f'{i[1]["name"]}')
            score_matchs = (f'{i[0]["name"]}', f'{i[0]["first_name"]}', score1,
                            f'{i[1]["name"]}', f'{i[1]["first_name"]}', score2,
                            f'{score1} - {score2}')
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

    def view_round_number(self, round_number):
        print("\n------------------------------------\n"
              f" Résultats des matchs du round n°{round_number} : "
              "\n------------------------------------")

    def view_matchs_results(self, list_score_matchs):
        x = 0
        for i in list_score_matchs:
            x += 1
            print(f"\nMatch n°{x} : {i[0]} {i[1]} VS {i[3]} {i[4]} : {i[6]}")
            if i[1] == 1:
                print(f'Le vainqueur du match est : {i[0]} {i[1]}')
            elif i[3] == 1:
                print(f'Le vainqueur du match est : {i[3]} {i[4]}')
            elif i[1] == 0.5:
                print("match nul")

    def display_tournament_results(self, tourna):
        inst_round = tourna.get('instances_rounds')
        match_round = inst_round[3::4]
        print("match_round dans display : ", match_round)
        print("match_round[0] dans display : ", match_round[0])
        print("--------------------------------------------------\n"
              "                 TOURNOIS :\n"
              f"               {tourna.get('name')} à {tourna.get('site')}\n"
              f"      du : {tourna.get('start_date')}\n      au : {tourna.get('end_date')}\n"
              f"description : {tourna.get('description_tournament')}\n"
              "--------------------------------------------------\n")
        print("---------- information sur les rounds : ----------")
        print(f"\nle {inst_round[0]} a débuté le : {inst_round[1]} et fini le : {inst_round[2]}\n"
              f"les rencontres pour ce round sont les suivantes :")
        for i in match_round[0]:
            print(f'{i[0]} {i[1]} VS {i[3]} {i[4]}, score : {i[6]}')

        print(f"\nle {inst_round[4]} a débuté le : {inst_round[5]} et fini le : {inst_round[6]}\n"
              f"les rencontres pour ce round sont les suivantes :")
        for i in match_round[1]:
            print(f'{i[0]} {i[1]} VS {i[3]} {i[4]}, score : {i[6]}')

        print(f"\nle {inst_round[8]} a débuté le : {inst_round[9]} et fini le : {inst_round[10]}\n"
              f"les rencontres pour ce round sont les suivantes :")
        for i in match_round[2]:
            print(f'{i[0]} {i[1]} VS {i[3]} {i[4]}, score : {i[6]}')

        print(f"\nle {inst_round[12]} a débuté le : {inst_round[13]} et fini le : {inst_round[14]}\n"
              f"les rencontres pour ce round sont les suivantes :")
        for i in match_round[3]:
            print(f'{i[0]} {i[1]} VS {i[3]} {i[4]}, score : {i[6]}')

    def display_playerdb_tourna(self, players):
        playersort = sorted(players, key=itemgetter('number_points'), reverse=True)
        print('\n--------------------------------------\n'
              'le joueur à obtenir le plus grand \n'
              'nombre de point remporte le tournois \n'
              '--------------------------------------')
        for i in playersort:
            print(i['name'], i['first_name'], 'nombre de point : ', i['number_points'])
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
              'le vainqueur du tournois est : ', playersort[0]['name'], playersort[0]['first_name'],
              '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    def update_ranking(self):
        ''' le gestionnaire devrait pouvoir modifier le classement d'un joueur à tout moment, et pas
                seulement après un tournoi.'''
        print("-------------------------------------------------\n"
              "           Mise à jour du classement             \n"
              "-------------------------------------------------\n")
        players = player_db.all()
        player = []
        update_ranking = input("---------- Voulez-vous mettre à jour le classement des joueurs ? ----------\n"
                               "[1] oui / [2] non\n=> ")
        for i in update_ranking:
            if i == '1':
                for elm in players:
                    print(elm['name'], elm['first_name'])
                    player.append(elm['name'])

                chooseplayer = str(input("\n---------- Choisir un joueur ----------\n"
                                         "Rentrez son nom =>  "))

                if chooseplayer in player:
                    newranking = int(input("\n---------- Rentrez son nouveau numéro de classement : "
                                           "----------\n  => "))
                    safenewranking = str(input("\n---------- Veuillez confirmer votre choix :"
                                               " ----------\n "
                                               "nouveau classement : joueur: "f'{chooseplayer}'" "
                                               "- classement : "f'{newranking}'" ?\n"
                                               " [1] oui / [2] non\n => "))

                    if safenewranking == '1':
                        player_db.update({'ranking': newranking}, maj.name == chooseplayer)
                        print("le classement est mis à jour")
                        newranking = str(input("\n---------- Voulez-vous affichier le nouveau classement ?"
                                               " ----------\n"
                                               "[1] oui / [2] non\n => "))

                        if newranking == '1':

                            print("Nouveau classement à l'issu du tournois :")
                            playersort = sorted(player_db, key=itemgetter('ranking'))
                            for elm in playersort:
                                print(elm['name'], elm['first_name'], ": ", elm['ranking'])
                        else:
                            return self.update_ranking()
                    else:
                        print("annulation de la demande de modification du classement du joueur")
                        return self.update_ranking()

            else:
                print("Le classement n'a pas été mis à jour")


class ViewReport:
    def menu_report(self):
        print("-------------------------------------------------\n"
              "                  Menu Rapport                 \n"
              "-------------------------------------------------\n"
              "---------- Menu  ----------\n"
              "[1] Voir la liste de tous les acteurs\n"
              "[2] Voir la liste de tous les joueurs d'un tournois \n"
              "[3] Voir la liste des tournois \n"
              "[4] Voir les rounds et les matchs pour un tournois \n"
              "[5] Retour au menu général")
        menureport = input("Entrez votre choix : ")
        return menureport

    def players(self):
        print("---------- liste des acteurs : ----------\n")
        players = player_db.all()
        return players

    def choicesorting(self, liste):
        self.cll = tournamentcll.ControllerReport()
        choicesorting = input("---------- choix du trie : ----------\n"
                              "[1] par ordre alphabetique\n"
                              "[2] par classement\n"
                              "[3] retour au menu Raport\n=>")
        for m in choicesorting:
            if m == '1':
                print("---------- par ordre alphabetique : ----------\n")
                sortalpha = sorted(liste, key=itemgetter('name'))
                for elm in sortalpha:
                    print(elm['name'], elm['first_name'], ' classement :', elm['ranking'])
                return self.choicesorting(liste)
            elif m == '2':
                print("---------- par classement : ----------\n")
                sortrank = sorted(liste, key=itemgetter('ranking'))
                for elm in sortrank:
                    print(elm['name'], elm['first_name'], ' classement :', elm['ranking'])
                return self.choicesorting(liste)
            elif m == '3':
                return self.cll()
            else:
                return self.choicesorting(liste)

    def choicetourna(self):
        tournament = tournament_db.all()
        nametourna = []
        print('\nles tournois disponible : ')
        for elm in tournament:
            print(elm['name'])
            nametourna.append(elm['name'])
        print()
        selectourna = str(input("---------- choix du tournoi : ----------\nRentrez son nom : \n=> "))
        if selectourna in nametourna:
            listourna = tournament_db.search(where('name') == selectourna)[0]
            return listourna
        else:
            print("\n-------------ERREUR-------------\n"
                  "Veuillez saisir le bon nom"
                  " (attention à l'orthographe)"
                  "\n--------------------------------\n")
            return self.choicetourna()
        return listourna

    def menuinfoplayer(self,selectourna):
        print(f"\n---------- liste des joueurs du tournoi {selectourna['name']}: ----------\n")

    def menuinfotourna(self, listourna):
        infotourna = str(input(f"\n---------- Voir les informations pour le tournois  {listourna['name']}:"
                               f" ----------\n"
                               "[1] liste des informations concernant les rounds du tounois\n"
                               "[2] issues des matchs du tournois \n"
                               "[3] retour au menu Rapport \n=> "))
        return infotourna

    def displayTourna(self):
        tournament = tournament_db.all()
        nametourna = []
        print('\nLa liste des tournois : ')
        for elm in tournament:
            print(elm['name'])
            nametourna.append(elm['name'])
        print('\nretour au menu\n')
