opcao = int(input("Selecione de 1 a 4: "))
match opcao:
    case 1: 
        print("Você selecionou 1")
    case 2: 
        print("Você selecionou 2")
    case 3 | 4:
        print("Você selecionou 3 ou 4")  
    case _:
        print("Opção Invalida")