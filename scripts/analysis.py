def overall_survival_rate(df):
    rate = df['Survived'].mean() * 100
    return f"{rate:.1f}%"


def survival_by_gender(df):
    result = df.groupby('Sex')['Survived'].mean() * 100
    return result.round(1).astype(str) + "%"


def survival_by_class(df):
    result = df.groupby('Pclass')['Survived'].mean() * 100
    return result.round(1).astype(str) + "%"
