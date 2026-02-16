def clean_sex(df):
    df['Sex'] = df['Sex'].str.capitalize().str.strip()
    return df
