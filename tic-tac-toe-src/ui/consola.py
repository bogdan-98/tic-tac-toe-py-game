from services.tic_tac_toe_services import TikTakToeServices

class Consola:
    def __init__(self, services: TikTakToeServices):
        self._lista = services

    def printeaza_meniu(self):
        print("Meniu:")
        print("Verifica jocurile neterminate.")
        print("Joaca.")

    def construieste_matrice_afisaj(self, table):
        matrice = [[None for _ in range(3)] for _ in range(3)]

        for index, elem in enumerate(table):
            row = index // 3
            col = index % 3
            matrice[row][col] = elem

        return matrice

    def verifica_jocurile_neterminate_ui(self):
        lista = self._lista.check_for_unfinished_games()
        print(lista)

    def play_game(self):
        numar_joc = int(input("Introdu numarul jocului:"))

        if self._lista.lista.check_if_unfinished(numar_joc):
            while self._lista.keep_track_of_winner():
                matrice_afisaj = self.construieste_matrice_afisaj(self._lista.lista.look_for_a_game(numar_joc).get_table())
                for row in matrice_afisaj:
                    print(row)
                print("Randul jucatorului:" + str(self._lista.return_which_player(numar_joc)))
                line = int(input("Introdu linia:"))
                coloana = int(input("Introdu coloana:"))
                msg = self._lista.play(numar_joc, line, coloana)
                if len(msg) > 0:
                    print(msg[0])

            if self._lista.return_winner() == 'X':
                print("Jocul s-a terminat! Castigatorul este jucatorul X! Felicitari!")
            elif self._lista.return_winner() == '0':
                print("Jocul s-a terminat! Castigatorul este jucatorul 0! Felicitari!")
            elif self._lista.return_winner() is None:
                print("Jocul s-a terminat la egalitate!")
        else:
            print("Meciul acesta s-a terminat deja cu victoria pentru jucatorul " + str(self._lista.lista.verifica_castigatorul_jocului(self._lista.lista.look_for_a_game(numar_joc).get_table())) + "!")


    def run(self):
        self._lista.read_games_from_file()
        while True:
            self.printeaza_meniu()
            cmd = input(">>>")

            match cmd:
                case "jocuri_neterminate":
                    self.verifica_jocurile_neterminate_ui()
                case "joaca":
                    self.play_game()
                case "iesire":
                    print("Iesire...")
                    break
