
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
        resuming_info = self.view.info()
        self.first_round(resuming_info)
        return resuming_info


    def first_round(self, players):
        print("player==============>", players)
        players = sorted(players, key=lambda player: player.ranking)
        middle = len(players) // 2
        groups = players[:middle], players[middle:]
        matches = list(zip(groups[0], groups[1]))
        print(matches)
