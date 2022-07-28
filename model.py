from datetime import date
import json

def isfloat(x):
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True

class Stanje:
    def __init__(self, semestri):
        self.semestri = semestri

    def dodaj_semester(self, semester):
        if semester in self.semestri:
            raise ValueError("Semester s takšnim imenom že obstaja.")
        else:
            self.semestri.append(semester)

    def pobrisi_semester(self, semester):
        self.semestri.remove(semester)

    def v_slovar(self):
        return {
            "Semestri": [semester.v_slovar() for semester in self.semestri]
        }
    
    @staticmethod
    def iz_slovarja(slovar):
        return Stanje(
            [             
                Semester.iz_slovarja(slovar_semestra) 
                for slovar_semestra in slovar["Semestri"]
            ]
        )

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
                napake["ime"] = "Ime je že zasedeno."
        return napake


class Semester:
    def __init__(self, ime_semestra, predmeti):
        self.ime_semestra = ime_semestra
        self.predmeti = predmeti

    def dodaj_predmet(self, predmet):
        if predmet in self.predmeti:
            raise ValueError("Predmet s takšnim imenom že obstaja.")
        else:
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
        return Semester(
            slovar["Semester"],
            [
                Predmet.iz_slovarja(slovar_predmetov) 
                for slovar_predmetov in slovar["Predmeti"]
            ]
        )

    def preveri_podatke_novega_predmeta(self, ime):
        napake = {}
        if not ime:
            napake["ime"] = "Ime predmeta mora biti neprazno."
        for semester in self.predmeti:
            if semester.ime_predmeta == ime:
                napake["ime"] = "Ime je že zasedeno."
        return napake

class Predmet:
    def __init__(self, ime_predmeta, opis, kreditne_tocke, izpitni_roki, ocene, opravljen=False):
        self.ime_predmeta = ime_predmeta
        self.opis = opis
        self.kreditne_tocke = kreditne_tocke
        self.izpitni_roki = izpitni_roki
        self.ocene = ocene
        self.opravljen = opravljen   
    
    def dodaj_izpitni_rok(self, izpitni_rok):   # dodaj pogoj, da je vneseni datum res datum
        if izpitni_rok in self.izpitni_roki:
            raise ValueError("Izpitni rok s takšnim imenom že obstaja.")
        else:
            self.izpitni_roki.append(izpitni_rok)

    def pobrisi_izpitni_rok(self, izpitni_rok):
        self.izpitni_roki.remove(izpitni_rok)

    def dodaj_oceno(self, ocena):
        if not isfloat(ocena) or ocena > 10 or ocena < 1:
            ValueError("Ocena mora biti število med 1 in 10")
        elif ocena in self.ocene:
            raise ValueError("Ocena s takšnim imenom že obstaja.")
        else:
            self.ocene.append(ocena)

    def pobrisi_oceno(self, ocena):
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
        return Predmet(
            slovar["Predmet"], 
            slovar["Informacije o predmetu"], 
            slovar["Kreditne točke"],        
            [
                Izpitni_rok.iz_slovarja(slovar_izp) 
                for slovar_izp in slovar["Izpitni roki"]
            ],
            [
                Ocena.iz_slovarja(slovar_ocen) 
                for slovar_ocen in slovar["Ocene"]
            ],
            slovar["Predmet opravljen"]
        )

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
            "Ime": self.ime,
            "Datum": self.datum
        }
    
    @staticmethod
    def iz_slovarja(slovar):
        return Izpitni_rok(
            slovar["Ime"],
            slovar["Datum"]
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