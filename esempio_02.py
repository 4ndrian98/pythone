n=int(input("inscerisci un numero: "))
l=input("inserisci una lettera: ")

for i in range(1,n): 
    print(" "*(n-i) + l*(1+(i-1)*2))