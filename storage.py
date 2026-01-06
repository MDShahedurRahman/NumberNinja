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
