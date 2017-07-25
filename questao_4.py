n = int(input("digite um número: "))
lista1 = list(range(1,n+1))
print(lista1)
#lista2 vai receber os numeros 
lista2 = []
a = 1
for i in lista1:
    if i % a == 0:
        a = a + 1
        lista2.append(i)

print(lista2)
        
