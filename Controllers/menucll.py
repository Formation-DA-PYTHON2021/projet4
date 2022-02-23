import sys

from ..Views.menuview import HomeMenuView
from ..Models.menumdl import Menu
from ..Controllers.tournamentcll import ControllerTournament
from ..Controllers.tournamentcll import ControllerResumingTournament
from ..Controllers.tournamentcll import ControllerReport


class ControllerMenus:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        while self.controller:
            self.controller = self.controller()


class HomeMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        print("-------------------------------------------------\n"
              "                  Menu Principal                 \n"
              "-------------------------------------------------")

        self.menu.add("auto", "Créer un tournois", TournamentMenuController())
        self.menu.add("auto", "Reprendre un tournoi", ResumingTournamentMenuController())
        self.menu.add("auto", "Rapports", ReportMenuController())
        self.menu.add("auto", "quitter", EndScreenMenuController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler


class TournamentMenuController:
    def __call__(self):
        return ControllerTournament()

class ResumingTournamentMenuController:
    def __call__(self):
        return ControllerResumingTournament()


class ReportMenuController:
    def __call__(self):
        return ControllerReport()

class EndScreenMenuController:
    def __call__(self):
        sys.exit()


