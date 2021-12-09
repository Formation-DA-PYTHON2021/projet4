from ..Views.playerview import ViewPlayer
from ..Models.playermdl import Player


class ControllerPlayer:
    def __init__(self):
        self.view = ViewPlayer()

    def __call__(self):
        players_info = self.view.info()
        print(*players_info)
        player1 = Player(*players_info)
        return Player.update(player1)