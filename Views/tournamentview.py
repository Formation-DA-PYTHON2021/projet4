

class ViewTournament:
    def info (self):
            name = input("Entrez le nom du tournoi : ")
            name_site = input("Entrez le lieu du tournoi : ")
            start_date = input("Entrez la date de début du tournois (JJ/MM/AAA) : ")
            end_date = input("Entrez la date de fin du tournois (JJ/MM/AAA): ")
            description_tournament = input("Description du tournois : ")
            tournament_id = input("Entrez l'identifiant du tournois : ")
            tournaments_info = []
            tournaments_info.extend((name, name_site, start_date,end_date, description_tournament, tournament_id))
            return tournaments_info