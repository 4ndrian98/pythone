variabile1= 5.0
somma=0.0
while True:
    variabile2=float(input("Scrivi un numero. Per fermare il ciclo per due volte scrivi 0: "))
    somma+=variabile2
    if variabile1 == 0 and variabile1 == variabile2:
        break
    else: variabile1=variabile2
print("Ecco la tua somma:", somma)
