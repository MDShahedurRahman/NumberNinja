from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(frozen=True)
class RoundConfig:
    low: int
    high: int
    max_attempts: int


@dataclass
class RoundState:
    config: RoundConfig
    secret: int
    attempts_used: int = 0
    last_guess: Optional[int] = None
    is_over: bool = False
    is_win: bool = False
