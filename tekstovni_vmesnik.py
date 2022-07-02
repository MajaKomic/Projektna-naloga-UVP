from model import Stanje, Semester, Predmet

IME_DATOTEKE = "stanje.json"   
try:
    moje_stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    moje_stanje = Stanje()

DODAJ_SEMESTER = 1
POBRISI_SEMESTER = 2
ZAMENJAJ_SEMESTER = 3
DODAJ_PREDMET = 4
POBRISI_PREDMET = 5
ZAMENJAJ_PREDMET = 6
OPRAVIL_PREDMET = 7
DODAJ_IZPITNI_ROK = 8
POBRISI_IZPITNI_ROK = 9 
DODAJ_OCENO = 10
IZBRISI_OCENO = 11
IZHOD = 12

#OPOMBA: lahko bi dodala tudi funkcijo UREDI
#IDEJA: ugotovi kako bi dodala da si usak napiše urnik za semester (dodaj sliko ali pa vnesi predmete ročno)

def preberi_stevilo():
    while True:
        vnos = input("> ")
        try:
            return int(vnos)
        except ValueError:
            print("Vnesti morate število.")

def izberi_moznost(moznosti):
    """uporabniku nasteje moznosti in vrne izbrano"""
    for i, (_moznost, opis) in enumerate(moznosti, 1):
        print(f"{i} {opis}")
    while True:
        i = preberi_stevilo()
        if 1 <= i <= len(moznosti):
            moznosti, _opis = moznosti[i - 1]
            return moznosti
        else:
            print(f"Vnesti morate število med 1 in {len(moznosti)}")

def prikazi_pozdravno_sporocilo():
    print("Pozdravljeni")

# TEKSTOVNI UMESNIK
def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        prikazi_aktualni_semester()
        ukaz = izberi_moznost(
            [
                (DODAJ_SEMESTER, "dodaj nov semester"),
                (POBRISI_SEMESTER, "pobriši semester"),
                (DODAJ_PREDMET, "dodaj nov predmet"),
                (POBRISI_PREDMET, "pobriši predmet"),
                (OPRAVIL_PREDMET, "predmet je opravljen"),
                (IZHOD, "zapri program")
            ]
        )
        if ukaz == DODAJ_SEMESTER:
            dodaj_semester()
        elif ukaz == POBRISI_SEMESTER:
            pobrisi_semester()
        elif ukaz == DODAJ_PREDMET:
            dodaj_predmet()
        elif ukaz == POBRISI_PREDMET:
            pobrisi_predmet()
        elif ukaz == OPRAVIL_PREDMET:
            opravljen_predmet()
        elif ukaz == IZHOD:
            moje_stanje.shrani_v_datoteko(IME_DATOTEKE)
            print("Nasvidenje")
            break

# VSE FUNKCIJE S SEMESTRI
def dodaj_semester():
    print("Vnesite podatke o semestru.")
    ime = input("Ime> ")
    nov_semester = Semester(ime)
    moje_stanje.dodaj_semester(nov_semester)

def prikaz_semestra(semester):
    neopravljeni = semester.stevilo_neopravljenih_predmetov()
    if neopravljeni:
        return f'{semester.ime_semestra} ({neopravljeni} neopravljenih predmetov)'
    else:
        return f'{semester.ime_semestra} (vsi premeti opravljeni)'

def prikazi_aktualni_semester():
    #ugotovi kako to naredit
    pass

def izberi_semester(stanje):
    return izberi_moznost([(semester, prikaz_semestra(semester)) for semester in stanje.semestri])

def zamenjaj_semester():
    print('Izberite semester na katerega bi preklopili.')
    semester = izberi_semester(moje_stanje)
    moje_stanje.zamenjaj_semester(semester)

def pobrisi_semester(): 
    semester = izberi_semester(moje_stanje)
    moje_stanje.pobrisi_semester(semester)

# VSE FUNKCIJE S PREDMETI
def dodaj_predmet():
    print("Vnesite podatke o predmetu.")
    ime = input("Ime> ")
    opis = input("Opis> ")
    kreditne_tocke = input("Krednitne točke> ")
    nov_predmet = Predmet(ime, opis, kreditne_tocke)
    moje_stanje.dodaj_predmet(nov_predmet)

def prikaz_predmeta(predmet):
    if predmet.opravljen == True:
        return f'{predmet.ime_predmeta} je opravljen'
    else:
        return f'Naslednji rok: {predmet.naslednji_izpitni_rok()} ({predmet.ime_predmeta})'

def izberi_predmet(stanje):
    return izberi_moznost([(predmet, prikaz_predmeta(predmet)) for predmet in stanje.aktualni_semester.predmet])   # nikjer ni definiran aktualni semester

def prikazi_aktualne_predmete():
    pass 

def pobrisi_predmet():
    predmet = izberi_predmet(moje_stanje)
    moje_stanje.pobrisi_predmet(predmet)

def opravljen_predmet():
    predmet = izberi_predmet(moje_stanje)
    predmet.opravil_predmet()

tekstovni_vmesnik()