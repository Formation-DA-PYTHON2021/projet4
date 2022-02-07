
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
        self.view.enter_result_match(groups)
        return resuming_info


    def first_round(self, players):
        #print("player==============>", players)
        #players = sorted(players, key=lambda player: player.ranking)
        middle = len(players) // 2
        group1 = players[:middle]
        group2 = players[middle:]
        matches = list(zip(group1, group2))
        return group1, group2

