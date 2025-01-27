somma=0
contatore=0
while True:
    numero=float(input("Inscerisci un numero per fare la media (per uscire dal programma digita un numero negativo): "))
    if numero<0:
        break
    else:
        somma += numero
        contatore +=1

if contatore > 0:
    media= somma/contatore
    print("La tua media è %.2f" % media)
else:
    print("Nessun numero inserito.")
