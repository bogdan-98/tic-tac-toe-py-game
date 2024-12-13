from domain.tic_tac_toe_game import TikTakToeGame
from domain.tic_tac_toe_game_status import TikTakToeGameStatus

class TikTakToeRepository:
    def __init__(self, nume_fisier):
        self._lista_jocuri = []
        self._lista_stari = []
        self._nume_fisier = nume_fisier

    def _add_games(self, game: TikTakToeGame):
        self._lista_jocuri.append(game)

    def _add_stare(self, stare:TikTakToeGameStatus):
        self._lista_stari.append(stare)

    def check_if_unfinished(self, nr_joc):
        for e in self._lista_stari:
            if e.get_game().get_nr_joc() == nr_joc and e.get_status() == "Unfinished":
                return True
        return False

    def look_for_a_game(self, nr_joc):
        for elem in self._lista_jocuri:
            if elem.get_nr_joc() == nr_joc:
                return elem

    def look_for_unfinished_games(self):
        lista = []
        for elem in self._lista_stari:
            if elem.get_status() == "Unfinished":
                lista.append(elem.get_game().get_nr_joc())
        return lista

    def verifica_joc_complet(self, tabela):
        if len(tabela) == 9:
            if '' not in tabela:
                return True
        return False

    def verifica_castigatorul_jocului(self, tabela):
        numar_x = tabela.count('X')
        numar_0 = tabela.count('0')

        if not (
                (numar_x == numar_0 or numar_x == numar_0 + 1 or numar_x + 1 == numar_0 or numar_0 == numar_x + 1)
        ):
            raise ValueError("Joc invalid: numerele de X și 0 nu sunt corecte.")

        matrice_tabela = [tabela[i:i + 3] for i in range(0, len(tabela), 3)]

        if matrice_tabela[0][0] == matrice_tabela[1][1] == matrice_tabela[2][2] and matrice_tabela[0][0] not in [None,
                                                                                                                 ' ']:
            return matrice_tabela[0][0]
        if matrice_tabela[0][2] == matrice_tabela[1][1] == matrice_tabela[2][0] and matrice_tabela[0][2] not in [None,
                                                                                                                 ' ']:
            return matrice_tabela[0][2]

        for i in range(3):
            if matrice_tabela[i][0] == matrice_tabela[i][1] == matrice_tabela[i][2] and matrice_tabela[i][0] not in [
                None, ' ']:
                return matrice_tabela[i][0]

        for i in range(3):
            if matrice_tabela[0][i] == matrice_tabela[1][i] == matrice_tabela[2][i] and matrice_tabela[0][i] not in [
                None, ' ']:
                return matrice_tabela[0][i]

        return None

    def read_games_from_file(self):
        with open(self._nume_fisier, "r") as file:
            for line in file:
                line = line.strip()
                line_members = line.split(",")
                nr_joc = int(line_members[0])
                continut_tabela = line_members[1:10]
                joc = TikTakToeGame(nr_joc, continut_tabela, 0, 0)
                if self.verifica_castigatorul_jocului(continut_tabela) is not None:
                    stare = TikTakToeGameStatus(joc, "Finished", self.verifica_castigatorul_jocului(continut_tabela))
                else:
                    if self.verifica_joc_complet(continut_tabela):
                        stare = TikTakToeGameStatus(joc, "Draw", "-")
                    else:
                        stare = TikTakToeGameStatus(joc, "Unfinished", "-")
                self._lista_jocuri.append(joc)
                self._lista_stari.append(stare)

    def update_game_file(self):
        with open(self._nume_fisier, "w") as file:
            for joc in self._lista_jocuri:
                extracted_game = joc.get_table()
                result = str(joc.get_nr_joc()) + ","
                result += ",".join(str(elem) for elem in extracted_game) + ","
                file.write(result + "\n")

