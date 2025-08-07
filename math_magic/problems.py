"""Sample math problems for use in battles."""

import random
from dataclasses import dataclass

@dataclass
class Problem:
    """Simple math problem container."""

    question: str
    answer: str  # always a **string** for simple equality check


_DIFFICULTY_LADDER = {
    1: [Problem("1/2 + 1/4 =", "0.75")],
    5: [Problem("Simplify 7/12 ÷ 14/18", "3/2")],
    10: [Problem("Convert 2 5/8 to a decimal", "2.625")],
}


def generate_problem(topic: str, level: int) -> Problem:
    """Generate a stub math problem based on level."""

    ladder = _DIFFICULTY_LADDER
    closest = max(k for k in ladder if k <= level)
    return random.choice(ladder[closest])
