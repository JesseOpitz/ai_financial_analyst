import pandas as pd
from tempfile import NamedTemporaryFile

def load_file(file) -> pd.DataFrame:
    with NamedTemporaryFile(delete=False) as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name

    if file.filename.endswith(".csv"):
        df = pd.read_csv(tmp_path)
    elif file.filename.endswith(".xlsx"):
        df = pd.read_excel(tmp_path)
    else:
        raise ValueError("Unsupported file type")
    
    return df


def sample_columns(df, n=3):
    samples = {}
    for col in df.columns:
        samples[col] = df[col].dropna().astype(str).head(n).tolist()
    return samples
