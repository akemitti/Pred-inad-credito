import pandas as pd

def gerar_base_lags(df: pd.DataFrame, col_data: str, col_valor: str, prefixo: str, max_lag: int = 6) -> pd.DataFrame:
    """Gera base auditável com série presente (_t) e lags (_L1..._Lk)."""
    base = df[[col_data, col_valor]].copy()
    base[col_data] = pd.to_datetime(base[col_data])
    base = base.sort_values(col_data).reset_index(drop=True)
    out = pd.DataFrame({col_data: base[col_data], f"{prefixo}_t": base[col_valor]})
    for lag in range(1, max_lag + 1):
        out[f"{prefixo}_L{lag}"] = out[f"{prefixo}_t"].shift(lag)
    return out
