from ..View.menu import ViewMenus
from ..Model.menu import Menu
from ..View.view import ViewPlayer
from ..Model.model import Player

class ControllerMenus:
    def __init__(self):
        self.view = ViewMenus()

    def Orga_menu_general(self):
        menu_info = self.menu.menu_general()
        print(*menu_info)
        while menu_info:
            if menu_info == "1":
                return menu_tournois()
            elif menu_info =="2":
                return menu_joueurs()
            elif menu_info =="3":
                return menu_rapports()
            elif menu_info == "4":
                pass #Quitter
            else :
                break

    def Orga_menu_tournois(self):
        menu_info = self.menu.menu_tournois()
        print(*menu_info)
        while menu_info:
            if menu_info == "1":
                pass # liste des tournois
            elif menu_info =="2":
                return Tournament()  # Créer un tournoi
            elif menu_info =="3":
                return menu_general()
            elif menu_info == "4":
                pass #Quitter
            else :
                break

    def Orga_menu_tournois_ouvert(self):
        menu_info = self.menu.menu_tournois_ouvert()
        print(*menu_info)
        while menu_info:
            if menu_info == "1":
                pass # Séléctionner un joueur
            elif menu_info =="2":
                pass  # Générer des paires
            elif menu_info =="3":
                return menu_pubier_rapport() # Publier un rapport
            elif menu_info =="4":
                pass  # Sauvegarder
            elif menu_info =="5":
                pass  # Clore le tournoi
            elif menu_info =="6":
                return menu_general()
            elif menu_info == "7":
                pass #Quitter
            else :
                break


    def Orga_menu_joueur(self):
        menu_info = self.menu.menu_joueur
        print(*menu_info)
        while menu_info:
            if menu_info == "1":
                pass #choisir un joueur
            elif menu_info =="2":
                return Player()
            elif menu_info =="3":
                return menu_rapports()
            elif menu_info == "4":
                pass #Quitter
            else :
                break


    def Orga_menu_selectionner_joueur(self):
        menu_info = self.menu.menu_joueur
        print(*menu_info)
        while menu_info:
            if menu_info == "1":
                pass #choisir un joueur
            elif menu_info =="2":
                return Player()
            elif menu_info =="3":
                return menu_rapports()
            elif menu_info == "4":
                pass #Quitter
            else :
                break

    def Orga_menu_rapports(self):
        menu_info = self.menu.menu_rapports()
        print(*menu_info)
        while menu_info:
            if menu_info == "1":
                pass # liste des tournois
                return menu_general()
            elif menu_info == "4":
                pass #Quitter
            else :
                break

    def Orga_menu_publier_rapport(self):
        menu_info = self.menu.menu_publier_rapport()
        print(*menu_info)
        while menu_info:
            if menu_info == "1":
                pass # Liste des acteurs
            elif menu_info =="2":
                pass  # Liste des joueurs
            elif menu_info =="3":
                pass # Liste et résultats des rounds
            elif menu_info =="4":
                pass  # Liste et résultats des matchs
            elif menu_info =="5":
                return menu_general()
            elif menu_info == "6":
                pass #Quitter
            else :
                break

    def Orga_menu_choix_affichage(self):
        menu_info = self.menu.choix_affichage()
        print(*menu_info)
        while menu_info:
            if menu_info == "1":
                # liste par ordre alpha
            elif menu_info =="2":
                # liste par ordre classement
            else :
                break


