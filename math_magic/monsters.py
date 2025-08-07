"""Placeholder monster data for Math&Magic battles."""

from dataclasses import dataclass

BASE_HP = 50


@dataclass
class Monster:
    """Lightweight monster placeholder."""

    name: str
    hp: int
    flavor: str = "A placeholder foe awaiting real artwork."


def create_monster(topic: str, level: int) -> Monster:
    """Create a deterministic placeholder monster.

    Parameters
    ----------
    topic:
        Descriptive theme for the monster.
    level:
        Difficulty level of the encounter.

    Returns
    -------
    Monster
        Generated monster instance.
    """

    return Monster(
        name=f"Generic {topic} Beast • Lvl {level}",
        hp=BASE_HP + level * 5,
        flavor=f"This monster embodies the theme '{topic}'.",
    )
