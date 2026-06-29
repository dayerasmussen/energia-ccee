# Faxina de Dados — PLD Médio Mensal (CCEE)

## O que é esse projeto
Limpeza e tratamento de dados públicos do mercado de energia elétrica brasileiro.
A base usada é o PLD Final Médio Mensal por submercado, disponibilizada pela CCEE.

## Fonte dos dados
Portal Dados Abertos CCEE — dadosabertos.ccee.org.br

## O que foi feito
- Leitura do arquivo CSV bruto
- Investigação da estrutura: linhas, colunas, tipos e valores vazios
- Transformação da coluna de mês de número para data
- Padronização dos nomes das colunas para letras minúsculas
- Verificação de duplicatas
- Validação dos valores (preços positivos e dentro do esperado)
- Exportação da base limpa em novo arquivo CSV

## Ferramentas utilizadas
- Python
- pandas
- Jupyter Notebook
- VS Code

## Arquivos
- `faxina.ipynb` — notebook com todo o processo documentado
- `pld_final_preco_medio.csv` — arquivo original da CCEE
- `pld_final_limpo.csv` — arquivo limpo, produto final da análise
