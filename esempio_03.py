Punteggio_A=0
Punteggio_B=0
ciclo=True
vincitore=0
scambio_passato=0
while ciclo:
    vincitore=int(input("Chi ha vinto lo scambio? 1(per giocatore 1) o 2 (per giocatore 2): "))
    if vincitore == 1 and Punteggio_A <40:
        Punteggio_A+=15
    else:
        Punteggio_B+=15
    print("Ecco il punteggio: Giocatore1",Punteggio_A,"-",Punteggio_B,"Giocatore2")
    if Punteggio_A >=40 or Punteggio_B>=40:
        if vincitore == 1 and vincitore == scambio_passato:
            ciclo=False
        elif vincitore == 2 and vincitore == scambio_passato:
            ciclo=False
    
    vincitore= scambio_passato


print("Ha vinto il giocatore", vincitore)
                  
                