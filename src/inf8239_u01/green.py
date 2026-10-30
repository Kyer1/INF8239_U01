def pareto_flags(df, score="f1_macro", cost="fit_median_s"):
    """Marca True si ningún otro modelo es mejor o igual en ambos criterios y estrictamente mejor en uno."""
    flags = []
    for _, row in df.iterrows():
        dominated = ((df[score] >= row[score]) & (df[cost] <= row[cost]) &
                     ((df[score] > row[score]) | (df[cost] < row[cost]))).any()
        flags.append(not bool(dominated))
    return flags