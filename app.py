meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas =[]

for mes in meses:
    temperaturas.append(float(input(f"Qual a temperatura média do mês de {mes}?")))
    
media_temperaturas = sum(temperaturas)/len(temperaturas)
print(f"A temperatura média é {media_temperaturas}ºC")
