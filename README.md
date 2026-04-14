# Pred-inad-credito

Projeto de TCC sobre **predição da inadimplência de crédito no Brasil** com uso de **séries temporais (dados observados ao longo do tempo)**, **machine learning (aprendizado de máquina)** e **análise de sentimento (classificação do tom dos textos)** aplicada a documentos do Banco Central do Brasil.

## Visão geral

A inadimplência de crédito é uma variável relevante para instituições financeiras, pois impacta precificação, provisão, gestão de risco e planejamento. Este projeto investiga se, além das variáveis macroeconômicas e de crédito tradicionalmente utilizadas, o **tom de documentos oficiais do Banco Central** pode contribuir para melhorar a capacidade preditiva dos modelos.

A proposta combina:

- **dados econômicos e de crédito**;
- **modelos estatísticos e de machine learning (aprendizado de máquina)**;
- **análise de sentimento (classificação do tom dos textos)** de documentos institucionais.

## Objetivo

Desenvolver e comparar modelos para **predizer a inadimplência de crédito no Brasil**, avaliando se a inclusão de variáveis derivadas de textos do Banco Central agrega valor preditivo ao modelo.

## Pergunta de pesquisa

**A análise de sentimento de documentos do Banco Central melhora a predição da inadimplência de crédito no Brasil?**

## Metodologia

O projeto foi desenvolvido em etapas, organizadas em notebooks:

### Etapas principais

1. **Construção da base de dados**
   - Coleta e organização das séries temporais (dados ao longo do tempo) econômicas e de crédito;
   - Tratamento e padronização das bases;
   - Consolidação das variáveis utilizadas na modelagem.

2. **Predição da inadimplência**
   - Desenvolvimento do modelo base de previsão;
   - Avaliação inicial do desempenho preditivo.

3. **Extração e preparação de textos**
   - Leitura e estruturação de documentos do Banco Central;
   - Geração de bases textuais para análise de sentimento.

4. **Análise de sentimento**
   - Aplicação de diferentes abordagens de análise de sentimento, como:
     - **BERT Multilingual (modelo de linguagem multilíngue)**;
     - **FinBERT-PT-BR (modelo especializado em linguagem financeira em português)**;
     - **NLTK/VADER (método léxico para sentimento)**;
     - **TextBlob (ferramenta simples de processamento de linguagem natural)**;
     - **Mistral (LLM, modelo de linguagem de grande porte)**.

5. **Seleção das melhores combinações**
   - Comparação entre modelos de sentimento;
   - Testes de correlação com a inadimplência em diferentes defasagens.

6. **Integração ao modelo preditivo**
   - Inclusão das variáveis de sentimento selecionadas no modelo de predição da inadimplência.

7. **Comparativo final**
   - Comparação entre o modelo base e o modelo com sentimento.

## Estrutura do repositório

| Notebook | Objetivo | Status |
|---|---|---|
| [`notebook01.ipynb`](./notebook01.ipynb) | Construção e preparação inicial da base de dados. | ✅ Concluído |
| [`notebook02.ipynb`](./notebook02.ipynb) | Modelo base de predição da inadimplência. | ✅ Concluído |
| [`notebook03.ipynb`](./notebook03.ipynb) | Análises auxiliares e exploração dos dados. | ✅ Concluído |
| [`notebook04_completo.ipynb`](./notebook04_completo.ipynb) | Pipeline (fluxo de processamento) completo de análise de sentimento. | ✅ Concluído |
| [`notebook04_sem_mistral.ipynb`](./notebook04_sem_mistral.ipynb) | Versão da análise de sentimento sem o modelo Mistral. | ✅ Concluído |
| [`notebook04_mistral_v2.ipynb`](./notebook04_mistral_v2.ipynb) | Versão específica da análise de sentimento com Mistral. | ✅ Concluído |
| [`notebook05.ipynb`](./notebook05.ipynb) | Comparação entre os modelos de sentimento e seleção das melhores combinações. | ✅ Concluído |
| `notebook06.ipynb` | Integração dos modelos escolhidos à predição da inadimplência. | 🚧 Em desenvolvimento |
| `notebook07.ipynb` | Comparativo entre os resultados do notebook06 e do notebook02. | 📝 Planejado |
