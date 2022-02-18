
from ..Views.tournamentview import ViewTournament
from ..Models.tournamentsmdl import Tournament
from ..Views.tournamentview import ViewResumingTournament
from operator import attrgetter

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
        list_first_matches = self.view.first_round(first_matches, selectourna)
        list_score_first_matches = self.view.enter_result_match(first_matches)
        self.view.view_first_round_results(list_score_first_matches)
        #i = 0
        #while i < 3:
        #next_matches = self.next_rounds(resuming_info)
        #self.view.next_round(next_matches)
        #self.view.enter_result_next_match(next_matches)
            #i = i+1
        #self.view.update_ranking(resuming_info)
        #self.view.view_next_round_results(next_matches)
        #self.view.display_tournament_results(selectourna)
        #self.display_tournament_results(first_matches, next_matches)


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
        list = sorted(players, key=lambda x: x['number_points'])
        player = sorted(list, key=lambda x: x['ranking'])
        return player



    def update_ranking(self, players):
        ''' le gestionnaire devrait pouvoir modifier le classement d'un joueur à tout moment, et pas
        seulement après un tournoi.'''
        pass

    def display_tournament_results(self, first_matches, next_matches):
        self.view.view_first_round_results(first_matches)
        self.view.view_next_round_results(next_matches)