# NumberNinja

NumberNinja is a small Python command-line guessing game with difficulty
levels, scoring, and unit tests.\
The player must guess a secret number within a limited number of
attempts while receiving feedback such as *too high*, *too low*,
*warmer*, or *colder*.

This project is intentionally lightweight and focuses on clean logic,
testability, and professional GitHub practices.

------------------------------------------------------------------------

## Requirements

-   Python 3.9 or higher

------------------------------------------------------------------------

## Setup

Create and activate a virtual environment:

``` bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .\.venv\Scripts\Activate.ps1  # Windows PowerShell
```

Upgrade pip and install dependencies:

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

------------------------------------------------------------------------

## Run the Game

``` bash
python main.py
```

Follow the on-screen menu to select a difficulty level and start
playing.

------------------------------------------------------------------------

## Run Tests

Always run tests using the active Python interpreter:

``` bash
python -m pytest -q
```

------------------------------------------------------------------------

## How Scoring Works

Points are awarded **only when the player wins a round**.

### Base Rules

-   Losing a round gives **0 points**
-   Winning a round starts with **100 base points**

### Bonus Points

Additional points are awarded based on: - The number of **remaining
attempts** - The **difficulty level** (larger ranges are harder and give
more points)

### Difficulty Multipliers

  Difficulty   Range    Multiplier
  ------------ -------- ------------
  Easy         1--20    ×1
  Medium       1--50    ×2
  Hard         1--100   ×3

### Final Score Formula

    score = 100 + (remaining_attempts × 10 × difficulty_multiplier)

The highest score achieved is stored locally and shown as the **Best
Score**.
