
num=[]
cnt=-1
while True:
    n=float(input("Scrivi un numero. Per fermare il ciclo per due volte scrivi 0: "))
    num.append(n)
    cnt+=1
    if len(num)>1:
        if num[cnt-1] == 0:
            if num[cnt] == 0:
                break
print("Ecco la tua somma:", sum(num))