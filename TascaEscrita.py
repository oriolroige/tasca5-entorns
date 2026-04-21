# === EXERCICI 2 ===
def trobar_edat_maxima(persones):
    if not isinstance(persones, list) or not persones:
        return -1
    for persona in persones:
        # Validem estructura i que edat sigui un número per evitar el TypeError
        if not isinstance(persona, dict) or "nom" not in persona or "edat" not in persona or not isinstance(persona["edat"], int):
            return -1
        
    edats = [persona["edat"] for persona in persones]
    return max(edats)

# === EXERCICI 3 ===
productes = [
    {'nom': 'Portàtil Dell XPS 15', 'preu': 1299.99, 'categoria': 'Informàtica', 'stock': 5},
    {'nom': 'Ratolí Logitech MX Master', 'preu': 89.99, 'categoria': 'Perifèrics', 'stock': 15},
    {'nom': 'Monitor Samsung 27"', 'preu': 349.50, 'categoria': 'Monitors', 'stock': 8}
]

def trobar_producte_mes_car():
    global productes
    if not productes:
        return None
    
    # Iniciem amb el primer producte com el més car
    producte_mes_car = productes[0]
    
    for producte in productes:
        if producte["preu"] > producte_mes_car["preu"]:
            producte_mes_car = producte
            
    return producte_mes_car

# === EXERCICI 4 ===
def comptar_empleats_per_departament(empresa):
    resum = {}
    for departament in empresa.get("departaments", []):
        resum[departament["nom"]] = len(departament["empleats"])
    return resum

# ========== PROVES (Només s'executen si corres aquest fitxer directament) ==========
if __name__ == "__main__":
    # Dades de prova exercici 2
    persones_1 = [{'nom': 'Pere', 'edat': 67}, {'nom': 'Sofia', 'edat': 31}]
    persones_4 = [{'nom': 'Anna', 'edat': 25}, {'nom': 'Marc', 'edat': '42'}] # Cas error

    print("=== Prova Exercici 2 (Èxit) ===")
    print(f"Edat màxima: {trobar_edat_maxima(persones_1)}")
    print("=== Prova Exercici 2 (Error tipus) ===")
    print(f"Resultat: {trobar_edat_maxima(persones_4)}")

    print("\n=== Prova Exercici 3 (Producte) ===")
    print(f"Producte més car: {trobar_producte_mes_car()['nom']}")

    # Dades de prova empresa
    empresa_de_prova = {
        'nom': 'TechCorp',
        'departaments': [{'nom': 'Informàtica', 'empleats': [{}, {}, {}]}]
    }
    print("\n=== Prova Exercici 4 (Empresa) ===")
    print(f"Empleats: {comptar_empleats_per_departament(empresa_de_prova)}")