import bottle
from model import Stanje

IME_DATOTEKE = "stanje.json"
try:
    moje_stanje = Stanje.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    moje_stanje = Stanje()
#except ValueError:
#    moje_stanje = Stanje(semestri=[])

@bottle.get("/")
def osnovna_stran():
    return bottle.template('osnovna_stran.tpl')

@bottle.error(404)
def error_404(error):
    return "Ta stran ne obstaja!"

bottle.run(reload=True, debug=True)