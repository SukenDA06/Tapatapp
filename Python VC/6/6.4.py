'''
El programa calcula el temps total necessari per produir i transportar un producte.
Rep com a inputs el temps de producció i el de transport, i retorna el temps total.
Això ajuda a mesurar l'eficiència de la cadena de subministrament.
'''

TempsDeProducció = float(input("Introdueix el temps de producció (hores): "))

TempsDeTransport = float(input("Introdueix el temps de transport (hores): "))

TempsTotal = TempsDeProducció + TempsDeTransport

def es_float(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

print("El producte tardará ",TempsTotal," Hores en produirse i transportarse.")