from datetime import date
import json

def isfloat(x):
    try:
        x = float(x)
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
    
    def povprecna_ocena(self, katera):
        stevilo = 0
        vsota = 0
        for predmet in self.predmeti:
            if katera == "povp_vaj":
                if predmet.ocena_vaj != '':
                    stevilo += 1
                    vsota += int(predmet.ocena_vaj)
            elif katera == "povp_teo":
                if predmet.ocena_teo != '':
                    stevilo += 1
                    vsota += int(predmet.ocena_teo)
            else:
                if predmet.ocena_vaj != '':
                    stevilo += 1
                    vsota += int(predmet.ocena_vaj)
                elif predmet.ocena_teo != '':
                    stevilo += 1
                    vsota += int(predmet.ocena_teo)
        if stevilo == 0:
            return 0
        return vsota / stevilo

    def stevilo_kreditnih_tock(self):
        stevilo = 0
        for predmet in self.predmeti:
            kreditne = int(predmet.kreditne_tocke)
            if kreditne == None:
                kreditne = 0
            else:
                stevilo += kreditne
        if stevilo == 0:
            return 0
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
    def __init__(self, ime_predmeta, predavatelj, asistent, kreditne_tocke,  ocena_vaj, ocena_teo, opravljen=False):
        self.ime_predmeta = ime_predmeta
        self.predavatelj = predavatelj
        self.asistent = asistent
        self.kreditne_tocke = kreditne_tocke
        self.ocena_vaj = ocena_vaj
        self.ocena_teo = ocena_teo
        self.opravljen = opravljen   

    def opravil_predmet(self):
        self.opravljen = True

    def v_slovar(self):
        return {
            "Predmet": self.ime_predmeta,
            "Predavatelj": self.predavatelj,
            "Asistent": self.asistent,
            "Kreditne točke": self.kreditne_tocke,
            "Ocena iz vaj": self.ocena_vaj,
            "Ocena iz teorije": self.ocena_teo,
            "Predmet opravljen": self.opravljen
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Predmet(
            slovar["Predmet"], 
            slovar["Predavatelj"], 
            slovar["Asistent"],
            slovar["Kreditne točke"],        
            slovar["Ocena iz vaj"],
            slovar["Ocena iz teorije"],
            slovar["Predmet opravljen"]
        )