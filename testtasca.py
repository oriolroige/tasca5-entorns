import pytest
from TascaEscrita import trobar_edat_maxima, trobar_producte_mes_car, comptar_empleats_per_departament, productes

# test ex 2
def test_trobar_edat_maxima_exit():
    persones = [{'nom': 'Pere', 'edat': 67}, {'nom': 'Sofia', 'edat': 31}, {'nom': 'Joan', 'edat': 80}]
    assert trobar_edat_maxima(persones) == 80

def test_trobar_edat_maxima_buida():
    assert trobar_edat_maxima([]) == -1

def test_trobar_edat_maxima_error_tipus():
    # Cas on l'edat és un string en comptes d'un int
    persones = [{'nom': 'Anna', 'edat': 25}, {'nom': 'Marc', 'edat': '42'}]
    assert trobar_edat_maxima(persones) == -1

def test_trobar_edat_maxima_no_llista():
    assert trobar_edat_maxima("No soc una llista") == -1


# tests ex 3
def test_trobar_producte_mes_car():
    # El producte més car segons la llista global és el Portàtil (1299.99)
    resultat = trobar_producte_mes_car()
    assert resultat['nom'] == 'Portàtil Dell XPS 15'
    assert resultat['preu'] == 1299.99

def test_trobar_producte_mes_car_llista_buida(monkeypatch):
    # Forcem que la llista global estigui buida per provar el cas d'error
    import TascaEscrita
    monkeypatch.setattr(TascaEscrita, "productes", [])
    assert trobar_producte_mes_car() is None


#tests ex 4
def test_comptar_empleats_per_departament():
    empresa = {
        'nom': 'TechCorp',
        'departaments': [
            {'nom': 'Informàtica', 'empleats': [{}, {}, {}]}, # 3 empleats
            {'nom': 'Màrqueting', 'empleats': [{}]}           # 1 empleat
        ]
    }
    resultat = comptar_empleats_per_departament(empresa)
    assert resultat['Informàtica'] == 3
    assert resultat['Màrqueting'] == 1

def test_comptar_empleats_sense_departaments():
    empresa = {'nom': 'EmptySoft'}
    # Ha de retornar diccionari buit ja que .get("departaments", []) retorna llista buida
    assert comptar_empleats_per_departament(empresa) == {}