class TikTakToeGame:
    def __init__(self, nr_joc:int, table, numar_x, numar_0):
        self._nr_joc = nr_joc
        self._table = table
        self._numar_x = numar_x
        self._numar_0 = numar_0

    def get_nr_joc(self):
        return self._nr_joc

    def get_table(self):
        return self._table

    def set_nr_joc(self, nr_joc):
        self._nr_joc = nr_joc

    def set_table(self, table):
        self._table = table

    def get_numar_x(self):
        return self._numar_x

    def set_numar_x(self, numar_x):
        self._numar_x = numar_x

    def get_numar_0(self):
        return self._numar_0

    def set_numar_0(self, numar_0):
        self._numar_0 = numar_0

