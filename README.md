# Pred-inad-credito

Projeto de TCC sobre **predição da inadimplência de crédito no Brasil** com uso de **séries temporais** — dados observados ao longo do tempo — e **análise de sentimento** — mensuração do tom dos textos — aplicada a documentos oficiais do Banco Central do Brasil.

## Visão geral

A inadimplência de crédito é uma variável relevante para instituições financeiras, pois impacta decisões relacionadas à concessão de crédito, gestão de risco, provisão, precificação e planejamento estratégico.

Este projeto investiga se o **tom de documentos oficiais do Banco Central do Brasil** pode contribuir para melhorar a previsão da inadimplência de crédito no Brasil.

A proposta compara dois tipos de abordagem:

- um modelo base de previsão, construído a partir da própria série histórica de inadimplência;
- modelos com inclusão de variáveis de sentimento extraídas de documentos do Banco Central.

Dessa forma, o foco principal do trabalho é avaliar se as informações textuais dos documentos oficiais agregam ganho preditivo em relação a um modelo puramente temporal.

## Objetivo

Desenvolver e comparar modelos para **predizer a inadimplência de crédito no Brasil**, avaliando se a inclusão de variáveis derivadas da análise de sentimento de documentos do Banco Central melhora o desempenho da previsão.

## Pergunta de pesquisa

**A análise de sentimento de documentos do Banco Central melhora a predição da inadimplência de crédito no Brasil?**

## Fontes de dados

O projeto utiliza duas principais fontes de informação.

### 1. Série de inadimplência

A série de inadimplência foi obtida a partir do **SGS/BCB** — Sistema Gerenciador de Séries Temporais do Banco Central do Brasil.

Essa série é utilizada como base para a construção do modelo temporal de referência, no qual a previsão da inadimplência é feita a partir do próprio comportamento histórico da variável.

### 2. Documentos textuais do Banco Central

Foram analisados dois tipos de documentos oficiais:

- **Atas do Copom** — documentos com caráter mais prospectivo, voltados a expectativas, riscos, inflação, atividade econômica, crédito e política monetária;
- **Relatórios de Estatísticas Monetárias e de Crédito** — documentos com caráter mais descritivo, voltados à divulgação de dados e estatísticas do mercado de crédito.

## Metodologia

O projeto foi desenvolvido em etapas, organizadas em notebooks.

### Etapas principais

1. **Construção da base de inadimplência**
   - Coleta da série de inadimplência no SGS/BCB;
   - Tratamento e padronização temporal da base;
   - Construção da variável-alvo de previsão com horizonte de 3 meses.

2. **Modelo base de predição**
   - Construção de modelos ARIMA para previsão da inadimplência sem variáveis textuais;
   - Comparação entre especificações alternativas;
   - Escolha do modelo benchmark com base no RMSE — raiz do erro quadrático médio.

3. **Coleta e preparação textual**
   - Extração dos textos dos documentos do Banco Central;
   - Tratamento dos arquivos em PDF;
   - Organização dos documentos por tipo e data.

4. **Análise de sentimento**
   - Aplicação de diferentes abordagens de análise de sentimento:
     - **NLTK/VADER** — método léxico, baseado em dicionário de polaridade;
     - **TextBlob** — biblioteca simples de processamento de linguagem natural;
     - **BERT Multilingual** — modelo de linguagem multilíngue;
     - **FinBERT-PT-BR** — modelo adaptado ao contexto financeiro em português;
     - **Mistral** — LLM, modelo de linguagem de grande porte.

5. **Preparação dos lags de sentimento**
   - Consolidação das séries de sentimento;
   - Criação de defasagens temporais, ou **lags** — deslocamentos no tempo — de até 6 meses;
   - Construção de uma base completa e auditável, registrando os lags utilizados para cada modelo de sentimento.

6. **Integração ao modelo preditivo**
   - Inclusão das variáveis de sentimento nos modelos ARIMAX — extensão do ARIMA com variável externa;
   - Seleção dos melhores lags e modelos com base no RMSE;
   - Comparação entre o modelo base sem sentimento e os modelos com sentimento.

## Estrutura do repositório

