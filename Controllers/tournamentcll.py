
from ..Views.tournamentview import ViewTournament
from ..Models.tournamentsmdl import Tournament
from ..Views.tournamentview import ViewResumingTournament

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
        self.view.first_round(first_matches)
        self.view.enter_result_match(first_matches)
        next_matches = self.next_rounds(resuming_info)
        self.view.next_round(next_matches)
        self.view.enter_result_next_match(next_matches)
        #self.update_ranking()


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
        associé le j1 avec j2 ect si la rencontre à déjà eu lieu j1 avec j3 ...
        '''
        player = sorted(players, key=lambda x: x['number_points'] or ['ranking'])
        print(player)
        group1 = player[:2]
        group2 = player[2:4]
        group3 = player[4:6]
        group4 = player[-2:]
        matches = list(zip(group1, group2, group3, group4))
        print('gr1 ', group1)
        print('gr2 ', group2)
        print('gr3 ', group3)
        print('gr4 ', group4)
        print(matches)
        return matches



    def update_ranking(self):
        ''' le gestionnaire devrait pouvoir modifier le classement d'un joueur à tout moment, et pas
        seulement après un tournoi.'''
        pass

    def display_tournament_results(self):
        pass