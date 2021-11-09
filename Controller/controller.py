from ..View.view import ViewPlayer
from ..Model.model import Player


class ControllerPlayer:
    def __init__(self):
        self.view = ViewPlayer()

    def start(self):
        players_info = self.view.info()
        print(*players_info)
        player1 = Player(*players_info)


if __name__ == "__main__":
    app = ControllerPlayer()
    app.start()
