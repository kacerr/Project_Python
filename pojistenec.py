
class Pojistenec():

    jmeno = None
    prijmeni = None
    vek = None
    tel_cislo = None

    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo
         
    def __repr__(self):
        return str("Pojistenec: jmeno: {0}, prijmeni: {1}".format(self.jmeno, self.prijmeni))

         
    def __str__(self):
        return str("jméno: {0}, přijmení: {1}, věk: {2}, telefonní číslo: {3}".format(self.jmeno, self.prijmeni, self.vek, self.tel_cislo))