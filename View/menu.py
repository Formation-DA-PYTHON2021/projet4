

class HomeMenuView:
        def __init__(self, menu):
                self.menu = menu

        def _display_menu(self):
                for key, entry in self.menu.items():
                        print(f"{key}: {entry.option}")
                print()

        def get_user_choice(self):
                while True:
                        self._display_menu() # 1 afficher le menu à l'utilisateur
                        choice = input("Entrez votre choix : ") # 2 demander à l'utilisateur de faire un choix
                        if choice in self.menu : # 3 valider le choix de l'utilisateur
                                print()
                                return self.menu[choice] # 4 retourner le choix de l'utilisateur


class TournamentMenuController:
        def __init__(self):
                self.menu = menu

        def _display_menu(self):
                print("-------- Menu Tournoi -------")
                for key, entry in self.menu.items():
                        print(f"{key}: {entry.option}")
                print()

        def get_user_choice(self):
                while True:
                        self._display_menu()  # 1 afficher le menu à l'utilisateur
                        choice = input("Entrez votre choix : ")  # 2 demander à l'utilisateur de faire un choix
                        if choice in self.menu:  # 3 valider le choix de l'utilisateur
                                print()
                                return self.menu[choice]  # 4 retourner le choix de l'utilisateur

class OpenTournamentMenuController:
        def __init__(self, menu):
                self.menu = menu

        def _display_menu(self):
                print("-------- Menu Tournoi en cours -------")
                for key, entry in self.menu.items():
                        print(f"{key}: {entry.option}")
                print()

        def get_user_choice(self):
                while True:
                        self._display_menu() # 1 afficher le menu à l'utilisateur
                        choice = input("Entrez votre choix : ") # 2 demander à l'utilisateur de faire un choix
                        if choice in self.menu : # 3 valider le choix de l'utilisateur
                                print()
                                return self.menu[choice] # 4 retourner le choix de l'utilisateur

class PlayerMenuController:
        def __init__(self, menu):
                self.menu = menu

        def _display_menu(self):
                print("-------- Menu Joueurs -------")
                for key, entry in self.menu.items():
                        print(f"{key}: {entry.option}")
                print()

        def get_user_choice(self):
                while True:
                        self._display_menu() # 1 afficher le menu à l'utilisateur
                        choice = input("Entrez votre choix : ") # 2 demander à l'utilisateur de faire un choix
                        if choice in self.menu : # 3 valider le choix de l'utilisateur
                                print()
                                return self.menu[choice] # 4 retourner le choix de l'utilisateur

class ReportMenuController:
        def __init__(self, menu):
                self.menu = menu

        def _display_menu(self):
                print("-------- Menu Rapports -------")
                for key, entry in self.menu.items():
                        print(f"{key}: {entry.option}")
                print()

        def get_user_choice(self):
                while True:
                        self._display_menu() # 1 afficher le menu à l'utilisateur
                        choice = input("Entrez votre choix : ") # 2 demander à l'utilisateur de faire un choix
                        if choice in self.menu : # 3 valider le choix de l'utilisateur
                                print()
                                return self.menu[choice] # 4 retourner le choix de l'utilisateur

class PublishReportMenuController:
        def __init__(self, menu):
                self.menu = menu

        def _display_menu(self):
                print("-------- Menu publier un rapport -------")
                for key, entry in self.menu.items():
                        print(f"{key}: {entry.option}")
                print()

        def get_user_choice(self):
                while True:
                        self._display_menu()  # 1 afficher le menu à l'utilisateur
                        choice = input("Entrez votre choix : ")  # 2 demander à l'utilisateur de faire un choix
                        if choice in self.menu:  # 3 valider le choix de l'utilisateur
                                print()
                                return self.menu[choice]  # 4 retourner le choix de l'utilisateur

class ListContributors:
        def __init__(self, menu):
                self.menu = menu

        def _display_menu(self):
                for key, entry in self.menu.items():
                        print(f"{key}: {entry.option}")
                print()

        def get_user_choice(self):
                while True:
                        self._display_menu() # 1 afficher le menu à l'utilisateur
                        choice = input("Entrez votre choix : ") # 2 demander à l'utilisateur de faire un choix
                        if choice in self.menu : # 3 valider le choix de l'utilisateur
                                print()
                                return self.menu[choice] # 4 retourner le choix de l'utilisateur

class ListSelectPlayer:
        def __init__(self, menu):
                self.menu = menu

        def _display_menu(self):
                for key, entry in self.menu.items():
                        print(f"{key}: {entry.option}")
                print()

        def get_user_choice(self):
                while True:
                        self._display_menu() # 1 afficher le menu à l'utilisateur
                        choice = input("Entrez votre choix : ") # 2 demander à l'utilisateur de faire un choix
                        if choice in self.menu : # 3 valider le choix de l'utilisateur
                                print()
                                return self.menu[choice] # 4 retourner le choix de l'utilisateur
