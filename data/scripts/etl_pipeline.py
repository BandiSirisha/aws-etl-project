import pandas as pd

def extract(file_path):
    return pd.read_csv(file_path)

def transform(df):
    df['sales'] = df['sales'] * 1.10  # apply 10% increase as example
    return df

def load(df, output_path):
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    raw = extract("../data/sample_data.csv")
    clean = transform(raw)
    load(clean, "../data/clean_data.csv")
