punteggio_giocatore1=0
punteggio_giocatore2=0
GIOCATE= ["C", "S", "F"]
partite=0

while True:
    print("Gioca a morra cinese, inserisci due lettere: C(per carta), S(per Sasso), F(per forbici):")
    Lettera_giocatore1= input("Prima lettera: ").upper()
    if Lettera_giocatore1 not in GIOCATE:
        print('Errore!, devi inserire: "C"(carta), "S"(sasso) o "F"(forbice)')
        continue
    Lettera_giocatore2= input("Seconda lettera: ").upper()
    if Lettera_giocatore2 not in GIOCATE:
        print('Errore!, devi inserire: "C"(carta), "S"(sasso) o "F"(forbice)')
        continue

    #Giocate C:
    if Lettera_giocatore1 == "C" and Lettera_giocatore2 == "C":
        print("Pareggio!")
        partite+=1
    elif Lettera_giocatore1 == "C" and Lettera_giocatore2 == "S":
        partite+=1
        punteggio_giocatore1+=1
        print("Ha vinto il Giocatore 1!", punteggio_giocatore1, "-", punteggio_giocatore2)

    elif Lettera_giocatore1 == "C" and Lettera_giocatore2 == "F":
        partite+=1
        punteggio_giocatore2+=1
        print("Ha vinto il Giocatore 2!", punteggio_giocatore1, "-", punteggio_giocatore2)
        
        
    #Giocate S:    
    if Lettera_giocatore1 == "S" and Lettera_giocatore2 == "S":
        print("Pareggio!")
        partite+=1
    elif Lettera_giocatore1 == "S" and Lettera_giocatore2 == "F":
        partite+=1
        punteggio_giocatore1+=1
        print("Ha vinto il Giocatore 1!", punteggio_giocatore1, "-", punteggio_giocatore2)
    elif Lettera_giocatore1 == "S" and Lettera_giocatore2 == "C":
        partite+=1
        punteggio_giocatore2+=1
        print("Ha vinto il Giocatore 2!", punteggio_giocatore1, "-", punteggio_giocatore2)
    
    #Giocate F:
    if Lettera_giocatore1 == "F" and Lettera_giocatore2 == "F":
        print("Pareggio!")
        partite+=1
    elif Lettera_giocatore1 == "F" and Lettera_giocatore2 == "S":  
        partite+=1
        punteggio_giocatore2+=1
        print("Ha vinto il Giocatore 2!", punteggio_giocatore1, "-", punteggio_giocatore2)
    elif Lettera_giocatore1 == "F" and Lettera_giocatore2 == "C":
        partite+=1
        punteggio_giocatore1+=1
        print("Ha vinto il Giocatore 1!", punteggio_giocatore1, "-", punteggio_giocatore2)
    if punteggio_giocatore1 > punteggio_giocatore2+2:
        print(f"Hai giocato: {partite} partite, ha vinto il Giocatore 2 {punteggio_giocatore1} - {punteggio_giocatore2}")
        break
    elif punteggio_giocatore2 > punteggio_giocatore1+2:
        print(f"Hai giocato: {partite} partite, ha vinto il Giocatore 1 {punteggio_giocatore1} - {punteggio_giocatore2}")
        break
