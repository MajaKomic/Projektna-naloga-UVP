from datetime import date
from model import Stanje, Semester, Predmet, Izpitni_rok, Ocena

IME_DATOTEKE = "stanje.json"   
try:
    moje_stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    moje_stanje = Stanje(semestri=[])

DODAJ_SEMESTER = 1
POBRISI_SEMESTER = 2
DODAJ_PREDMET = 3
POBRISI_PREDMET = 4
DODAJ_IZPITNI_ROK = 5
POBRISI_IZPITNI_ROK = 6
DODAJ_OCENO = 7
POBRISI_OCENO = 8
IZHOD = 9

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

def prikaz_izpitnega_roka(izpitni_rok):
    return f"{izpitni_rok.ime}: {izpitni_rok.datum}"

def prikaz_ocene(ocena):
    return f"{ocena.ime}: {ocena.ocena}"

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

def izberi_izpitni_rok(predmet):
    print("Izberi izpitni rok.")
    return izberi_moznost(
        [
            (izpitni_rok, prikaz_izpitnega_roka(izpitni_rok)) 
            for izpitni_rok in predmet.izpitni_roki
        ]
    ) 

def izberi_oceno(predmet):
    print("Izberi oceno.")
    return izberi_moznost(
        [
            (ocena, prikaz_ocene(ocena)) 
            for ocena in predmet.ocene
        ]
    )

def trenutno_stanje():
    print("Vaše trenutno stanje:")
    for semester in moje_stanje.semestri:
        print(f"{prikaz_semestra(semester)}")
        for predmet in semester.predmeti:
            print(f"    {prikaz_predmeta(predmet)}")
            for izpitni_rok in predmet.izpitni_roki:
                print(f"        {prikaz_izpitnega_roka(izpitni_rok)}")
            #for ocena in predmet.ocena:
            #    print(f"    {prikaz_ocene(ocena)}")
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
        ime = input("Ime> ")
        opis = input("Opis> ")
        kreditne_tocke = input("Krednitne točke> ")
        nov_predmet = Predmet(ime, opis, kreditne_tocke, [], [])
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

def dodaj_izpitni_rok():
    if not moje_stanje.semestri:
        return print("Nimate nobenega semestra zato dodajte enega.")
    else:
        semester = izberi_semester(moje_stanje)
        if not semester.predmeti:
            return print("V tem semestru nimate nobenega predmeta zato dodajte enega.")
        else:
            predmet = izberi_predmet(semester)
            print("Vnesite podatke o izpitnem roku.")
            ime = input("Ime> ")
            datum = input("Datum (YYYY-MM-DD)> ")
            if datum.strip():
                datum = date.fromisoformat(datum)
            else: 
                datum = None
            izp_rok = Izpitni_rok(ime, datum)
            predmet.dodaj_izpitni_rok(izp_rok)
 
def pobrisi_izpitni_rok():
    if not moje_stanje.semestri:
        return print("Nimate nobenega semestra zato dodajte enega.")
    else:
        semester = izberi_semester(moje_stanje)
        if not semester.predmeti:
            return print("V tem semestru nimate nobenega predmeta zato dodajte enega.")
        else:
            predmet = izberi_predmet(semester)
            if not predmet.izpitni_roki:
                return print("Pri tem predmetu nimate nobenega izpitnega roka, zato dodajte enega.")
            else:
                izpitni_rok = izberi_izpitni_rok(predmet)
                predmet.pobrisi_izpitni_rok(izpitni_rok)

def dodaj_oceno():
    if not moje_stanje.semestri:
        return print("Nimate nobenega semestra zato dodajte enega.")
    else:
        semester = izberi_semester(moje_stanje)
        if not semester.predmeti:
            return print("V tem semestru nimate nobenega predmeta zato dodajte enega.")
        else:
            predmet = izberi_predmet(semester)
            print("Vnesite podatke o oceni.")
            ime = input("Ime> ")
            ocena = input("Ocena> ")
            predmet.dodaj_oceno(Ocena(ime, ocena))

def pobrisi_oceno():
    if not moje_stanje.semestri:
        return print("Nimate nobenega semestra zato dodajte enega.")
    else:
        semester = izberi_semester(moje_stanje)
        if not semester.predmeti:
            return print("V tem semestru nimate nobenega predmeta zato dodajte enega.")
        else:
            predmet = izberi_predmet(semester)
            if not predmet.ocene:
                return print("Pri tem predmetu nimate nobene ocene, zato dodajte eno.")
            else:
                ocena = izberi_oceno(predmet)
                predmet.pobrisi_oceno(ocena)

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
                (DODAJ_IZPITNI_ROK, "dodaj nov izpitni rok"),
                (POBRISI_IZPITNI_ROK, "pobrisi izpitni rok"),
                (DODAJ_OCENO, "dodaj novo oceno"),
                (POBRISI_OCENO, "pobrisi oceno"),
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
        elif ukaz == DODAJ_IZPITNI_ROK:
            dodaj_izpitni_rok()
        elif ukaz == POBRISI_IZPITNI_ROK:
            pobrisi_izpitni_rok()
        elif ukaz == DODAJ_OCENO:
            dodaj_oceno()
        elif ukaz == POBRISI_OCENO:
            pobrisi_oceno()
        elif ukaz == IZHOD:
            moje_stanje.shrani_v_datoteko(IME_DATOTEKE)
            print("Nasvidenje")
            break

tekstovni_vmesnik()