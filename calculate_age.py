import datetime

def calculate_age(birth_date_list):
    current_data = datetime.datetime.now()
    current_year = current_data.year
    current_month = current_data.month
    current_day = current_data.day

    # Calcula a idade base apenas pelo ano
    calculated_age = current_year - birth_date_list[0] # birth_date_list[0] é o ano de nascimento

    # Verifica se o aniversário já passou neste ano
    if current_month < birth_date_list[1]: # birth_date_list[1] é o mês de nascimento
        calculated_age -= 1
    elif current_month == birth_date_list[1]: # Se o mês atual for igual ao mês de nascimento
        if current_day < birth_date_list[2]: # birth_date_list[2] é o dia de nascimento
            calculated_age -= 1 # Aniversário ainda não chegou neste mês

   

    return calculated_age
