# Predição da Inadimplência de Crédito com Análise de Sentimento

**Trabalho de Conclusão de Curso**  
Isabella Akemi Farabotti

---

## Estrutura do repositório

### Notebooks

Os notebooks devem ser executados **na ordem indicada**, pois cada um depende dos arquivos gerados pelo anterior.

| Notebook | Objetivo | Entrada | Saída |
|---|---|---|---|
| [`notebook01.ipynb`](./notebook01.ipynb) | Coleta e preparação da série de inadimplência | SGS/BCB | `base_series.csv` |
| [`notebook02.ipynb`](./notebook02.ipynb) | Modelo base ARIMA sem sentimento | `base_series.csv` | `resultados_sem_sentimento.csv` |
| [`notebook03.ipynb`](./notebook03.ipynb) | Coleta e extração dos textos do BCB | `COPOM.zip`, `Estatísticas.zip` | `base_relatorios.csv` |
| [`notebook04.ipynb`](./notebook04.ipynb) | Análise de sentimento — todos os modelos e documentos | `base_relatorios.csv` | `base_sentimentos.csv` |
| [`notebook05.ipynb`](./notebook05.ipynb) | Preparação dos lags de sentimento | `base_sentimentos.csv` | `base_completa.csv` |
| [`notebook06.ipynb`](./notebook06.ipynb) | Modelos preditivos com sentimento | `base_completa.csv` | `resultados_com_sentimento.csv` |
| [`notebook07.ipynb`](./notebook07.ipynb) | Comparativo final baseline vs. sentimento | `resultados_sem_sentimento.csv` + `resultados_com_sentimento.csv` | Tabelas e gráficos finais |

### Arquivos de dados

| Arquivo | Gerado por | Descrição |
|---|---|---|
| [`base_series.csv`](./base_series.csv) | Notebook 01 | Série histórica de inadimplência com lags |
| [`base_relatorios.csv`](./base_relatorios.csv) | Notebook 03 | Textos dos documentos do BCB organizados por tipo e data |
| [`base_sentimentos.csv`](./base_sentimentos.csv) | Notebook 04 | Scores de sentimento por documento, modelo e data |
| [`base_completa.csv`](./base_completa.csv) | Notebook 05 | Base unificada com inadimplência, lags e scores de sentimento |
| [`resultados_sem_sentimento.csv`](./resultados_sem_sentimento.csv) | Notebook 02 | Métricas dos modelos baseline (ARIMA, SVR, XGBoost) |
| [`resultados_com_sentimento.csv`](./resultados_com_sentimento.csv) | Notebook 06 | Métricas dos modelos com sentimento — top 3 por família |
| [`COPOM.zip`](./COPOM.zip) | — | PDFs das Atas do Copom |
| [`Estatísticas monetárias e de crédito.zip`](./Estatísticas%20monetárias%20e%20de%20crédito.zip) | — | PDFs dos Relatórios de Estatísticas |

### Ordem de execução

```
notebook01 → notebook02
           → notebook03 → notebook04 → notebook05 → notebook06 → notebook07
```

---

## Como reproduzir os resultados

### Pré-requisitos

- Python 3.10 ou superior
- As dependências podem ser instaladas via `pip` na primeira célula de cada notebook:

```bash
pip install pandas numpy matplotlib statsmodels scikit-learn xgboost-cpu
```

Para os modelos de sentimento baseados em Transformers (BERT, FinBERT), instale adicionalmente:

```bash
pip install transformers torch
```

O modelo Mistral requer a instalação do **Ollama** com o modelo `mistral` disponível localmente. Consulte a documentação em [ollama.com](https://ollama.com).

### Ambiente recomendado

Os notebooks foram desenvolvidos e testados no **Google Colab** e no **GitHub Codespaces**. Qualquer ambiente com Python 3.10+ e acesso ao sistema de arquivos local é compatível.

### Atalho: pular a análise de sentimento

Os arquivos `base_sentimentos.csv` e `base_completa.csv` já estão disponíveis no repositório. Caso não queira reexecutar o Notebook 04 — que requer Ollama/Mistral e modelos Transformer —, é possível iniciar diretamente pelo **Notebook 05**, usando os arquivos pré-gerados.

Da mesma forma, os arquivos `resultados_sem_sentimento.csv` e `resultados_com_sentimento.csv` permitem executar o **Notebook 07** diretamente, sem reexecutar os modelos preditivos.

---

## Principais resultados

O modelo base **ARIMA(2,1,4) com correção de bias** apresentou RMSE de **0,0973** no conjunto de teste.

Entre os modelos com sentimento, o melhor resultado foi obtido pelo **ARIMAX com Mistral aplicado às Atas do Copom**, com RMSE de **0,0852** — redução de aproximadamente **12,4%** em relação ao baseline.

A família ARIMAX foi a única que apresentou ganho preditivo consistente com a inclusão de sentimento. SVR e XGBoost não melhoraram em relação aos seus respectivos baselines no período analisado.

A principal conclusão é que o sentimento extraído dos documentos do Banco Central **possui valor preditivo para a inadimplência**, especialmente quando incorporado via ARIMAX às Atas do Copom, que têm caráter prospectivo e tendem a antecipar movimentos da política monetária.

---

## Tecnologias utilizadas

- **Python** — linguagem principal
- **Pandas / NumPy** — manipulação e computação numérica
- **Matplotlib** — visualizações
- **Statsmodels** — modelos ARIMA e ARIMAX
- **Scikit-learn** — SVR e pré-processamento
- **XGBoost** — modelo de *gradient boosting*
- **NLTK / TextBlob** — análise de sentimento léxica
- **Transformers (Hugging Face)** — BERT Multilingual e FinBERT-PT-BR
- **Ollama / Mistral** — LLM para análise de sentimento
- **Google Colab / GitHub Codespaces** — ambientes de execução
