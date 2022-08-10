import bottle
from model import Stanje, Semester, Predmet

IME_DATOTEKE = "stanje.json"
try:
    moje_stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    moje_stanje = Stanje(semestri=[])
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
        id_semestra = moje_stanje.dodaj_semester(semester)
        #shrani_stanje_trenutnega_uporabnika(stanje)
        bottle.redirect(url_semestra(id_semestra))


@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"

bottle.run(reload=True, debug=True)