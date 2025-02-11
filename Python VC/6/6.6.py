'''
El programa gestiona l'inventari d'una empresa, mantenint un registre d'entrades i sortides de productes.
També genera alertes quan les existències d'un producte cauen per sota d'un mínim establert, indicant que és necessari reposar-lo.
'''

inventari = {"producte_A": 50, "producte_B": 10, "producte_C": 5}

minim = 10

for producte, quantitat in inventari.items():
    if quantitat < minim:
        print(f"¡Alerta! El producto {producte} está por debajo del mínimo. Solo quedan {quantitat} unidades.")