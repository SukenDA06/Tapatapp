'''
El manteniment predictiu és una pràctica important a la indústria digitalitzada.
Aquest programa rep dades sobre l'ús d'una màquina com les hores treballades, la temperatura i les vibracions, i decideix si cal o no manteniment segons uns llindars establerts.
Si alguna de les variables supera els límits, el sistema alerta que es necessita manteniment.

'''

hores = int(input("Introdueix les hores treballades: "))

temperatura = float(input("Introdueix la temperatura (°C): "))

vibracions = float(input("Introdueix les vibracions (unitats): "))

horesMaximes = 14

temperaturaMaxima = 80

vibracionMaxima = 25

def es_float(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
    
def es_int(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False
    
if hores > horesMaximes or temperatura > temperaturaMaxima or vibracions > vibracionMaxima:
    print("Alerta de manteniment!") 
else:
    print("La maquina está en bones condicions!")
