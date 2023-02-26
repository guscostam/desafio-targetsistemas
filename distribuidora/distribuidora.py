faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

soma = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = (valor / soma) * 100
    print(f'{estado}: {percentual:.2f}%')