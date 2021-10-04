from scripts.scripts import predict

if __name__ == '__main__':
    try:
        days_input = int(input("Entre com o número de dias que deseja prever...\n"))
    except ValueError:
        print("Entrada inválida!\nEntre com um número inteiro!\n")
    predict(days_input)
