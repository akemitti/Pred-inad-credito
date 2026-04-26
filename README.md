# Pred-inad-credito

Projeto de TCC sobre **predição da inadimplência de crédito no Brasil** com uso de **séries temporais** — dados observados ao longo do tempo —, **machine learning** — aprendizado de máquina — e **análise de sentimento** — classificação do tom dos textos — aplicada a documentos do Banco Central do Brasil.

## Visão geral

A inadimplência de crédito é uma variável relevante para instituições financeiras, pois impacta precificação, provisão, gestão de risco, concessão de crédito e planejamento estratégico.

Este projeto investiga se, além das variáveis macroeconômicas e de crédito tradicionalmente utilizadas, o **tom de documentos oficiais do Banco Central do Brasil** pode contribuir para melhorar a capacidade preditiva dos modelos de inadimplência.

A proposta combina:

- **dados econômicos e de crédito**;
- **modelos estatísticos e de machine learning** — aprendizado de máquina;
- **processamento de linguagem natural (PLN)** — técnicas para tratar e analisar textos;
- **análise de sentimento** — mensuração do tom positivo, negativo ou neutro dos documentos;
- **comparação entre modelos com e sem variáveis textuais**.

## Objetivo

Desenvolver e comparar modelos para **predizer a inadimplência de crédito no Brasil**, avaliando se a inclusão de variáveis derivadas de textos do Banco Central agrega valor preditivo ao modelo.

## Pergunta de pesquisa

**A análise de sentimento de documentos do Banco Central melhora a predição da inadimplência de crédito no Brasil?**

## Fontes de dados

O projeto utiliza duas principais fontes de informação:

### 1. Séries temporais econômicas e de crédito

Dados obtidos a partir do **SGS/BCB** — Sistema Gerenciador de Séries Temporais do Banco Central do Brasil —, incluindo variáveis como:

- inadimplência total;
- saldo da carteira de crédito;
- concessões de crédito;
- taxa média de juros;
- Selic;
- IPCA.

### 2. Documentos textuais do Banco Central

Foram analisados dois tipos de documentos:

- **Atas do Copom** — documentos com caráter mais prospectivo, voltados a expectativas, riscos, inflação, atividade econômica, crédito e política monetária;
- **Relatórios de Estatísticas Monetárias e de Crédito** — documentos de caráter mais descritivo, voltados à divulgação de dados e estatísticas do mercado de crédito.

## Metodologia

O projeto foi desenvolvido em etapas, organizadas em notebooks.

### Etapas principais

1. **Construção da base de dados**
   - Coleta e organização das séries temporais econômicas e de crédito;
   - Tratamento e padronização das bases;
   - Consolidação das variáveis utilizadas na modelagem.

2. **Modelo base de predição**
   - Construção de modelos para previsão da inadimplência;
   - Avaliação inicial de desempenho sem variáveis textuais.

3. **Coleta e preparação textual**
   - Extração e tratamento dos textos dos documentos do Banco Central;
   - Organização dos documentos por tipo e data.

4. **Análise de sentimento**
   - Aplicação de diferentes abordagens de análise de sentimento:
     - **NLTK/VADER** — método léxico, baseado em dicionário de polaridade;
     - **TextBlob** — biblioteca simples de processamento de linguagem natural;
     - **BERT Multilingual** — modelo de linguagem multilíngue;
     - **FinBERT-PT-BR** — modelo adaptado ao contexto financeiro em português;
     - **Mistral** — LLM, modelo de linguagem de grande porte.

5. **Comparação dos sentimentos com a inadimplência**
   - Correlação entre os scores de sentimento e a série de inadimplência;
   - Testes com diferentes defasagens temporais, ou **lags** — deslocamentos no tempo;
   - Comparação entre os resultados das Atas do Copom e dos Relatórios de Estatísticas.

6. **Integração ao modelo preditivo**
   - Inclusão dos melhores scores de sentimento no modelo XGBoost;
   - Comparação entre modelo base e modelos com variáveis textuais;
   - Avaliação do ganho preditivo por meio de métricas como MAE, RMSE e R².

## Estrutura do repositório

