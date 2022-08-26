from pojistenec import Pojistenec
from seznam_pojistencu import Seznam_pojistencu

seznam_pojistencu = Seznam_pojistencu()


# předvyplněný seznam pojištěnců
pojistenec_1 = Pojistenec("Jan", "Novák", 25, "226539619")
pojistenec_2 = Pojistenec("Petr", "Petřina", 55, "226539666")
pojistenec_3 = Pojistenec("Vladimir", "Novák", 41, "212369874")
pojistenec_4 = Pojistenec("Pavel", "Svoboda", 88, "365987561")

seznam_pojistencu.pridej(pojistenec_1)
seznam_pojistencu.pridej(pojistenec_2)
seznam_pojistencu.pridej(pojistenec_3)
seznam_pojistencu.pridej(pojistenec_4)


pokracuj = True
while pokracuj:
    print("----------------------")
    print("Evidence pojištěnců")
    print("----------------------")

    print("1 - Přidat nového pojištěnce")
    print("2 - Vypsat všechny pojištěnce")
    print("3 - Vyhledat pojištěnce")
    print("4 - Smazat pojištěnce")
    print("5 - Konec")

    # přidá nového pojištěnce    
    menu = int(input("Vyberte si akci: "))
    if menu == 1:
        menu1 = True
        while menu1:
            jmeno = input("Zadejte jméno pojištěnce: ")
            if !jmeno.isalpha()
                print("Musí obsahovat pouze písmena.")
                input("Pokračujte libovolnou klávesou...")
                break

            prijmeni = input("Zadejte příjmení: ")
            x = (prijmeni.isalpha())
            if x == True:
                pass
            else:
                print("Musí obsahovat pouze písmena.")
                input("Pokračujte libovolnou klávesou...")
                break

            tel_cislo = input("Zadejte telefonní číslo: ")
            y = (tel_cislo.isdigit())
            if y == True:
                pass
            else:
                print("Musí obsahovat pouze čísla.")
                input("Pokračujte libovolnou klávesou...")
                break

            vek = input("Zadejte věk: ")
            y = (vek.isdigit())
            if y == True:
                pass
            else:
                print("Musí obsahovat pouze čísla.")
                input("Pokračujte libovolnou klávesou...")
                break

            print(jmeno, prijmeni, tel_cislo, vek)
            seznam_pojistencu.pridej(Pojistenec(jmeno, prijmeni, vek, tel_cislo))
            input("\nData byla uložena. Pokračujte libovolnou klávesou...")
            menu1 = False 

    # vypíše všechny pojištence v seznamu
    elif menu == 2:
        for p in seznam_pojistencu.pojistenci:
            print(p)
        input("\nPokračujte libovolnou klávesou...")

    # vyhledá pojištěnce dle jména a příjmení
    elif menu == 3:
        jmeno = input("Zadejte jméno pojištěnce: ")
        prijmeni = input("Zadejte příjmení pojištěnce: ")
        poradi, nalezeny_pojistenec = seznam_pojistencu.vyhledej(jmeno, prijmeni)
        if poradi != -1:
            print("\n{0}, {1}, {2}, {3}".format(nalezeny_pojistenec.jmeno, nalezeny_pojistenec.prijmeni, nalezeny_pojistenec.vek, nalezeny_pojistenec.tel_cislo))
        else:
            print("\nPojištěnec nenalezen.")
            input("\nPokračujte libovolnou klávesou...")    

    # vyhledá pojištěnce dle jména a příjmení, pokud je nalezen, lze potvrdit smazání pojištěnce ze seznamu
    elif menu == 4:
        jmeno = input("Zadejte jméno pojištěnce: ")
        prijmeni = input("Zadejte příjmení pojištěnce: ")
        poradi, nalezeny_pojistenec = seznam_pojistencu.vyhledej(jmeno, prijmeni)
        if nalezeny_pojistenec != None:
            opravdu_smazat = input("\nNašli jsme pojištěnce: {0}. Chcete ho opravdu smazat [y/n]".format(nalezeny_pojistenec))
            if opravdu_smazat == "y":
                seznam_pojistencu.smaz(poradi)
        else:
            print("\nNenašli jsme pojištěnce: {0}{1}".format(jmeno, prijmeni))
            input("\nPokračujte libovolnou klávesou...")

    # ukončí aplikaci        
    elif menu == 5:
        pokracuj = False
