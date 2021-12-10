from .Views.tournamentview import ViewTournament
from .Models.playermdl import Player

from tinydb import TinyDB, Query, where

db = TinyDB("./mvc/db.json")
player_db = db.table('player_db')

class LaunchTournament:

    def round(self, name, start_date_time, end_date_time):
        self.name = name
        self.start_date_time = start_date_time
        self.end_date_time = end_date_time
        self.instances_match = []

    def match(self, players_match, player_rank):
        self.players_match = ViewTournament.assign_player()
        self.player_rank = Player.add()
        self.rankink = db.search(where('ranking') == player_rank.ranking)

    def open_tournament(self):
        self.round()
        self.instances_round = []
        self.match()
        self.instances_match = []

    def first_round(self):
        self = self.generate_pairs_first_round() + self.assign_color() + \
               self.enter_result_match() + self.update_total_results()

    def next_round(self):
        cmpt = 0
        roundsnext = []
        while cmpt < 3:
            roundnext = self.generate_pairs_next_round() + self.assign_color() + \
                         self.enter_result_match() + self.update_total_results()
            roundsnext.append(roundnext)
            cmpt += 1

    def generate_pairs_first_round(self, players_match, ranking):
        pass

    def generate_pairs_next_round(self):
        pass

    def assign_color(self):
        pass

    def enter_result_match(self):
        pass

    def update_total_results(self):
        pass

    def update_rankings(self):
        pass

    def save_tournament(self):
        pass