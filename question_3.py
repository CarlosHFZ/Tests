import json

# Nome do arquivo JSON (ajuste o caminho conforme necessário)
file_name = "revenue.json"

# Lê o conteúdo do arquivo JSON
try:
    with open(file_name, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"Arquivo '{file_name}' não encontrado. Verifique o caminho e tente novamente.")
    exit()

# Extraindo os valores de faturamento diário
daily_revenue = [day["revenue"] for day in data["days"] if day.get("revenue")]

# Calculando o menor e o maior valor de faturamento
min_value = min(daily_revenue)
max_value = max(daily_revenue)

# Calculando a média mensal
monthly_average = sum(daily_revenue) / len(daily_revenue)

# Contando quantos dias tiveram faturamento acima da média
days_above_average = sum(1 for valor in daily_revenue if valor > monthly_average)

# Imprimindo os resultados
print(f"Menor valor de faturamento: R${min_value:.2f}")
print(f"Maior valor de faturamento: R${max_value:.2f}")
print(f"Dias com faturamento acima da média: {days_above_average}")
