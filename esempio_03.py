Punteggio_A=0
Punteggio_B=0
scambi=0
game=True
vincitore=0
vincitore_scambio_passato=0
x=0
x2=0
while game:
    vincitore=int(input("Chi ha vinto lo scambio? 1(per giocatore 1) o 2 (per giocatore 2): "))
    scambi+=1
    if vincitore == 1 and Punteggio_A <40:
        Punteggio_A+=15
    if Punteggio_A > 40:
        Punteggio_A = 40
        x= scambi

    if vincitore == 2 and Punteggio_B <40:
        Punteggio_B+=15
    if Punteggio_B >40:
        Punteggio_B = 40
        x2= scambi 
    print("Scambio",scambi, "vinto dal Giocatore",vincitore,"Ecco il punteggio: Giocatore1",Punteggio_A,"-",Punteggio_B,"Giocatore2")
    if (scambi > x+1 and Punteggio_A == 40 and vincitore == 1 and vincitore == vincitore_scambio_passato) or ( scambi > x+1 and Punteggio_B == 40 and vincitore == 2 and vincitore == vincitore_scambio_passato):
        game=False
    vincitore_scambio_passato= vincitore
    

print("Ha vinto il giocatore", vincitore)
                  
                
                
                  
                
