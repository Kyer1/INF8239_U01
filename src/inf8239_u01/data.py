from pathlib import Path

import pandas as pd

DATA_URL = (
    "https://archive.ics.uci.edu/static/public/697/"
    "predict+students+dropout+and+academic+success.zip"
)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_PATH = PROJECT_ROOT / "data" / "raw" / "dataset.csv"


def download_csv(url: str = DATA_URL, destination=DEFAULT_PATH, sep: str = ";") -> Path:
    """Descarga el dataset desde UCI y lo guarda como CSV en data/raw."""
    if not url.startswith(("https://", "http://")):
        raise ValueError("La fuente debe ser una URL HTTP(S)")
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    frame = pd.read_csv(url, sep=sep)
    if frame.empty:
        raise ValueError("El dataset descargado está vacío")
    frame.columns = frame.columns.str.strip()
    frame.to_csv(path, index=False)
    return path


def load_data(path=DEFAULT_PATH) -> pd.DataFrame:
    """Carga el CSV ya descargado."""
    return pd.read_csv(path)