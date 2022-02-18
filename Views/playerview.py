

class ViewPlayer:
    def info (self):
        name = input("Entrez le nom : ")
        first_name = input("Entrez le prénom : ")
        date_birth = input("Entrez la date de naissance (JJ/MM/AAAA) : ")
        genre = input("Entrez le sexe (F/M) : ")
        ranking = int(input("Entrez le classement : "))
        player_played = []
        players_info = []
        players_info.extend((name,first_name,date_birth,genre,ranking, player_played))
        return players_info
