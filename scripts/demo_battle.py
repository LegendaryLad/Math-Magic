#!/usr/bin/env python
"""Run a demo Math&Magic battle from the command line."""
import argparse

from math_magic.combat import CombatEngine


def main() -> None:
    """Parse CLI arguments and run a demo battle."""
    parser = argparse.ArgumentParser(description="Demo Math&Magic battle.")
    parser.add_argument("topic", help="e.g. Fractions")
    parser.add_argument("level", type=int, help="1-10")
    args = parser.parse_args()

    engine = CombatEngine(topic=args.topic, level=args.level)
    engine.run_battle()


if __name__ == "__main__":
    main()
