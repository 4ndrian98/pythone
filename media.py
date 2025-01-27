somma=0
contatore=0
while True:
    numero=float(input("Inscerisci un numero per fare la media (-1 per uscire dal programma): "))
    if numero==-1:
        break
    else:
        somma += numero
        contatore +=1

if contatore > 0:
    media= somma/contatore
    print("La tua media è:", media)
else:
    print("Nessun numero inserito.")