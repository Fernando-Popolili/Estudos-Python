contador = 1

while contador <= 5:
    print(f'contador é: {contador}')
    contador += 1

print("Fim")

for numero in range(1,6):
    print(numero)


frutas = ["Maça", "Banana", "Uva"]

for fruta in frutas:
    print(fruta)



for fruta in frutas:
    print(f"Verificando: {fruta}")   
    if fruta == "Banana":
        print(f"Fruta encontrada: {fruta}") 
        break


for numero in range(1,11):
    if numero % 2 == 0:
        continue
    print(numero)