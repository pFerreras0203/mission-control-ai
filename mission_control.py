NOME_MISSAO = "Missao"
NOME_EQUIPE = "Pedro's"

dados_missao = [
    [22, 95, 91, 98, 95],
    [26, 83, 76, 95, 88],
    [32, 61, 54, 90, 68],
    [37, 44, 35, 85, 52],
    [41, 25, 17, 76, 32],
    [35, 52, 29, 80, 47],
]

areas_monitoradas = [
    "Temperatura interna",
    "Comunicacao com a base",
    "Sistema de energia",
    "Suporte de oxigenio",
    "Estabilidade operacional"
]

def analisar_temperatura(valor):
    if valor < 18:
      return "ATENCAO", 1, "Temperatura baixa"
    elif valor <= 30:
        return "NORMAL", 0, "Temperatura normal"
    elif valor <= 35:
        return "ATENCAO", 1, "Temperatura elevada"
    else:
        return "CRITICO", 2, "Risco de superaquecimento"

def analisar_comunicacao(valor):
    if valor < 30:
        return "CRITICO", 2, "Comunicacao com a base em nivel critico"
    elif valor <= 59:
        return "ATENCAO", 1, "Comunicacao instavel"
    else:
        return "NORMAL", 0, "Comunicacao normal"

def analisar_bateria(valor):
    if valor < 20:
        return "CRITICO", 2, "Bateria em nivel critico"
    elif valor <= 49:
        return "ATENCAO", 1, "Bateria abaixo do recomendado"
    else:
        return "NORMAL", 0, "Energia normal"

def analisar_oxigenio(valor):
    if valor < 80:
        return "CRITICO", 2, "Oxigenio em nivel critico"
    elif valor <= 89:
        return "ATENCAO", 1, "Oxigenio abaixo do ideal"
    else:
        return "NORMAL", 0, "Oxigenio normal"