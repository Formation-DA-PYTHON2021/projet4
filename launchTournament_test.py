from .Views.tournamentview import ViewTournament
from .Models.playermdl import Player
from .Models.tournamentsmdl import Tournament
from .Models import tournamentsmdl

from tinydb import TinyDB, Query, where

db = TinyDB("./mvc/db.json")
player_db = db.table('player_db')
tournament_db = db.table('tournament_db')


class Match:
    def info(self, player1, score1, player2, score2):
        self.player1 = [player1, score1]
        self.player2 = [player2, score2]


class LaunchTournament:

    def selectournament(self):
        dispalytournament = tournament_db.all()
        tournaments = []
        for i in dispalytournament:
            print(i['name'])
            selectournament = str(input("choisir un tournoi. Rentrer son nom : "))
        if selectournament in tournaments:
            return selectournament
        #print list tournament + faire demander un choix + selctionner (voir avec cll)

    def first_round(self, round):
        """classer la liste par ranking (fonct : sort ou sorted)"""
        players_match = ViewTournament.assign_player()
        players_match_sort = sorted(players_match, key=lambda player: player.ranking)
        """diviser la liste en 2 listes"""
        players_match_l1 = players_match_sort[0:3]
        players_match_l2 = players_match_sort[4:9]
        """association"""
        for i in players_match_sort:
            match = Match(players_match_l1[i], 0, players_match_l2[i], 0)
            players_match_l1[i].add(players_match_l2[i])
            players_match_l2.add(players_match_l1[i])
            round.addMatch(match)
        print("les matchs du premier round sont les suivants : ")
        for m in round.instances_match:
            print(m.player1[0].name + "vs" + m.player2[0].name)
        return round
    # match : modifier score + ad resultat

    def next_round(self):
        pass

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


    def assign_color(self):
        pass

    def enter_result_match(self):
        #print("Veuillez entrer le résultat du match.")
        #print("Vainqueur" str() + "1" )

        pass

    def update_total_results(self):
        pass

    def update_rankings(self):
        pass

    def save_tournament(self):
        pass