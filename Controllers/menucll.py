import sys

from ..Views.menuview import HomeMenuView
from ..Models.menumdl import Menu
from ..Controllers.tournamentcll import ControllerTournament
from ..Controllers.playercll import ControllerPlayer
from ..Controllers.launchTournacll import ControllerLaunchTournament
from ..Controllers.tournamentcll import ControllerResumingTournament


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
        # 1 construire un menu
        self.menu.add("auto", "Créer un tournois", TournamentMenuController()) #menu.add(key,option, controller)
        self.menu.add("auto", "Reprendre un tournoi", ResumingTournament())
        self.menu.add("auto", "Rapports", ReportMenuController())
        self.menu.add("auto", "quitter", EndScreenMenuController())
        # 2 demander à la vue d'afficher le menu + collecte réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        #3 retourner le controller associer au choix de l'utilisateur au controller principal
        return user_choice.handler


class TournamentMenuController:
    def __call__(self):
        return ControllerTournament()

class PlayerMenuController:
    def __call__(self):
        return ControllerPlayer()


class LaunchTournament:
    def __call__(self):
        return ControllerLaunchTournament()

class ResumingTournament:
    def __call__(self):
        return ControllerResumingTournament()


class ReportMenuController:
    pass # appel la methode pour lancer le rapport ou choisir un tournoi

class EndScreenMenuController:
    def __call__(self):
        sys.exit()


