'''
Descripció: Aquest programa simula la implementació d'un projecte de digitalització en una empresa i calcula l'estalvi potencial obtingut. 
L'objectiu és rebre com a input els costos abans i després de la digitalització i retornar l'estalvi total en euros i el percentatge de reducció de costos.
'''

cost_abans = float(input("Entra el cost abans de la digitalització (€): "))

cost_despres = float(input("Entra el cost després de la digitalització (€): "))

def es_float(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False

estalvi = cost_abans - cost_despres
porcentatge = (estalvi / cost_abans) * 100

print("El estalvi total es de ",estalvi,"€")

print("El porcentatge d'estalvi es de",porcentatge,"%")