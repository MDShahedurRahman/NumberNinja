import random
import pytest

from game import (
    get_config,
    new_round,
    validate_guess,
    apply_guess,
    score_for_round,
    feedback,
)


# -------------------------
# Config & validation tests
# -------------------------

def test_get_config_easy():
    cfg = get_config("easy")
    assert cfg.low == 1
    assert cfg.high == 20
    assert cfg.max_attempts == 6


def test_get_config_invalid():
    with pytest.raises(ValueError):
        get_config("invalid")


def test_validate_guess_ok():
    cfg = get_config("easy")
    guess, err = validate_guess("10", cfg)
    assert guess == 10
    assert err == ""


def test_validate_guess_invalid_input():
    cfg = get_config("easy")
    guess, err = validate_guess("abc", cfg)
    assert guess is None
    assert "Invalid" in err


def test_validate_guess_out_of_range():
    cfg = get_config("easy")
    guess, err = validate_guess("999", cfg)
    assert guess is None
    assert "Out of range" in err


# -------------------------
# Game round behavior tests
# -------------------------

def test_apply_guess_win():
    cfg = get_config("easy")
    rng = random.Random(0)
    state = new_round(cfg, rng=rng)

    secret = state.secret
    msg = apply_guess(state, secret)

    assert state.is_over is True
    assert state.is_win is True
    assert "Correct" in msg


def test_apply_guess_loss_after_max_attempts():
    cfg = get_config("easy")
    rng = random.Random(1)
    state = new_round(cfg, rng=rng)

    wrong_guess = cfg.low if state.secret != cfg.low else cfg.high

    for _ in range(cfg.max_attempts):
        msg = apply_guess(state, wrong_guess)

    assert state.is_over is True
    assert state.is_win is False
    assert "No attempts left" in msg
    assert score_for_round(state) == 0


def test_score_positive_on_win():
    cfg = get_config("easy")
    rng = random.Random(2)
    state = new_round(cfg, rng=rng)

    apply_guess(state, state.secret)
    score = score_for_round(state)

    assert score > 0


# ------------------------------------------------
# STEP 16: Feedback progression (warmer / colder)
# ------------------------------------------------

def test_feedback_first_guess_high_low():
    secret = 50

    msg_high = feedback(secret, 60, None)
    msg_low = feedback(secret, 40, None)

    assert msg_high == "Too high."
    assert msg_low == "Too low."


def test_feedback_warmer_when_closer():
    secret = 50
    # Last guess was farther (60 → diff 10)
    # New guess is closer (55 → diff 5)
    msg = feedback(secret, 55, 60)

    assert "warmer" in msg.lower()
