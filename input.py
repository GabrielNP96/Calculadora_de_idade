def receives_data():
    i = False
    while i == False:


        try:
            year = int(input("Digite seu ano de nascimento: "))
            month = int(input("Digite o mês que você nasceu: "))
            day = int(input("Digite sua o dia em que você nasceu: "))
            
            i = True
            return [year, month, day]
        
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite APENAS números inteiros, Digite novamente.")