| Notebook | Objetivo | Status |
|---|---|---|
| [`notebook01.ipynb`](./notebook01.ipynb) | Coleta, organização e preparação da série de inadimplência. | ✅ Concluído |
| [`notebook02.ipynb`](./notebook02.ipynb) | Construção do modelo base de predição da inadimplência sem variáveis de sentimento. | ✅ Concluído |
| [`notebook03.ipynb`](./notebook03.ipynb) | Coleta, extração e preparação dos documentos textuais do Banco Central. | ✅ Concluído |
| [`notebook04_sem_mistral_copom.ipynb`](./notebook04_sem_mistral_copom.ipynb) | Análise de sentimento das Atas do Copom com modelos tradicionais, sem Mistral. | ✅ Concluído |
| [`notebook04_mistral_copom.ipynb`](./notebook04_mistral_copom.ipynb) | Análise de sentimento das Atas do Copom com o modelo Mistral. | ✅ Concluído |
| [`notebook04_sem_mistral_estatisticas.ipynb`](./notebook04_sem_mistral_estatisticas.ipynb) | Análise de sentimento dos Relatórios de Estatísticas Monetárias e de Crédito com modelos tradicionais, sem Mistral. | ✅ Concluído |
| [`notebook04_mistral_estatisticas.ipynb`](./notebook04_mistral_estatisticas.ipynb) | Análise de sentimento dos Relatórios de Estatísticas Monetárias e de Crédito com o modelo Mistral. | ✅ Concluído |
| [`notebook04_completo.ipynb`](./notebook04_completo.ipynb) | Consolidação das bases de sentimento do Copom e dos Relatórios de Estatísticas em uma base final unificada. | ✅ Concluído |
| [`notebook05.ipynb`](./notebook05.ipynb) | Preparação da base completa com os lags de sentimento e análise das combinações candidatas para a modelagem. | ✅ Concluído |
| [`notebook06.ipynb`](./notebook06.ipynb) | Integração das variáveis de sentimento ao modelo ARIMAX e comparação final com o modelo base. | ✅ Concluído |

## Organização da etapa de análise de sentimento

A análise de sentimento foi separada por tipo de documento e por abordagem de modelagem.

### Atas do Copom

- `notebook04_sem_mistral_copom.ipynb`: aplica os modelos tradicionais de sentimento;
- `notebook04_mistral_copom.ipynb`: aplica o modelo Mistral;
- os resultados são consolidados no `notebook04_completo.ipynb`.

### Relatórios de Estatísticas Monetárias e de Crédito

- `notebook04_sem_mistral_estatisticas.ipynb`: aplica os modelos tradicionais de sentimento;
- `notebook04_mistral_estatisticas.ipynb`: aplica o modelo Mistral;
- os resultados também são consolidados no `notebook04_completo.ipynb`.

## Notebook 05 — Preparação dos lags de sentimento

O `notebook05.ipynb` organiza a base de sentimentos para uso na modelagem preditiva.

Nesta etapa, são criados lags de até 6 meses para cada combinação de:

- tipo de documento;
- modelo de sentimento;
- defasagem temporal.

O objetivo é deixar a base completa, auditável e pronta para o teste preditivo no Notebook 06.

## Notebook 06 — Integração preditiva e comparação final

No `notebook06.ipynb`, as variáveis de sentimento são incorporadas aos modelos de previsão por meio de modelos ARIMAX.

A comparação é feita entre:

- o modelo base ARIMA, que utiliza apenas a série histórica de inadimplência;
- os modelos ARIMAX, que adicionam uma variável de sentimento como variável externa.

A avaliação é realizada principalmente por meio do **RMSE** — raiz do erro quadrático médio —, com o objetivo de verificar se a inclusão das variáveis de sentimento reduz o erro de previsão.

## Principais resultados

O modelo base ARIMA(2,1,4), com correção de bias, apresentou o melhor desempenho entre as especificações testadas, com RMSE de aproximadamente **0,1841**.

Entre os modelos com sentimento, o melhor resultado foi obtido pelo modelo **ARIMAX com FinBERT aplicado aos Relatórios de Estatísticas Monetárias e de Crédito no lag 1**, com RMSE de aproximadamente **0,1868**.

Apesar de as variáveis de sentimento acompanharem razoavelmente a trajetória da inadimplência, elas não reduziram o erro de previsão em relação ao modelo base.

Assim, a principal conclusão do exercício é que o sentimento extraído dos documentos do Banco Central possui valor interpretativo, mas, na especificação testada, não apresentou ganho preditivo em relação ao modelo puramente temporal.

## Tecnologias utilizadas

- Python;
- Pandas;
- NumPy;
- Matplotlib;
- Statsmodels;
- NLTK;
- TextBlob;
- Transformers;
- Ollama/Mistral;
- Google Colab;
- GitHub Codespaces.

## Status do projeto

✅ Coleta e preparação da série de inadimplência concluída  
✅ Coleta e preparação dos documentos textuais concluída  
✅ Análise de sentimento concluída  
✅ Construção dos lags de sentimento concluída  
✅ Modelo base ARIMA concluído  
✅ Modelos ARIMAX com sentimento concluídos  
✅ Comparação final entre modelo base e modelos com sentimento concluída  

## Autoria

Projeto desenvolvido por **Isabella Akemi Farabotti** como parte do Trabalho de Conclusão de Curso.
