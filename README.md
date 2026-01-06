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
