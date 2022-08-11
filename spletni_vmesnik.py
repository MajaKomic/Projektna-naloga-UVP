import bottle
from model import Stanje, Semester, Predmet

IME_DATOTEKE = "primer_stanja.json"
#try:
moje_stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
#except FileNotFoundError:
#    moje_stanje = Stanje(semestri=[])
#except ValueError:
#    moje_stanje = Stanje(semestri=[])

def url_semestra(id_semestra):
    return f"/semester/{id_semestra}/"


@bottle.get("/")
def osnovna_stran():
    return bottle.template(
        'osnovna_stran.tpl',
        semestri=moje_stanje.semestri
        )

@bottle.post("/pobrisi-semester/<id_semestra:int>/")
def pobrisi_semester(id_semestra):
    #stanje = stanje_trenutnega_uporabnika()
    semester = moje_stanje.semestri[id_semestra]
    moje_stanje.pobrisi_semester(semester)
    #shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect("/")

@bottle.get("/semester/<id_semestra:int>/")
def prikazi_semester(id_semestra):
    #stanje = stanje_trenutnega_uporabnika()
    semester = moje_stanje.semestri[id_semestra]
    return bottle.template(
        "semester.tpl",
        semestri=moje_stanje.semestri,
        aktualni_semester=semester,
        id_aktualni_semester=id_semestra,
    )

@bottle.get("/dodaj-semester/")
def dodaj_semester_get():
    return bottle.template(
        "dodaj_semester.tpl", napake={}, polja={}
    )

@bottle.post("/dodaj-semester/")
def dodaj_semester_post():
    #stanje = stanje_trenutnega_uporabnika()
    ime = bottle.request.forms.getunicode("ime")
    semester = Semester(ime, predmeti=[])
    napake = moje_stanje.preveri_podatke_novega_semestra(semester)
    if napake:
        polja = {"ime": ime}
        return bottle.template("dodaj_semester.tpl", napake=napake, polja=polja)
    else:
        moje_stanje.dodaj_semester(semester)
        #shrani_stanje_trenutnega_uporabnika(stanje)
        bottle.redirect("/")


@bottle.get("/dodaj-predmet/<id_semestra:int>/")
def dodaj_predmet_get(id_semestra):
    return bottle.template(
        "dodaj_predmet.tpl", 
        id_semestra=id_semestra
    )


@bottle.post("/dodaj-predmet/<id_semestra:int>/")
def dodaj_predmet_post(id_semestra):
    #stanje = stanje_trenutnega_uporabnika()
    semester = moje_stanje.semestri[id_semestra]
    ime_predmeta = bottle.request.forms.getunicode("ime_predmeta")
    predavatelj = bottle.request.forms.getunicode("predavatelj")
    asistent = bottle.request.forms.getunicode("asistent")
    kreditne_tocke = bottle.request.forms.getunicode("kreditne_tocke")
    ocena_vaj = bottle.request.forms.getunicode("ocena_vaj")
    ocena_teo = bottle.request.forms.getunicode("ocena_teo")   
    predmet = Predmet(ime_predmeta, predavatelj, asistent, kreditne_tocke,  ocena_vaj, ocena_teo)
    semester.dodaj_predmet(predmet)
    #shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_semestra(id_semestra))

@bottle.post("/pobrisi-predmet/<id_semestra:int>/<id_predmeta:int>/")
def pobrisi_predmet(id_semestra, id_predmeta):
    #stanje = stanje_trenutnega_uporabnika()
    semester = moje_stanje.semestri[id_semestra]
    predmet = semester.predmeti[id_predmeta]
    semester.pobrisi_predmet(predmet)
    #shrani_stanje_trenutnega_uporabnika(stanje)
    bottle.redirect(url_semestra(id_semestra))

@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"

bottle.run(reload=True, debug=True)