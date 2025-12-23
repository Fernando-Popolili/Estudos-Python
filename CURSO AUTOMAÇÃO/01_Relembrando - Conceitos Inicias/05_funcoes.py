#CODIGO 1

def saudacao():
    print("Olá!")

saudacao()


#CODIGO 2
def nome(nome):
    print(f"Olá, {nome}!")

nome_user = input("Qual seu nome? ")
nome(nome_user)

#CODIGO 3
def somar(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

num1 = int(input("Fale um numero: "))
num2 = int(input("Fale um numero: "))

resultado_soma = somar(num1, num2)
print(resultado_soma)
