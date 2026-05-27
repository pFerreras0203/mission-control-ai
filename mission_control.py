NOME_MISSAO = "Missao_espacial1"
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

def analisar_estabilidade(valor):
    if valor < 40:
        return "CRITICO", 2, "Estabilidade operacional critica"
    elif valor <= 69:
        return "ATENCAO", 1, "Estabilidade operacional reduzida"
    else:
        return "NORMAL", 0, "Estabilidade operacional normal"

def calcular_risco_ciclo(ciclo):
    _, pontos_temp,  _ = analisar_temperatura(ciclo[0])
    _, pontos_com,   _ = analisar_comunicacao(ciclo[1])
    _, pontos_bat,   _ = analisar_bateria(ciclo[2])
    _, pontos_oxi,   _ = analisar_oxigenio(ciclo[3])
    _, pontos_est,   _ = analisar_estabilidade(ciclo[4])

    return pontos_temp + pontos_com + pontos_bat + pontos_oxi + pontos_est

def classificar_ciclo(pontuacao):
    if pontuacao <= 2:
        return "MISSAO ESTAVEL"
    elif pontuacao <= 5:
        return "MISSAO EM ATENCAO"
    else:
        return "MISSAO CRITICA"

def gerar_recomendacao(ciclo):
    _, pontos_temp, _ = analisar_temperatura(ciclo[0])
    _, pontos_com,  _ = analisar_comunicacao(ciclo[1])
    _, pontos_bat,  _ = analisar_bateria(ciclo[2])
    _, pontos_oxi,  _ = analisar_oxigenio(ciclo[3])
    _, pontos_est,  _ = analisar_estabilidade(ciclo[4])

    recomendacoes = []

    if pontos_temp == 2:
        recomendacoes.append("Verificar controle termico da missao")
    if pontos_com == 2:
        recomendacoes.append("Tentar restabelecer contato com a base")
    if pontos_bat == 2:
        recomendacoes.append("Ativar modo de economia de energia")
    if pontos_oxi == 2:
        recomendacoes.append("Acionar protocolo de suporte a vida")
    if pontos_est == 2:
        recomendacoes.append("Reduzir operacoes nao essenciais")

    if not recomendacoes:
        return "Manter operacao normal e continuar monitoramento"

    return " | ".join(recomendacoes)

def analisar_tendencia():
    risco_primeiro = calcular_risco_ciclo(dados_missao[0])
    risco_ultimo = calcular_risco_ciclo(dados_missao[-1])

    if risco_ultimo > risco_primeiro:
        return "A missao apresentou tendencia de piora"
    elif risco_ultimo < risco_primeiro:
        return "A missao apresentou tendencia de melhora"
    else:
        return "A missao permaneceu estavel em relacao ao inicio"

def identificar_area_mais_afetada():
    pontos_por_area = [0, 0, 0, 0, 0]

    for ciclo in dados_missao:
        _, p0, _ = analisar_temperatura(ciclo[0])
        _, p1, _ = analisar_comunicacao(ciclo[1])
        _, p2, _ = analisar_bateria(ciclo[2])
        _, p3, _ = analisar_oxigenio(ciclo[3])
        _, p4, _ = analisar_estabilidade(ciclo[4])

        pontos_por_area[0] += p0
        pontos_por_area[1] += p1
        pontos_por_area[2] += p2
        pontos_por_area[3] += p3
        pontos_por_area[4] += p4

    maior_indice = pontos_por_area.index(max(pontos_por_area))
    return areas_monitoradas[maior_indice], pontos_por_area

def gerar_relatorio_final():
    riscos = [calcular_risco_ciclo(ciclo) for ciclo in dados_missao]

    media_temp = sum(ciclo[0] for ciclo in dados_missao) / len(dados_missao)
    media_com  = sum(ciclo[1] for ciclo in dados_missao) / len(dados_missao)
    media_bat  = sum(ciclo[2] for ciclo in dados_missao) / len(dados_missao)
    media_oxi  = sum(ciclo[3] for ciclo in dados_missao) / len(dados_missao)
    media_est  = sum(ciclo[4] for ciclo in dados_missao) / len(dados_missao)

    ciclo_critico = riscos.index(max(riscos)) + 1
    risco_medio   = sum(riscos) / len(riscos)
    ciclos_criticos = sum(1 for r in riscos if r >= 6)

    tendencia = analisar_tendencia()
    area_mais_afetada, pontos_por_area = identificar_area_mais_afetada()
    classificacao_final = classificar_ciclo(round(risco_medio))

    print("\n" + "=" * 60)
    print("RELATORIO FINAL DA MISSAO")
    print("=" * 60)
    print(f"Missao: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"\nQuantidade de ciclos analisados: {len(dados_missao)}")
    print(f"Media de temperatura:  {media_temp:.2f} C")
    print(f"Media de comunicacao:  {media_com:.2f}%")
    print(f"Media de bateria:      {media_bat:.2f}%")
    print(f"Media de oxigenio:     {media_oxi:.2f}%")
    print(f"Media de estabilidade: {media_est:.2f}%")
    print(f"\nCiclo mais critico: Ciclo {ciclo_critico}")
    print(f"Maior pontuacao de risco: {max(riscos)}")
    print(f"Risco medio da missao: {risco_medio:.2f}")
    print(f"Quantidade de ciclos criticos: {ciclos_criticos}")
    print(f"\nTendencia da missao:")
    print(f"{tendencia}")
    print(f"\nPontuacao acumulada por area:")
    for i, area in enumerate(areas_monitoradas):
        print(f"{area}: {pontos_por_area[i]} pontos")
    print(f"\nArea mais afetada:")
    print(f"{area_mais_afetada}")
    print(f"\nClassificacao final da missao:")
    print(f"{classificacao_final}")
    print("=" * 60)

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print(f"Missao: {NOME_MISSAO}")
print(f"Equipe: {NOME_EQUIPE}")
print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
print("=" * 60)

for i, ciclo in enumerate(dados_missao):
    status_temp, _, desc_temp = analisar_temperatura(ciclo[0])
    status_com,  _, desc_com  = analisar_comunicacao(ciclo[1])
    status_bat,  _, desc_bat  = analisar_bateria(ciclo[2])
    status_oxi,  _, desc_oxi  = analisar_oxigenio(ciclo[3])
    status_est,  _, desc_est  = analisar_estabilidade(ciclo[4])

    pontuacao = calcular_risco_ciclo(ciclo)
    classificacao = classificar_ciclo(pontuacao)
    recomendacao = gerar_recomendacao(ciclo)

    print(f"\nCICLO {i + 1}")
    print("-" * 60)
    print(f"Temperatura:  {ciclo[0]} C  | {status_temp} | {desc_temp}")
    print(f"Comunicacao:  {ciclo[1]}%   | {status_com}  | {desc_com}")
    print(f"Bateria:      {ciclo[2]}%   | {status_bat}  | {desc_bat}")
    print(f"Oxigenio:     {ciclo[3]}%   | {status_oxi}  | {desc_oxi}")
    print(f"Estabilidade: {ciclo[4]}%   | {status_est}  | {desc_est}")
    print(f"\nPontuacao de risco do ciclo: {pontuacao}")
    print(f"Classificacao do ciclo: {classificacao}")
    print(f"Recomendacao: {recomendacao}")

gerar_relatorio_final()