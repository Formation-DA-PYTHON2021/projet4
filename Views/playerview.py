

class ViewPlayer:
    def info (self):
        i = 0
        while i < 1:
            name = input("Entrez le nom : ")
            first_name = input("Entrez le prénom : ")
            date_birth = input("Entrez la date de naissance (JJ/MM/AAA) : ")
            sexe = input("Entrez le sexe (F/M) : ")
            ranking = int(input("Entrez le classement : "))
            players_info = []
            players_info.extend((name,first_name,date_birth,sexe,ranking))
            i += 1
        return players_info
