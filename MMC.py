n = int(input("digite um número diferente de zero: "))
while n == 0:
    n = int(input("digite um número diferente de zero: "))

m = int(input("digite outro número diferente de zero: "))
while m == 0:
    m = int(input("digite outro número diferente de zero: "))

for i in range(2, n+1):
    if n % i == 0:
        print(n / i)
        
for i in range(2, m+1):
    if m % i == 0:
        print(m / i)


    
