

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