n = int(input("digite o número de alunos: "))
a = 0
y = n
lista = []
while y != 0:
    b = int(input("nota: "))
    lista.append(b)
    a = a + b
    y = y - 1
print(a)

media = a / n
print("média: %d" % media)
print("notas maiores que a média:")
for i in lista:
    if i > media:
        print(i)


    
