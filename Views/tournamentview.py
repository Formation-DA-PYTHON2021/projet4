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
                return choose
            num += 1
        maj = Query()
        tournament_db.update({'assign_player': players}, maj.name == selectournament)
        newlist = []
        for i in players:
            newlist.append(player_db.search((where('name') == i)))
        return newlist


    def create_player(self):
        name = input("Entrez le nom : ")
        first_name = input("Entrez le prénom : ")
        date_birth = input("Entrez la date de naissance (JJ/MM/AAA) : ")
        sexe = input("Entrez le sexe (F/M) : ")
        ranking = input("Entrez le classement : ")
        resuming_info = [name, first_name, date_birth, sexe, ranking]
        return resuming_info

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
            print("\n-------\nErreur de nom!\nVeuillez saisir le bon nom dans la liste ci-dessous "
                  "(attention à l'orthographe) :\n-------")
            return self.assign_player()


