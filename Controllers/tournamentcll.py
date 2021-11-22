from ..Views.tournamentview import ViewTournament
from ..Models.tournamentsmdl import Tournament

class ControllerTournament:
    def __init__(self):
        self.view = ViewTournament()

    def __call__(self):
        tournaments_info = self.view.info()
        print(*tournaments_info)
        tourmament1 = Tournament(*tournaments_info)
        return Tournament.update(tourmament1)