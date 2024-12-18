from tic_tac_toe_game import TikTakToeGame

class TikTakToeGameStatus:
    def __init__(self, game:TikTakToeGame, status, winner):
        self._game = game
        self._status = status
        self._winner = winner

    def get_game(self):
        return self._game

    def get_status(self):
        return self._status

    def get_winner(self):
        return self._winner

    def set_status(self, state):
        self._status = state

    def set_winner(self, winner):
        self._winner = winner

        
