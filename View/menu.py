

class ViewMenus:
    def menu_general(self):
        print("""
        -------- Menu Général -------
        1 Tournois
        2 Joueurs
        3 Rapports
        4 Quitter 
        """)
        ans = input("Entrez le numéro correspondant : ")
        menu_info = []
        menu_info.extend((ans))
        return menu_info

    def menu_tournois(self):

        print("""
         -------- Menu Tournois -------
        1 Séléctionner un tournoi
        2 Créer un tournoi
        3 Revenir au menu général
        4 Quitter
        """)
        ans = input("Entrez le numéro correspondant : ")
        menu_info = []
        menu_info.extend((ans))
        return menu_info

    def menu_tournoi_ouvert(self):
        print("""
        1 Séléctionner un joueur
        2 Générer des paires
        3 Publier un rapport
        4 Sauvagarder
        5 Clore le tournoi
        6 Revenir au menu général
        7 Quitter 
           """)
        ans = input("Entrez le numéro correspondant : ")
        menu_info = []
        menu_info.extend((ans))
        return menu_info

    def menu_joueurs(self):
        print("""
        -------- Menu Joueurs -------
        1 choisir un joueur 
        2 Ajouter un joueur
        3 Revenir au menu général
        4 Quitter 
        """)
        ans = input("Entrez le numéro correspondant : ")
        menu_info = []
        menu_info.extend((ans))
        return menu_info

    def menu_selectionner_joueurs(self):
        print("""
        1 choisir un joueur 
        2 Ajouter un joueur
        3 Revenir au menu général
        4 Quitter 
        """)
        ans = input("Entrez le numéro correspondant : ")
        menu_info = []
        menu_info.extend((ans))
        return menu_info

    def menu_rapports(self):
        print("""
        -------- Menu Rapports -------
        1 Séléctionner un tournoi
        3 Revenir au menu général
        4 Quitter 
        """)
        ans = input("Entrez le numéro correspondant : ")
        menu_info = []
        menu_info.extend((ans))
        return menu_info

    def menu_pubier_rapport(self):
        print("""
        1 Liste des acteurs
        2 Liste des joueurs
        3 Liste et résultats des rounds
        4 Liste et résultats des matchs
        5 Revenir au menu général
        6 Quitter 
            """)
        ans = input("Entrez le numéro correspondant : ")
        menu_info = []
        menu_info.extend((ans))
        return menu_info

    def menu_choix_affichage(self):
        print("""
        1 par odre alphabétique
        2 par classement
            """)
        ans = input("Entrez le numéro correspondant : ")
        menu_info = []
        menu_info.extend((ans))
        return menu_info


