import math

# Dados
tempo_PL1 = [17, 16, 21, 14, 18, 24, 16, 21, 14, 23, 18, 18, 14, 13, 15]
tempo_PL2 = [18, 14, 19, 11, 23, 21, 10, 19, 13, 24, 15, 20, 15, 21, 16]

# Função para calcular a média
def media(dados):
    return sum(dados) / len(dados)

# Calcular as diferenças
diferencas = [tempo_PL1[i] - tempo_PL2[i] for i in range(len(tempo_PL1))]

# Média das diferenças
media_diferencas = media(diferencas)

# Função para calcular o desvio padrão
def desvio_padrao(dados, media_valor):
    variancia = sum((x - media_valor) ** 2 for x in dados) / (len(dados) - 1)
    return math.sqrt(variancia)

# Desvio padrão das diferenças
desvio_padrao_diferencas = desvio_padrao(diferencas, media_diferencas)

# Tamanho da amostra
n = len(diferencas)

# Calcular o valor t
t = media_diferencas / (desvio_padrao_diferencas / math.sqrt(n))

# Valor crítico t para 95% de confiança e 14 graus de liberdade (aproximadamente)
t_critico = 2.145

print(f"Média das diferenças: {media_diferencas}")
print(f"Desvio padrão das diferenças: {desvio_padrao_diferencas}")
print(f"Valor t: {t}")
print(f"Valor crítico t para 95% de confiança: {t_critico}")

# Decisão
if abs(t) > t_critico:
    print("Rejeitamos a hipótese nula (H0). Há evidência suficiente para concluir que as linguagens possuem desempenhos diferentes.")
else:
    print("Não rejeitamos a hipótese nula (H0). Não há evidência suficiente para concluir que as linguagens possuem desempenhos diferentes.")
