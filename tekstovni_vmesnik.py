from datetime import date
from model import Stanje, Semester, Predmet

IME_DATOTEKE = "stanje.json"   
try:
    moje_stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:   
    moje_stanje = Stanje(semestri=[])

DODAJ_SEMESTER = 1
POBRISI_SEMESTER = 2
DODAJ_PREDMET = 3
POBRISI_PREDMET = 4
IZHOD = 5

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

def prikaz_semestra(semester):
    return f"{semester.ime_semestra}"

def prikaz_predmeta(predmet):
    if predmet.opravljen:
        return f"{predmet.ime_predmeta} je opravljen"
    else:
        return f"{predmet.ime_predmeta}"

def izberi_semester(moje_stanje):
    print("Izberi semester:")
    return izberi_moznost(
        [
            (semester, prikaz_semestra(semester)) 
            for semester in moje_stanje.semestri
        ]
    )

def izberi_predmet(semester):
    print("Izberi predmet:")
    return izberi_moznost(
        [
            (predmet, prikaz_predmeta(predmet)) 
            for predmet in semester.predmeti
        ]
    ) 

def trenutno_stanje():
    print("Vaše trenutno stanje:")
    for semester in moje_stanje.semestri:
        print(f"{prikaz_semestra(semester)}")
        for predmet in semester.predmeti:
            print(f"    {prikaz_predmeta(predmet)}")
    if not moje_stanje.semestri:
        print("Trenutno nimate še nobenega semestra, prosimo ustvarite enega.")

def dodaj_semester():
    ime = input("Ime> ")
    nov = Semester(ime, [])
    moje_stanje.dodaj_semester(nov)

def pobrisi_semester():
    if not moje_stanje.semestri:
        return print("Nimate nobenega semestra zato dodajte enega.")
    else:
        semester = izberi_semester(moje_stanje)
        moje_stanje.pobrisi_semester(semester)

def dodaj_predmet():
    if not moje_stanje.semestri:
        return print("Nimate nobenega semestra zato dodajte enega.")
    else:
        semester = izberi_semester(moje_stanje)
        print("Vnesite podatke o predmetu.")
        ime_predmeta = input("Ime> ")
        predavatelj = input("Predavatelj> ")
        asistent = input("Asistent> ")
        kreditne_tocke = input("Krednitne točke> ")
        ocena_vaj = input("Ocena vaj> ")
        ocena_teo = input("Ocena teorije> ")
        if ocena_vaj.isdigit():
            ocena_vaj = int(ocena_vaj)
        else:
            ocena_vaj = ''
        if ocena_teo.isdigit():
            ocena_teo = int(ocena_teo)
        else:
            ocena_teo = ''    
        nov_predmet = Predmet(ime_predmeta, predavatelj, asistent, kreditne_tocke,  ocena_vaj, ocena_teo)
        semester.dodaj_predmet(nov_predmet)

def pobrisi_predmet():
    if not moje_stanje.semestri:
        return print("Nimate nobenega semestra zato dodajte enega.")
    else:
        semester = izberi_semester(moje_stanje)
        if not semester.predmeti:
            return print("V tem semestru nimate nobenega predmeta zato dodajte enega.")
        else:
            predmet = izberi_predmet(semester)
            semester.pobrisi_predmet(predmet)

def opravljen_predmet():
    if not moje_stanje.semestri:
        return print("Nimate nobenega semestra zato dodajte enega.")
    else:
        semester = izberi_semester(moje_stanje)
        if not semester.predmeti:
            return print("V tem semestru nimate nobenega predmeta zato dodajte enega.")
        else:
            predmet = izberi_predmet(semester)
            predmet.opravil_predmet()

# TEKSTOVNI UMESNIK
def tekstovni_vmesnik():
    prikazi_pozdravno_sporocilo()
    while True:
        trenutno_stanje()
        ukaz = izberi_moznost(
            [
                (DODAJ_SEMESTER, "dodaj nov semester"),
                (POBRISI_SEMESTER, "pobriši semester"),
                (DODAJ_PREDMET, "dodaj nov predmet"),
                (POBRISI_PREDMET, "pobrisi predmet"),
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
        elif ukaz == IZHOD:
            moje_stanje.shrani_v_datoteko(IME_DATOTEKE)
            print("Nasvidenje")
            break

tekstovni_vmesnik()