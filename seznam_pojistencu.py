
class Seznam_pojistencu():

    pojistenci = []

    # přidá pojištěnce do seznamu    
    def pridej(self, pojistenec):
        self.pojistenci.append(pojistenec)

    # smaže pojištěnce dle pozice pokud existuje
    def smaz(self, pozice):
        if pozice >= 0 and pozice < len(self.pojistenci): 
            del(self.pojistenci[pozice])
        else: 
            print("Špatné parametry pro smazání, index {0} zřejmě neexistuje".format(pozice))

    # vyhledá počet pojištěnců v seznamu a dle jména/přijmení a vrátí jejich pořadí
    def vyhledej(self, jmeno, prijmeni):
        for i in range (len(self.pojistenci)):
            if self.pojistenci[i].prijmeni == prijmeni and self.pojistenci[i].jmeno == jmeno:
                return i, self.pojistenci[i]
        return -1, None        

    
    def __repr__(self):            
        return str("Jméno: {0}, Přijmení: {1}, věk: {2}, Telefonní číslo: {3}".format(self.jmeno, self.prijmeni, self.vek, self.tel_cislo))

         
    