| Notebook | Objetivo | Status |
|---|---|---|
| [`notebook01.ipynb`](./notebook01.ipynb) | Coleta, organização e preparação inicial das séries econômicas e de crédito. | ✅ Concluído |
| [`notebook02.ipynb`](./notebook02.ipynb) | Construção do modelo base de predição da inadimplência sem variáveis textuais. | ✅ Concluído |
| [`notebook03.ipynb`](./notebook03.ipynb) | Coleta, extração e preparação dos documentos textuais do Banco Central. | ✅ Concluído |
| [`notebook04_sem_mistral_copom.ipynb`](./notebook04_sem_mistral_copom.ipynb) | Análise de sentimento das Atas do Copom com modelos tradicionais, sem Mistral. | ✅ Concluído |
| [`notebook04_mistral_copom.ipynb`](./notebook04_mistral_copom.ipynb) | Análise de sentimento das Atas do Copom com o modelo Mistral. | ✅ Concluído |
| [`notebook04_sem_mistral_estatisticas.ipynb`](./notebook04_sem_mistral_estatisticas.ipynb) | Análise de sentimento dos Relatórios de Estatísticas Monetárias e de Crédito com modelos tradicionais, sem Mistral. | ✅ Concluído |
| [`notebook04_mistral_estatisticas.ipynb`](./notebook04_mistral_estatisticas.ipynb) | Análise de sentimento dos Relatórios de Estatísticas Monetárias e de Crédito com o modelo Mistral. | ✅ Concluído |
| [`notebook04_completo.ipynb`](./notebook04_completo.ipynb) | Consolidação das bases de sentimento do Copom e dos Relatórios de Estatísticas em uma base final unificada. | ✅ Concluído |
| [`notebook05.ipynb`](./notebook05.ipynb) | Correlação entre sentimentos e inadimplência, comparação por tipo de relatório, seleção dos melhores modelos e respectivos lags. | ✅ Concluído |
| [`notebook06.ipynb`](./notebook06.ipynb) | Integração dos sentimentos selecionados ao modelo preditivo, comparação com o modelo base e análise do ganho de desempenho. | ✅ Concluído |

## Organização da etapa de análise de sentimento

A análise de sentimento foi separada por tipo de documento e por abordagem de modelagem.

### Atas do Copom

- `notebook04_sem_mistral_copom.ipynb`: aplica os modelos tradicionais de sentimento.
- `notebook04_mistral_copom.ipynb`: aplica o modelo Mistral.
- Os resultados são consolidados no `notebook04_completo.ipynb`.

### Relatórios de Estatísticas Monetárias e de Crédito

- `notebook04_sem_mistral_estatisticas.ipynb`: aplica os modelos tradicionais de sentimento.
- `notebook04_mistral_estatisticas.ipynb`: aplica o modelo Mistral.
- Os resultados também são consolidados no `notebook04_completo.ipynb`.

## Principais resultados parciais

A etapa de correlação indicou que os sentimentos extraídos das **Atas do Copom** apresentaram maior associação com a inadimplência do que os sentimentos extraídos dos **Relatórios de Estatísticas Monetárias e de Crédito**.

Entre os principais resultados observados:

- **Copom + Mistral**, com lag de 6 meses, apresentou a maior correlação em valor absoluto;
- **Copom + NLTK/VADER**, com lag de 1 mês, também apresentou correlação relevante;
- os Relatórios de Estatísticas apresentaram correlações mais fracas, sugerindo menor poder explicativo individual em relação à inadimplência.

Esse resultado é coerente com a natureza dos documentos: as Atas do Copom possuem conteúdo mais prospectivo, enquanto os Relatórios de Estatísticas têm caráter mais descritivo.

## Notebook 06 — Integração ao modelo preditivo

No `notebook06.ipynb`, os melhores scores de sentimento selecionados no Notebook 05 são incorporados ao modelo XGBoost.

A comparação é realizada entre:

- modelo base com variáveis macroeconômicas;
- modelo com NLTK/VADER;
- modelo com Mistral;
- modelo com média dos modelos de sentimento;
- modelo com BERT Multilingual.

As métricas utilizadas incluem:

- **MAE** — erro absoluto médio;
- **RMSE** — raiz do erro quadrático médio;
- **R²** — coeficiente de determinação, que indica o grau de explicação do modelo.

## Tecnologias utilizadas

- Python;
- Pandas;
- NumPy;
- Matplotlib;
- Scikit-learn;
- XGBoost;
- Statsmodels;
- NLTK;
- TextBlob;
- Transformers;
- Ollama/Mistral;
- Google Colab;
- GitHub Codespaces.

## Status do projeto

✅ Coleta e preparação das bases concluídas  
✅ Análise de sentimento concluída  
✅ Correlação entre sentimento e inadimplência concluída  
✅ Integração ao modelo preditivo concluída  
✅ Comparação entre modelo base e modelos com sentimento concluída  

## Autoria

Projeto desenvolvido por **Isabella Akemi Farabotti** como parte do Trabalho de Conclusão de Curso.
