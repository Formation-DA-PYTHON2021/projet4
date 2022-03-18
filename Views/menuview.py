class HomeMenuView:
    def __init__(self, menu):
        self.menu = menu

    def _display_menu(self):
        print("-------------------------------------------------\n"
              "                  Menu Principal                 \n"
              "-------------------------------------------------")
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")
        print()

    def get_user_choice(self):
        while True:
            self._display_menu()
            choice = input("Entrez votre choix : ")
            if choice in self.menu:
                print()
                return self.menu[choice]
