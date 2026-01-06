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
