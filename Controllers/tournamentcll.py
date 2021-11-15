from ..Views.tournamentview import ViewTournament
from ..Models.tournamentsmdl import Tournament

class ControllerTournament:
    def __init__(self):
        self.view = ViewTournament()

    def __call__(self):
        tournament_info = self.view.info()
        print(*tournament_info)
        player1 = Tournament(*tournament_info)