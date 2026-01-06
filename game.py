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


def new_round(config: RoundConfig, rng: Optional[random.Random] = None) -> RoundState:
    rng = rng or random.Random()
    secret = rng.randint(config.low, config.high)
    return RoundState(config=config, secret=secret)


def validate_guess(text: str, config: RoundConfig) -> Tuple[Optional[int], str]:
    """
    Returns (guess_or_none, message). message is non-empty for errors.
    """
    t = text.strip()
    if t == "":
        return None, "Enter a number."
    try:
        guess = int(t)
    except ValueError:
        return None, "Invalid input. Enter an integer."
    if guess < config.low or guess > config.high:
        return None, f"Out of range. Enter {config.low} to {config.high}."
    return guess, ""


def feedback(secret: int, guess: int, last_guess: Optional[int]) -> str:
    if guess == secret:
        return "Correct! 🎉"

    diff = abs(secret - guess)
    if last_guess is None:
        return "Too high." if guess > secret else "Too low."

    last_diff = abs(secret - last_guess)

    # Hot/Cold style
    if diff < last_diff:
        return ("Too high, but warmer 🔥" if guess > secret else "Too low, but warmer 🔥")
    if diff > last_diff:
        return ("Too high, but colder ❄️" if guess > secret else "Too low, but colder ❄️")
    return "Same distance as before."
