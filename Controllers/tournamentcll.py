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
        selectourna = self.view.info()
        resuming_info = self.view.choose_player(selectourna)
        first_matches = self.first_round(resuming_info)
        self.view.display_round(first_matches)
        begin_time = self.dateandtime()
        list_score_first_matches = self.view.enter_result_match(first_matches)
        end_time = self.dateandtime()
        self.view.view_round_results(list_score_first_matches)
        inst_first_round = self.inst_round(list_score_first_matches, begin_time, end_time)
        self.save_inst_round(inst_first_round, selectourna)
        i = 0
        while i < 3:
            players = self.view.players_tournament()
            next_matches = self.next_rounds(players)
            self.view.display_round(next_matches)
            self.save_inst_round(next_matches, selectourna)
            list_score_next_matches = self.view.enter_result_match(next_matches)
            self.view.view_round_results(list_score_next_matches)
            inst_next_round = self.inst_round(list_score_next_matches, begin_time, end_time)
            self.save_inst_round(inst_next_round, selectourna)
            i = i + 1
        players = self.view.players_tournament()
        self.view.display_tournament_results(selectourna, players)
        self.view.update_ranking()

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

    def dateandtime(self):
        now = str(datetime.now())
        return now

    def inst_round(self, list_scor_match, begin_time, end_time):
        name = 'nameround'
        inst_round = (name, begin_time, end_time, list_scor_match)
        return inst_round

    def save_inst_round(self, inst_round, selectourna):
        maj = Query()
        tournament_db.update(add('instances_rounds', inst_round), maj.name == selectourna)


class ControllerReport:
    def __init__(self):
        self.view = ViewReport()
        self.viewresuming = ViewResumingTournament()

    def __call__(self):
        choicemenu = self.view.menu_report()
        for i in choicemenu:
            if i == '1':  # acteur
                players = self.view.players()
                self.view.choicesorting(players)
            elif i == '2':  # joueur pour un tournoi
                playerstourna = self.view.choicetourna()
                print(f"---------- liste des joueurs du tournoi f'{playerstourna['name']}: ----------\n")
                self.view.choicesorting(playerstourna)
            elif i == '3':  # round/match pour un tournoi
                listourna = self.view.choicetourna()
                infotourna = self.view.menuinfotourna(listourna)
                for p in infotourna:
                    if p == '1':
                        pass
                    elif p in infotourna:
                        return self.viewresuming.view_round_results(listourna)
                    else:
                        return self.view.menu_report()
            else:
                return self.view.menu_report()
