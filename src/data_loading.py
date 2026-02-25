import json
from pathlib import Path
import pandas as pd


def _find_project_root(start: Path) -> Path:
    current = start
    for _ in range(10):
        if (current / "data").exists() and (current / "src").exists():
            return current
        current = current.parent
    return start


def load_raw_data(path: str = "data/raw_credit_applications.json") -> pd.DataFrame:
    start = Path(__file__).resolve()
    project_root = _find_project_root(start)

    full_path = project_root / path

    if not full_path.exists():
        raise FileNotFoundError(
            f"Could not find data file at: {full_path}\n"
            f"Project root used: {project_root}\n"
            f"Available files in data/: {[p.name for p in (project_root / 'data').glob('*')]}"
        )

    with open(full_path, "r", encoding="utf8") as f:
        data = json.load(f)

    return pd.json_normalize(data, sep=".")
