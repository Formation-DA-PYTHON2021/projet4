

class Player:
    def __init__(self, name, first_name, date_birth, sexe, classement):
        player = Player(name, first_name, date_birth, sexe, classement)
        serialized_player = {
            'name': player.name,
            'first_name': player.first_name,
            'date_birth': player.date_birth,
            'sexe': player.sexe,
            'classement': player.classement
        }
        self.name = serialized_player['name']
        self.first_name = serialized_player['first_name']
        self.date_birth = serialized_player['date_birth']
        self.sexe = serialized_player['sexe']
        self.classement = serialized_player['classement']


    def __str__(self):
        return f"{self.name} {self.first_name} {self.date_birth} {self.sexe} {self.classement}"
