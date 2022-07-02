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

    def pobrisi_semester(self, semester):
        self.semestri.remuve(semester)

    def pobrisi_predmet(self, predmet):
        self.aktualni_semester.izbrisi_predmet(predmet)

    def dodaj_predmet(self, predmet):
        self.aktualni_semester.dodaj_predmet(predmet)
    
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
            Semester.iz_slovarja(slovar_predmeta) for slovar_predmeta in slovar['predmeti']   # to je mal čudno poglej se enkrat
        ]
        if slovar["Aktualni semester":] is not None:
            stanje.aktualni_semester = stanje.semestri[slovar["Aktualni semester":]]
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
            napake['ime'] = 'Ime semestra mora biti neprazno.'
        for semester in self.semestri:
            if semester.ime == ime:
                napake['ime'] == 'Ime je že zasedeno.'
        return napake


class Semester:
    def __init__(self, ime_semestra):
        self.ime_semestra = ime_semestra
        self.predmeti = []
    
    def dodaj_predmet(self, predmet):
        self.predmeti.append(predmet)
    
    def stevilo_neopravljenih_predmetov(self):
        stevilo = 0
        for predmet in self.predmeti:
            if not predmet.opravljen:       #nikjer nisem definirala funkcije opravljeno
                stevilo += 1
            return stevilo

    def v_slovar(self):
        return {
            "Semester": self.ime_semestra,
            "Predmeti": [predmet.v_slovar() for predmet in self.predmeti]
        }
   
    @staticmethod
    def iz_slovarja(slovar):
        semester = Semester(slovar['ime'])
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
            if izpitni_rok < date.today():
                pretekli.append(izpitni_rok)
        return pretekli

    def naslednji_izpitni_rok(self):
        pretekli = preteceni_izpitni_roki()
        if self.izpitni_roki[0] in pretekli:
            self.izpitni_roki.remuve(self.izpitni_roki[0])
        else:
            return self.izpitni_roki[0]

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
            #napiše najbližji/nasledji izpitni rok
            "ocena": self.ocene,
            "Predmet opravljen": self.opravljen
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Predmet(slovar["Predmet"], slovar["Informacije o predmetu"], slovar["Kreditne točke"], slovar["ocena"], slovar["Predmet opravljen"])    


class Izpitni_roki:
    def __init__(self, kolokvij1, kolokvij2, izpitni_rok1, izpitni_rok2, izpitni_rok3):
        self.kolokvij1 = kolokvij1
        self.kolokvij2 = kolokvij2
        self.izpitni_rok1 = izpitni_rok1
        self.izpitni_rok2 = izpitni_rok2
        self.izpitni_rok3 = izpitni_rok3

    def v_slovar(self):
        return {
            "1. kolokvij": self.kolokvij1,
            "2. kolokvij": self.kolokvij2,
            "1. izpitni rok": self.izpitni_rok1,
            "2. izpitni rok": self.izpitni_rok2,
            "3. izpitni rok": self.izpitni_rok3
        }