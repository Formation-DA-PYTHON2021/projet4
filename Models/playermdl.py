from tinydb import TinyDB, Query, where

db = TinyDB("./mvc/db.json")
player_db = db.table('player_db')



class Player:

    def __init__(self, name,
                 first_name,
                 date_birth,
                 sexe,
                 classement):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.sexe = sexe
        self.classement = classement

    def serialized(player):
        serialized_player = {
            'name': player.name,
            'first_name': player.first_name,
            'date_birth': player.date_birth,
            'sexe': player.sexe,
            'classement': player.classement
        }
        return serialized_player

    def add(player):
        serialized_player = {
            'name': player.name,
            'first_name': player.first_name,
            'date_birth': player.date_birth,
            'sexe': player.sexe,
            'classement': player.classement
        }

        player_db.insert(serialized_player)

        print(db)



    def update(player):
        #name = db.search(where('name') == player.name)
        player_id = player_db.insert(player.serialized())
        player_db.update({'Id du joueur': player_id}, doc_ids=[player_id])

    def __str__(self):
        return f"{self.name} {self.first_name} {self.date_birth} {self.sexe} {self.classement}"


