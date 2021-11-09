from ..View.menu import HomeMenuView
from ..Model.menu import Menu

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
        print("~~~~ Menu Général ~~~~")
        # 1 construire un menu
        self.menu.add("auto", "Tournois", TournamentMenuController()) #menu.add(key,option, controller)
        self.menu.add("auto", "Joueurs", PlayerMenuController())
        self.menu.add("auto", "Rapports", ReportMenuController())
        self.menu.add("auto", "q", EndScreenMenuController())
        # 2 demander à la vue d'afficher le menu + collecte réponse de l'utilisateur
        user_choice = self.view.get_user_choice()
        #3 retourner le controller associer au choix de l'utilisateur au controller principal
        return user_choice.handler

class TournamentMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)
    def __call__(self):
        print("~~~~ Menu Tournois ~~~~")
        self.menu.add("auto","Séléctionner un tournoi", SelectTournament())
        self.menu.add("auto", "Créer un tournoi", CreateTournament())
        self.menu.add("auto", "Tournoi en cours", OpenTournamentMenuController)
        self.menu.add("auto", "q", EndScreenMenuController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler

class SelectTournament:
    pass # doit choisir dans la liste des tournoi déjà enregistrer + voir les rapports à lier avec PublishReportMenuController

class CreateTournament:
    pass #doit renvoyer aux aux critères d'enregistrement d'un tournois

class OpenTournamentMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        print("~~~~ Menu Tournoi en cours ~~~~")
        self.menu.add("auto","Séléctionner un joueur", SelectPlayer())
        self.menu.add("auto", "Générer des paires", SelectPlayer())
        self.menu.add("auto", "Publier un rapport", PublishReportMenuController())
        self.menu.add("auto","Sauvagarder", SaveTournament())
        self.menu.add("auto", "Clore le tournoi", FinishTournament())
        self.menu.add("auto", "q", EndScreenMenuController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler

class SelectPlayer():
    pass #doit choisir dans un liste un joueur

class SaveTournament():
    pass # doit sauvegarder le tournoi soit les match et round + enregistrement des note au joueur

class FinishTournament():
    pass #clore le tournois avec impossibilité de modifier les donners

class PlayerMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        print("~~~~ Menu Joueurs ~~~~")
        self.menu.add("auto", "Séléctionner un joueur", SelectPlayer())
        self.menu.add("auto", "Ajouter un joueur", AddPlayer())
        self.menu.add("auto", "q", EndScreenMenuController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler

class AddPlayer :
    pass # doit renvoyer à la liste de critère du joueur

class ReportMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        print("~~~~ Menu Rapports ~~~~")
        self.menu.add("auto","Séléctionner un tournoi", SelectTournament())
        self.menu.add("auto", "q", EndScreenMenuController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler

class PublishReportMenuController:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        self.menu.add("auto","Liste des acteurs", ListContributors())
        self.menu.add("auto", "Liste des joueurs", ListSelectPlayer())
        self.menu.add("auto", "Liste et résultats des rounds", ListResultRounds())
        self.menu.add("auto","Liste et résultats des matchs", ListResultMatches())
        self.menu.add("auto", "q", EndScreenMenuController())
        user_choice = self.view.get_user_choice()
        return user_choice.handler

class ListContributors:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        self.menu.add("auto","par odre alphabétique", AlphabeticalOrder())
        self.menu.add("auto", "par classement",RankOrder())
        user_choice = self.view.get_user_choice()
        return user_choice.handler

class ListSelectPlayer:
    def __init__(self):
        self.menu = Menu()
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        self.menu.add("auto", "par odre alphabétique", AlphabeticalOrder())
        self.menu.add("auto", "par classement", RankOrder())
        user_choice = self.view.get_user_choice()
        return user_choice.handler

class AlphabeticalOrder:
    pass # doit faire un trier alphabétique de la liste choisi

class RankOrder:
    pass #doir faire un trier par classement de la liste choisi

class ListResultRounds:
    pass # doit montrer la liste des round pour le tournois choisi

class ListResultMatches:
    pass # doit montrer la liste des matchs pour le tournois choisi

class EndScreenMenuController:
    pass

