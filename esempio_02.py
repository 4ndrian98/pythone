n=int(input("inscerisci un numero: "))
l=input("inserisci una lettera: ")

for i in range(0,n): 
    print(" "*(n-i) + l*(1+i*2))
