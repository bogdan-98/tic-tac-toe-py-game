from repository.tic_tac_toe_repository import TikTakToeRepository

class TikTakToeServices:
    def __init__(self, repository: TikTakToeRepository):
        self.lista = repository
        self._castigator = '?'

    def keep_track_of_winner(self):
        return self._castigator == '?'

    def return_winner(self):
        return self._castigator

    def check_for_unfinished_games(self):
        lista = self.lista.look_for_unfinished_games()
        return lista

    def play(self, nr_joc, line, column):
        table = self.lista.look_for_a_game(nr_joc).get_table()
        joc_neterminat = self.lista.check_if_unfinished(nr_joc)

        msg = []

        if joc_neterminat:
            index = (line - 1) * 3 + (column - 1)

            self.lista.look_for_a_game(nr_joc).set_numar_x(table.count('X'))
            self.lista.look_for_a_game(nr_joc).set_numar_0(table.count('0'))

            if self.lista.look_for_a_game(nr_joc).get_numar_x() == self.lista.look_for_a_game(nr_joc).get_numar_0():
                if table[index] != 'X' and table[index] != '0':
                    table[index] = 'X'
                else:
                    msg.append("Coordonatele acestea sunt deja folosite!")

            elif self.lista.look_for_a_game(nr_joc).get_numar_x() > self.lista.look_for_a_game(nr_joc).get_numar_0():
                if table[index] != 'X' and table[index] != '0':
                    table[index] = '0'
                else:
                    msg.append("Coordonatele acestea sunt deja folosite!")

            elif self.lista.look_for_a_game(nr_joc).get_numar_x() < self.lista.look_for_a_game(nr_joc).get_numar_0():
                if table[index] != 'X' and table[index] != '0':
                    table[index] = 'X'
                else:
                    msg.append("Coordonatele acestea sunt deja folosite!")

            self.lista.look_for_a_game(nr_joc).set_numar_x(table.count('X'))
            self.lista.look_for_a_game(nr_joc).set_numar_0(table.count('0'))

            self.lista.look_for_a_game(nr_joc).set_table(table)
            self.lista.update_game_file()

            if self.lista.look_for_a_game(nr_joc).get_numar_x()  + self.lista.look_for_a_game(nr_joc).get_numar_0()  == 9 or self.lista.verifica_castigatorul_jocului(table) is not None:
                self._castigator = self.lista.verifica_castigatorul_jocului(table)

            return msg

    def return_which_player(self, nr_joc):
        if self.lista.look_for_a_game(nr_joc).get_numar_x() == self.lista.look_for_a_game(nr_joc).get_numar_0():
            return 'X'
        elif self.lista.look_for_a_game(nr_joc).get_numar_x() > self.lista.look_for_a_game(nr_joc).get_numar_0():
            return '0'
        elif self.lista.look_for_a_game(nr_joc).get_numar_x() < self.lista.look_for_a_game(nr_joc).get_numar_0():
            return 'X'

    def read_games_from_file(self):
        self.lista.read_games_from_file()
