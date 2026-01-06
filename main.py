from __future__ import annotations

from game import get_config, new_round, validate_guess, apply_guess, score_for_round
from storage import load_scores, save_best


MENU = """
NumberNinja 🎯
--------------
1) Play (Easy)
2) Play (Medium)
3) Play (Hard)
4) View Best Score
5) Reset Best Score
6) Quit
"""


def play(difficulty: str) -> int:
    cfg = get_config(difficulty)
    state = new_round(cfg)

    print(f"\nDifficulty: {difficulty.title()}")
    print(f"Guess a number between {cfg.low} and {cfg.high}")
    print(f"Attempts: {cfg.max_attempts}\n")

    while not state.is_over:
        raw = input("Your guess: ")
        guess, err = validate_guess(raw, cfg)
        if err:
            print(err)
            continue
        msg = apply_guess(state, guess)
        print(msg)

    score = score_for_round(state)
    if score > 0:
        print(f"Score: {score}\n")
    else:
        print("Score: 0\n")
    return score
