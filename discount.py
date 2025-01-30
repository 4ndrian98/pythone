
prices= []
isPet=[]
animal_list=[]
nItems=0
ciclo= True
sconto = 0.8
while ciclo:
    prezzo=float(input("Inserisci il prezzo dell'articolo: (-1 per chiudere il programma)"))
    if prezzo == "-1":
        ciclo=False
        break

    elif prezzo > 0:
        prices.append(prezzo)
    animale=input("Inserisci True se è un'animale o False per tutti gli altri articoli: ").lower().strip()
    if animale == 'true':
        isPet.append(True)
    elif animale == 'false':
        isPet.append(False)
    else:
        print("Inserisci solo True o False.")           
    nItems+=1


sum_without_discount= sum(prices)
sum_price_animals=[]
for i in range(0,len(prices)):
    if isPet[i] == True:
        sum_without_discount -= prices[i]
        sum_price_animals.append(prices[i])
if (len(prices)-len(sum_price_animals)) >=5:
    final_price= (sum_without_discount*sconto) + sum_price_animals
else:
    final_price=sum(prices)

print("la tua somma finale è:", final_price, "€")

