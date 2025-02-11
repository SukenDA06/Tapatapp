'''
Explicació pas a pas:
Menú: El programa mostra un menú d'opcions perquè l'usuari pugui triar què vol fer.
Afegir producte: Afegeix un nou producte a la llista inventari amb la quantitat introduïda per l'usuari.
Eliminar producte: L'usuari pot introduir el nom del producte que vol eliminar, i si es troba, s'elimina de la llista.
Actualitzar quantitat: Permet canviar la quantitat d'un producte existent. Si el producte no existeix, mostra un missatge d'error.
Consultar inventari: Mostra tots els productes amb la seva quantitat actual.
Sortir: Finalitza el programa quan l'usuari selecciona l'opció 5.
Aquest és un enfocament més senzill, sense utilitzar funcions, només amb estructures bàsiques com les llistes, bucles i condicionals.

'''



# Llista inicial d'inventari amb alguns productes (nom, quantitat)
inventari = [["Poma", 50], ["Plàtan", 30], ["Taronja", 20]]


while True:
    print("\n--- Menú d'Inventari ---")
    print("1. Afegir producte")
    print("2. Eliminar producte")
    print("3. Actualitzar quantitat")
    print("4. Consultar inventari")
    print("5. Sortir")

    opcio = input("Esculli una opció: ")

    if opcio == "1":
        print("Afegir producte")
        p=input("Introdueix producte: ")
        q=int(input("Introdueix quantitat: "))
        inventari.append([p,q])
    elif opcio == "2":
        print("Eliminar producte")
        nom=input("Introdueix el Producte a eliminar: ")
        for producte in inventari:
            if producte[0] == nom:
                inventari.remove(producte)
                print("Producte eliminat")
                break
    elif opcio == "3":
        print("Actualitzar quantitat")
    elif opcio == "4":
        print("Consultar inventari")
        for x in range(len(inventari)):
            print(inventari[x][0], " quantitat ", inventari[x][1])
    elif opcio == "5":
        print("Sortim, Adeu!!")
        break
