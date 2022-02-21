
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
        self.view.display_round(first_matches, selectourna)
        list_score_first_matches = self.view.enter_result_match(first_matches)
        self.view.view_round_results(list_score_first_matches)
        i = 0
        while i < 3:
            players = self.view.players_tournament()
            next_matches = self.next_rounds(players)
            self.view.display_round(next_matches, selectourna)
            list_score_next_matches = self.view.enter_result_match(next_matches)
            self.view.view_round_results(list_score_next_matches)
            i = i + 1
        # self.view.update_ranking(resuming_info)
        # self.view.view_next_round_results(next_matches)
        # self.view.display_tournament_results(selectourna)
        # self.display_tournament_results(first_matches, next_matches)

    def first_round(self, players):
        '''premier tour, triez tous les joueurs en fonction de leur classement.
        Divisez les joueurs en deux moitiés, une supérieure et une inférieure.
        Le meilleur joueur de la moitié supérieure est jumelé avec le meilleur joueur de la moitié inférieure
        ex:  joueur 2 est jumelé avec le joueur 6, etc.'''
        #print('players in first round :', players)
        player = sorted(players, key=lambda x: x['ranking'])
        middle = len(player) // 2
        group1 = player[:middle]
        group2 = player[middle:]
        matches = list(zip(group1, group2))
        return matches

    def next_rounds(self, players):
        '''faire le trie sur le nbr de point si égale sur le ranking
        associé le j1 avec j2 ect si la rencontre à déjà eu lieu j1 avec j3 ...
        print('players in next round :',players)
        list = sorted(players, key=lambda x: x['number_points'])
        player = sorted(list, key=lambda x: x['ranking'])
        group1 = player[0:2]
        group2 = player[2:4]
        group3 = player[4:6]
        group4 = player[6:8]
        return group1, group2, group3, group4'''
        liste = sorted(players, key=lambda x: x['number_points'])
        player = sorted(liste, key=lambda x: x['ranking'])
        playeround = []
        playeround.extend(player)
        #print("first rounddddddd", playeround)  #
        groups = playeround[::2], playeround[1::2]
        matches = list(zip(groups[0], groups[1]))

        availables = []
        availables.extend(playeround)
        #print("le testtt unique===", availables) #

        for item in range(len(matches)):
            (player_1, player_2) = matches[item]
            availables.remove(player_1)

            if player_2['name'] in player_1['player_played']:
                possibles = [p for p in availables if p not in player_1['player_played']]

                if not possibles:
                    availables.remove(player_2)
                    #print("not possiblesnot possiblesnot possibles")  #
                else:
                    # print("possibles", possibles)
                    fighter = next(iter(sorted(possibles)))
                    # print("fighter===>", fighter)
                    matches[item] = (player_1, fighter)

                    availables.remove(fighter)
                    #print("availables remove fighter 1===", availables)  #
                    groups2 = availables[::2], availables[1::2]

                    matches2 = list(zip(groups2[0], groups2[1]))
                    #print("Matches Matches 2===", matches2)  #
                    matches[item + 1:] = matches2
                    #print("possible Matches 3===", matches)  #
        #print("matches====>", matches)
        return matches

    def update_ranking(self, players):
        ''' le gestionnaire devrait pouvoir modifier le classement d'un joueur à tout moment, et pas
        seulement après un tournoi.'''
        pass

    def display_tournament_results(self, first_matches, next_matches):
        self.view.view_round_results(first_matches)
        self.view.view_next_round_results(next_matches)
