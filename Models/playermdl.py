

class Player:
    def __init__(self, name, first_name, date_birth, sexe, classement):
        self.name = name
        self.first_name = first_name
        self.date_birth = date_birth
        self.sexe = sexe
        self.classement = classement

    def __str__(self):
        return f"{self.name} {self.first_name} {self.date_birth} {self.sexe} {self.classement}"
