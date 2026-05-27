# mission-control-ai

## Equipe

**Missão:** Projeto_Helios  
**Equipe:** Polaris

---

## Como executar

Não é necessário instalar nenhuma biblioteca externa. Basta ter o Python 3 instalado.

```cmd
python mission_control.py
```

---

## Estrutura do projeto
mission-control-ai/
│
├── README.md
└── mission_control.py

---

## Estrutura dos dados

O sistema utiliza uma matriz chamada `dados_missao` onde cada linha representa um ciclo e cada coluna uma área monitorada:

| Posição | Informação   | Unidade |
|---------|-------------|---------|
| 0       | Temperatura  | °C      |
| 1       | Comunicação  | %       |
| 2       | Bateria      | %       |
| 3       | Oxigênio     | %       |
| 4       | Estabilidade | %       |

---

## Regras de alerta

### Temperatura
| Condição              | Status   |
|-----------------------|----------|
| Menor que 18°C        | ATENCAO  |
| De 18°C até 30°C      | NORMAL   |
| De 30°C até 35°C      | ATENCAO  |
| Maior que 35°C        | CRITICO  |

### Comunicação
| Condição       | Status   |
|----------------|----------|
| Menor que 30%  | CRITICO  |
| De 30% a 59%   | ATENCAO  |
| 60% ou mais    | NORMAL   |

### Bateria
| Condição       | Status   |
|----------------|----------|
| Menor que 20%  | CRITICO  |
| De 20% a 49%   | ATENCAO  |
| 50% ou mais    | NORMAL   |

### Oxigênio
| Condição       | Status   |
|----------------|----------|
| Menor que 80%  | CRITICO  |
| De 80% a 89%   | ATENCAO  |
| 90% ou mais    | NORMAL   |

### Estabilidade
| Condição       | Status   |
|----------------|----------|
| Menor que 40%  | CRITICO  |
| De 40% a 69%   | ATENCAO  |
| 70% ou mais    | NORMAL   |

---

## Pontuação de risco

| Status   | Pontos |
|----------|--------|
| NORMAL   | 0      |
| ATENCAO  | 1      |
| CRITICO  | 2      |

### Classificação do ciclo

| Pontuação total | Classificação       |
|-----------------|---------------------|
| 0 a 2 pontos    | MISSAO ESTAVEL      |
| 3 a 5 pontos    | MISSAO EM ATENCAO   |
| 6 a 10 pontos   | MISSAO CRITICA      |

---

## Funções do sistema

| Função                            | Descrição                                        |
|-----------------------------------|--------------------------------------------------|
| `analisar_temperatura()`          | Classifica a temperatura e retorna pontuação     |
| `analisar_comunicacao()`          | Classifica a comunicação e retorna pontuação     |
| `analisar_bateria()`              | Classifica a bateria e retorna pontuação         |
| `analisar_oxigenio()`             | Classifica o oxigênio e retorna pontuação        |
| `analisar_estabilidade()`         | Classifica a estabilidade e retorna pontuação    |
| `calcular_risco_ciclo()`          | Soma a pontuação total de um ciclo               |
| `classificar_ciclo()`             | Retorna a classificação com base na pontuação    |
| `gerar_recomendacao()`            | Gera recomendações automáticas para o ciclo      |
| `analisar_tendencia()`            | Compara o primeiro e último ciclo                |
| `identificar_area_mais_afetada()` | Identifica a área com maior risco acumulado      |
| `gerar_relatorio_final()`         | Exibe o relatório completo da missão             |