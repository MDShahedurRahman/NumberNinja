from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any


@dataclass(frozen=True)
class StoragePaths:
    base_dir: Path
    scores_file: Path


def get_paths() -> StoragePaths:
    home = Path(os.path.expanduser("~"))
    base = home / ".numberninja"
    return StoragePaths(base_dir=base, scores_file=base / "scores.json")


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return default


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_scores() -> Dict[str, int]:
    paths = get_paths()
    data = read_json(paths.scores_file, {"best": 0})
    best = int(data.get("best", 0))
    return {"best": best}


def save_best(best: int) -> None:
    paths = get_paths()
    write_json(paths.scores_file, {"best": int(best)})
