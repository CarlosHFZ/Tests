# Valores de faturamento mensal por estado
revenue_by_state = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

# Calcula o valor total mensal
total_monthly_revenue = sum(revenue_by_state.values())

# Calcula os percentuais de representação
percentages_by_state = {}
for state, value in revenue_by_state.items():
    percentage = (value / total_monthly_revenue) * 100
    percentages_by_state[state] = percentage

# Exibe os resultados
for state, percentage in percentages_by_state.items():
    print(f"{state}: {percentage:.2f}%")