
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
        groups = self.first_round(resuming_info)
        self.view.first_round(groups)
        points = self.view.enter_result_match(groups)
        self.view.update_result_match(points)
        #self.next_rounds(resuming_info)
        #scores = self.view.enter_result_match(groups)
        #self.update_result_match(groups, scores)
        return resuming_info


    def first_round(self, players):
        #print("player==============>", players)
        #players = sorted(players, key=lambda player: player.ranking)
        player = sorted(players, key=lambda x: x['ranking'])
        #for verif in player:
            #print(verif['ranking'])
        #print(player)
        #faire le trie sur le classement
        middle = len(player) // 2
        group1 = player[:middle]
        group2 = player[middle:]
        matches = list(zip(group1, group2))
        return group1, group2

    def next_rounds(self, players):
        #print("player==============>", players)
        # players = sorted(players, key=lambda player: player.ranking)
        player = sorted(players, key=lambda x: x['number_points'])
        # faire le trie sur le nbr de point si égale sur le ranking
        middle = len(player) // 2
        group1 = player[:middle]
        group2 = player[middle:]
        matches = list(zip(group1, group2))
        return group1, group2



    def update_ranking(self):
        pass