import random


from game import (
    get_config,
    new_round,
    validate_guess,
    apply_guess,
    score_for_round,
)


def test_get_config_easy():
    cfg = get_config("easy")
    assert cfg.low == 1 and cfg.high == 20 and cfg.max_attempts == 6


def test_validate_guess_ok():
    cfg = get_config("easy")
    guess, err = validate_guess("10", cfg)
    assert guess == 10
    assert err == ""


def test_validate_guess_invalid():
    cfg = get_config("easy")
    guess, err = validate_guess("abc", cfg)
    assert guess is None
    assert "Invalid" in err


def test_validate_guess_out_of_range():
    cfg = get_config("easy")
    guess, err = validate_guess("999", cfg)
    assert guess is None
    assert "Out of range" in err


def test_apply_guess_win_scores_positive():
    cfg = get_config("easy")
    rng = random.Random(0)
    state = new_round(cfg, rng=rng)

    # With seed 0, secret is deterministic for this config
    secret = state.secret

    msg = apply_guess(state, secret)
    assert state.is_over is True
    assert state.is_win is True
    assert "Correct" in msg

    score = score_for_round(state)
    assert score > 0
