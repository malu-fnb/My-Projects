def metroPKm (metros):
    return metros / 1000

def metrosPHc (metros):
    return metros / 100

def metrosPDC (metros):
    return metros / 10

def metrosPDeci (metros):
    return metros * 10

def metrosPCm (metros):
    return metros * 100

def metrosPMm (metros):
    return metros * 1000


def menu():
    print("1. Metros para Quilômetros")
    print("2. Metros para Hectômetros")
    print("3. Metros para Decâmetros")
    print("4. Metros para Decímetros")
    print("5. Metros para Centímetros")
    print("6. Metros para Milímetros")

def main ():
    menu()
    opcao = input("Digite o número da opção desejada:")

    vEmMetro = float(input("Digite o valor em metros: "))

    if opcao == '1':
        result = metroPKm
        print (vEmMetro, " metros equivalem a", result, "quilômetros")

    elif opcao == '2':
        result = metrosPHc
        print (vEmMetro, "em metros equivale a", result, "hectômetros")
    
    elif opcao == '3':
        result = metrosPDC
        print (vEmMetro, "em metros equivale a", result, "decâmetros.")

    elif opcao == '4':
        result = metrosPDeci
        print (vEmMetro, "em metros equivale a ", result, "decímetros.")
    
    elif opcao == '5':
        result = metrosPCm
        print (vEmMetro, "em metros equivale a ", result, "centímetros.")
    
    elif opcao == '6':
        result = metrosPMm
        print (vEmMetro, "em metros equivale a ", result, "milímetros.")
    
    else:
        print("Opção inválida. Por favor, digite um número de 1 a 6.")

if __name__ == "__main__":
    main()