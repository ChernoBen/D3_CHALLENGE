from scripts.scripts import predict

if __name__ == '__main__':
    while True:
        try:
            days_input = int(input("Entre com o número de dias que deseja prever...\nEntre com '0' para sair\n"))
            if days_input == 0:
                break
            predict(days_input)
        except ValueError:
            print("Entrada inválida!\nEntre com um número inteiro!\n")
            break
