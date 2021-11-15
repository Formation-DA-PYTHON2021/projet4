

class ViewTournament:
    def info (self):
            name = input("Entrez le nom du tournoi : ")
            name_site = input("Entrez le lieu du tournoi : ")
            start_date = input("Entrez la date de début du tournois (JJ/MM/AAA) : ")
            end_date = input("Entrez la date de fin du tournois (JJ/MM/AAA): ")
            tournaments_info = []
            tournaments_info.extend((name, name_site, start_date,end_date))
            return tournaments_info