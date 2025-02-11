'''
Aquest programa simula el monitoratge d'una granja mitjançant sensors intel·ligents que recullen dades sobre la humitat i la temperatura.
Si aquests valors estan fora del rang òptim, el sistema emet una alerta
'''

humitat = 30  # Exemple de humitat
temperatura = 35  # Exemple de temperatura
humitatMaxima = 45  
temperaturaMaxima = 50

if humitat > humitatMaxima or temperatura > temperaturaMaxima:
    print("Alerta de dades fora del rang optim!")
else:
    print("Valors de dades optims!")