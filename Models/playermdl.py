from tinydb import TinyDB

db = TinyDB("./mvc/db.json")
player_db = db.table('player_db')


class Player:

    def __init__(self, name, first_name, date_birth,
                 genre, ranking, player_played, number_points=0):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.genre = genre
        self.player_played = player_played
        self.ranking = ranking
        self.number_points = number_points

    def serialized(player):
        serialized_player = {
            'name': player.name,
            'first_name': player.first_name,
            'date_birth': player.date_birth,
            'genre': player.genre,
            'ranking': player.ranking,
            'player_played': player.player_played,
            'number_points': player.number_points
        }
        return serialized_player

    def add(player):
        serialized_player = {
            'name': player.name,
            'first_name': player.first_name,
            'date_birth': player.date_birth,
            'genre': player.genre,
            'ranking': player.ranking,
            'player_played': player.player_played,
            'number_points': player.number_points
        }

        player_db.insert(serialized_player)

        print(db)

    def update(player):
        player_id = player_db.insert(player.serialized())
        player_db.update({'Id du joueur': player_id}, doc_ids=[player_id])

    def __str__(self):
        return f"{self.name} {self.first_name} {self.date_birth} {self.genre} {self.ranking}"
