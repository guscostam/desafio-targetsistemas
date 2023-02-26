import json

with open('dados.json', 'r') as arquivo:
    conteudo = json.load(arquivo)

valores = []

for elemento in conteudo:
    valores.append(elemento['valor'])


menor_valor = min(valores)
maior_valor = max(valores)

def dias_faturamento():
    count = 0
    for valor in valores:
        if valor > media():
            count += 1
    return count

def media():
    soma = sum(valores)
    media = soma / len(valores)
    return media

print(menor_valor)
print(maior_valor)
print(dias_faturamento())