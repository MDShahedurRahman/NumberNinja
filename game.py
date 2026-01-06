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


def get_config(difficulty: str) -> RoundConfig:
    d = difficulty.strip().lower()
    if d == "easy":
        return RoundConfig(low=1, high=20, max_attempts=6)
    if d == "medium":
        return RoundConfig(low=1, high=50, max_attempts=7)
    if d == "hard":
        return RoundConfig(low=1, high=100, max_attempts=8)
    raise ValueError("difficulty must be one of: easy, medium, hard")
