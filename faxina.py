# Projeto: Faxina de Dados — PLD Mercado de Energia CCEE
# Descrição: Limpeza e tratamento de dados públicos do PLD Final Médio
# Ferramentas: Python, pandas

import pandas as pd

# ============================================================================
# FASE 1: Leitura do arquivo CSV
# ============================================================================

# Carregar o CSV com separador ; e encoding latin-1 (padrão brasileiro)
df = pd.read_csv(
    "pld_final_preco_medio.csv",
    sep=";",
    encoding="latin-1"
)

print("Arquivo carregado com sucesso")
print(f"Dimensões: {df.shape[0]} linhas, {df.shape[1]} colunas")
print("\nPrimeiras 5 linhas:")
print(df.head())

# ============================================================================
# FASE 2: Diagnóstico inicial
# ============================================================================

print("\n--- DIAGNÓSTICO INICIAL ---")
print("\nTipos de dados e valores vazios:")
print(df.info())

print(f"\nTotal de linhas duplicadas: {df.duplicated().sum()}")

# ============================================================================
# FASE 3: Padronização de nomes das colunas
# ============================================================================

# Converter todos os nomes para minúsculo
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\nNomes das colunas padronizados")

# ============================================================================
# FASE 4: Conversão de datas
# ============================================================================

# Transformar a coluna de mês (201304 = abril 2013) em data real
df["mes"] = pd.to_datetime(df["mes_referencia"].astype(str), format="%Y%m")

print("Data convertida para tipo datetime")
print(df[["mes_referencia", "mes"]].head())

# ============================================================================
# FASE 5: Validação dos dados numéricos
# ============================================================================

print("\n--- RESUMO ESTATÍSTICO ---")
print(df.describe())

# Conferir se não tem valores negativos
precos_negativos = (df["pld_final_medio"] < 0).sum()
print(f"\nPreços negativos encontrados: {precos_negativos}")

# ============================================================================
# FASE 6: Salvamento da base limpa
# ============================================================================

# Exportar o arquivo limpo em CSV
df.to_csv("pld_final_limpo.csv", index=False)

print("\nArquivo salvo como 'pld_final_limpo.csv'")
print("Processo concluído com sucesso!")