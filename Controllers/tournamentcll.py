from operator import itemgetter
from datetime import datetime
from tinydb import TinyDB, Query, where
from tinydb.operations import add


from ..Views.tournamentview import ViewTournament
from ..Models.tournamentsmdl import Tournament
from ..Views.tournamentview import ViewResumingTournament
from ..Views.tournamentview import ViewReport

db = TinyDB("./mvc/db.json")
player_db = db.table('player_db')
tournament_db = db.table('tournament_db')


class ControllerTournament:
    def __init__(self):
        self.view = ViewTournament()

    def __call__(self):
        tournaments_info = self.view.info()
        tourmament1 = Tournament(*tournaments_info)
        return Tournament.update(tourmament1)


class ControllerResumingTournament:
    def __init__(self):
        self.view = ViewResumingTournament()

    def __call__(self):
        self.view.menu()
        selectourna = self.view.selectourna()
        chooseplayers = self.view.choose_player(selectourna)
        self.starttourna(self.dateandtime(), selectourna)
        first_matchs = self.first_round(chooseplayers)
        self.view.display_round(first_matchs)
        begin_time_first = self.dateandtime()
        list_score_first_matchs = self.view.enter_result_match(first_matchs)
        end_time_first = self.dateandtime()
        round_first_matchs = ("1")
        self.view.view_round_number(round_first_matchs)
        self.view.view_matchs_results(list_score_first_matchs)
        inst_first_round = self.inst_round(round_first_matchs, begin_time_first, end_time_first,list_score_first_matchs)
        self.save_inst_round(inst_first_round, selectourna)
        i = 2
        while i < 5:
            players = self.players_tournament(selectourna)
            next_matchs = self.next_rounds(players)
            self.view.display_round(next_matchs)
            begin_time_next = self.dateandtime()
            list_score_next_matchs = self.view.enter_result_match(next_matchs)
            end_time_next = self.dateandtime()
            round_next_matchs = (f'{i}')
            self.view.view_round_number(round_next_matchs)
            self.view.view_matchs_results(list_score_next_matchs)
            inst_next_round = self.inst_round(round_next_matchs, begin_time_next, end_time_next, list_score_next_matchs)
            self.save_inst_round(inst_next_round, selectourna)
            i = i + 1
        self.endtourna(self.dateandtime(), selectourna)
        players = self.players_tournament(selectourna)
        self.view.display_tournament_results(selectourna, players)
        self.view.update_ranking()

    def starttourna(self, now, selectourna):
        maj = Query()
        tournament_db.update(add('start_date', now), maj.name == selectourna)

    def first_round(self, players):
        '''premier tour, triez tous les joueurs en fonction de leur classement.
        Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
        Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié inférieure
        ex:  joueur 2 est jumelé avec le joueur 6, etc.'''
        player = sorted(players, key=lambda x: x['ranking'])
        middle = len(player) // 2
        group1 = player[:middle]
        group2 = player[middle:]
        matches = list(zip(group1, group2))
        return matches

    def next_rounds(self, players):
        '''faire le trie sur le nbr de point si égale sur le ranking
        associé le j1 avec j2 ect si la rencontre à déjà eu lieu j1 avec j3 '''
        player = sorted(players, key=itemgetter('ranking'))
        playersort = sorted(players, key=itemgetter('number_points'), reverse=True)
        playeround = []
        playeround.extend(playersort)
        groups = playeround[::2], playeround[1::2]
        matches = list(zip(groups[0], groups[1]))
        dispo = []
        dispo.extend(playeround)
        for item in range(len(matches)):
            (player_1, player_2) = matches[item]
            dispo.remove(player_1)
            if player_2['name'] in player_1['player_played']:
                possibles = [p for p in dispo if p['name'] not in player_1['player_played']]
                if not possibles:
                    dispo.remove(player_2)
                else:
                    fighter = next(iter(possibles))
                    matches[item] = (player_1, fighter)
                    dispo.remove(fighter)
                    groups2 = dispo[::2], dispo[1::2]
                    matches2 = list(zip(groups2[0], groups2[1]))
                    matches[item + 1:] = matches2
            else:
                dispo.remove(player_2)
        return matches

    def players_tournament(self, selectourna):
        tournament = tournament_db.all()
        namealltourna = []
        listourna = []
        newlistupdate = []
        for elm in tournament:
            namealltourna.append(elm['name'])
        if selectourna in namealltourna:
            listourna = tournament_db.search(where('name') == selectourna)[0]
        players_tourna = listourna['assign_player']
        for i in players_tourna:
            newlistupdate.extend(player_db.search((where('name') == i)))
        return newlistupdate

    def dateandtime(self):
        now = str(datetime.now())
        return now

    def inst_round(self, numround, begin_time, end_time, list_scor_match):
        inst_round = (f'round n°{numround}', begin_time, end_time, list_scor_match)
        return inst_round

    def save_inst_round(self, inst_round, selectourna):
        maj = Query()
        tournament_db.update(add('instances_rounds', inst_round), maj.name == selectourna)

    def endtourna(self, now, selectourna):
        maj = Query()
        tournament_db.update(add('end_date', now), maj.name == selectourna)

class ControllerReport:
    def __init__(self):
        self.view = ViewReport()
        self.viewresuming = ViewResumingTournament()
        self.cll = ControllerResumingTournament()

    def __call__(self):
        choicemenu = self.view.menu_report()
        for i in choicemenu:
            if i == '1':  # acteurs
                players = self.view.players()
                self.view.choicesorting(players)
                return self.view.menu_report()
            elif i == '2':  # joueurs pour un tournoi
                selectourna = self.view.choicetourna()
                print(f"---------- liste des joueurs du tournoi {selectourna['name']}: ----------\n")
                assignplayerstourna = []
                assignplayerstourna.extend(selectourna['assign_player'])
                playerstourna = []
                for i in assignplayerstourna:
                    playerstourna.extend(player_db.search(where('name') == i))
                self.view.choicesorting(playerstourna)
                return self.view.menu_report()
            elif i == '3': #liste de tous les tournois
                self.view.displayTourna()
                return self.view.menu_report()
            elif i == '4':  # issus des match pour un tournoi
                listourna = self.view.choicetourna()
                selectourna = listourna['name']
                instance_round = listourna['instances_rounds']
                lists_score_matchs = instance_round[3::4]
                infotourna = self.view.menuinfotourna(listourna)
                players = self.cll.players_tournament(selectourna)
                for p in infotourna:
                    if p == '1': #Liste info round d'un tournoi
                        self.viewresuming.display_tournament_results(selectourna, players)
                    elif p == '2': # ensemble des matchs du tournoi
                        x = 0
                        for elm in lists_score_matchs:
                            x += 1
                            self.viewresuming.view_round_number(x)
                            self.viewresuming.view_matchs_results(elm)
                    else:
                        return self.view.menu_report()
                return self.view.menu_report()
            else:
                return self.view.menu_report()
