from datetime import date
import json

class Stanje:
    def __init__(self):
        self.semestri = []
        self.aktualni_semester = None

    def dodaj_semester(self, semester):
        self.semestri.append(semester)
        if not self.aktualni_semester:
            self.aktualni_semester = semester

    def zamenjaj_ak_semester(self, semester):
        self.aktualni_semester = semester

    def pobrisi_semester(self, semester):
        self.semestri.remove(semester)

    def dodaj_predmet(self, predmet):
            self.aktualni_semester.dodaj_predmet(predmet)

    def pobrisi_predmet(self, predmet):
        self.aktualni_semester.pobrisi_predmet(predmet)

    def stevilo_neopravljenih_predmetov(self):
        return sum([semester.stevilo_neopravljenih_predmetov() for semester in self.semestri])

    def v_slovar(self):
        return {
            "Semestri": [semester.v_slovar() for semester in self.semestri],
            "Aktualni semester": self.semestri.index(self.aktualni_semester)
            if self.aktualni_semester else None
        }
    
    @staticmethod
    def iz_slovarja(slovar):
        stanje = Stanje()
        stanje.semestri = [
            Semester.iz_slovarja(slovar_predmeta) for slovar_predmeta in slovar["predmeti"]   # to je mal čudno poglej se enkrat
        ]
        if slovar["Aktualni semester"] is not None:
            stanje.aktualni_semester = stanje.semestri[slovar["Aktualni semester"]]
        return stanje

    def shrani_v_datoteko(self, ime_datoteke):
        with open(ime_datoteke, 'w', encoding='utf-8') as datoteka:
            slovar = self.v_slovar()
            json.dump(slovar, datoteka, indent=4, ensure_ascii=False)
    
    @staticmethod
    def preberi_iz_datoteke(ime_datoteke):
        with open(ime_datoteke, encoding='utf-8') as datoteka:
            slovar = json.load(datoteka)
            return Stanje.iz_slovarja(slovar)

    def preveri_podatke_novega_semestra(self, ime):
        napake = {}
        if not ime:
            napake["ime"] = "Ime semestra mora biti neprazno."
        for semester in self.semestri:
            if semester.ime_semestra == ime:
                napake["ime"] == "Ime je že zasedeno."
        return napake


class Semester:
    def __init__(self, ime_semestra):
        self.ime_semestra = ime_semestra
        self.predmeti = []
    
    def dodaj_predmet(self, predmet):
        self.predmeti.append(predmet)
    
    def pobrisi_predmet(self, predmet):
        self.predmeti.remove(predmet)
    
    def stevilo_neopravljenih_predmetov(self):
        stevilo = 0
        for predmet in self.predmeti:
            if not predmet.opravljen:       
                stevilo += 1
        return stevilo

    def v_slovar(self):
        return {
            "Semester": self.ime_semestra,
            "Predmeti": [predmet.v_slovar() for predmet in self.predmeti]
        }
   
    @staticmethod
    def iz_slovarja(slovar):
        semester = Semester(slovar["Semester"])
        semester.predmet = [
            Predmet.iz_slovarja(slovar_predmetov) for slovar_predmetov in slovar["Predmeti"]
        ]
        return semester


class Predmet:
    def __init__(self, ime_predmeta, opis, kreditne_tocke, opravljen=False):
        self.ime_predmeta = ime_predmeta
        self.opis = opis
        self.kreditne_tocke = kreditne_tocke
        self.izpitni_roki = []
        self.ocene = []
        self.opravljen = opravljen   
    
    def dodaj_izpitni_rok(self, izpitni_rok):
        self.izpitni_roki.append(izpitni_rok)

    def izbrisi_izpitni_rok(self, izpitni_rok):
        self.izpitni_roki.remove(izpitni_rok)
    
    def preteceni_izpitni_roki(self):          # nevem ali bom to funkcijo zares potrebovala
        pretekli = []
        if self.izpitni_roki == []:
            return None
        for izpitni_rok in self.izpitni_roki:
            if self.izpitni_roki.je_pretecen():
                pretekli.append(izpitni_rok)
        return pretekli

    def naslednji_izpitni_rok(self):
        if self.izpitni_roki == []:
            return None
        for izpitni_rok in self.izpitni_roki:
            if not self.izpitni_roki.je_pretecen():
                return izpitni_rok

    def dodaj_oceno(self, ocena):
        self.ocene.append(ocena)

    def izbrisi_oceno(self, ocena):
        self.ocene.remove(ocena)

    def opravil_predmet(self):
        self.opravljen = True

    def v_slovar(self):
        return {
            "Predmet": self.ime_predmeta,
            "Informacije o predmetu": self.opis,
            "Kreditne točke": self.kreditne_tocke,
            "Izpitni roki": [izpitni_rok.v_slovar() for izpitni_rok in self.izpitni_roki],
            "Ocene": [ocena.v_slovar() for ocena in self.ocene],
            "Predmet opravljen": self.opravljen
        }

    @staticmethod
    def iz_slovarja(slovar):
        predmet = Predmet(slovar["Predmet"], slovar["Informacije o predmetu"], slovar["Informacije o predmetu"], slovar["Predmet opravljen"])         
        predmet.izpitni_roki = [
            Izpitni_rok.iz_slovarja(slovar_izp) for slovar_izp in slovar["Izpitni roki"]
        ]
        predmet.ocene = [
            Ocena.iz_slovarja(slovar_ocen) for slovar_ocen in slovar["Ocene"]
        ]

class Izpitni_rok:

    def __init__(self, ime, datum):
        self.ime = ime
        self.datum = datum
    
    def je_pretecen(self):
        if self.datum < date.today:
            return True
        else:
            return False

    def v_slovar(self):
        return {
            "ime": self.ime,
            "datum": date.isoformat(self.datum)
        }
    
    @staticmethod
    def iz_slovarja(slovar):
        return Izpitni_rok(
            slovar["ime"],
            date.fromisoformat(slovar["datum"])
        )

class Ocena:

    def __init__(self, ime, ocena):
        self.ime = ime
        self.ocena = ocena
    
    def v_slovar(self):
        return {
            "ime": self.ime,
            "ocena": self.ocena
        }
    
    @staticmethod
    def iz_slovarja(slovar):
        return Ocena(
            slovar["ime"],
            slovar["ocena"]
        )