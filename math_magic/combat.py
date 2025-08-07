"""Simple combat engine for Math&Magic battles."""

import time
from dataclasses import dataclass

from .monsters import create_monster
from .problems import Problem, generate_problem

BASE_PLAYER_HP = 50


@dataclass
class CombatResult:
    """Outcome container for a battle."""
    winner: str
    turns: int


class CombatEngine:
    """Handles a text-based Math&Magic battle."""

    def __init__(
        self,
        topic: str,
        level: int,
        num_problems: int = 5,
    ) -> None:
        """Initialize the combat engine.

        Parameters
        ----------
        topic:
            The math topic used for problem generation.
        level:
            Difficulty level of the encounter.
        num_problems:
            Number of problems (turns) in the battle.
        """
        self.topic = topic
        self.level = level
        self.num_problems = num_problems
        self.player_hp = BASE_PLAYER_HP
        self.monster = create_monster(topic, level)

    # ---------- private helpers ----------
    def _time_allowed(self) -> int:
        """Return allowed time per problem in seconds."""
        return max(15 - self.level, 4)

    def _damage(self) -> int:
        """Compute damage dealt for each hit."""
        return 10 + self.level

    # ---------- public API ----------
    def run_battle(self, input_func=input, print_func=print) -> CombatResult:
        """Run the battle loop.

        Parameters
        ----------
        input_func:
            Function used to gather user input.
        print_func:
            Function used to output messages.

        Returns
        -------
        CombatResult
            Result object indicating winner and number of turns.
        """
        print_func(f"\n⚔️  Encounter: {self.monster.name}  (HP {self.monster.hp})")
        print_func(self.monster.flavor)
        turns = 0

        for i in range(1, self.num_problems + 1):
            turns += 1
            prob: Problem = generate_problem(self.topic, self.level)
            allowed = self._time_allowed()
            print_func(f"\nProblem {i}/{self.num_problems}  (⏱  {allowed}s)")
            print_func(f"{prob.question} ")

            start = time.time()
            ans = input_func().strip()
            elapsed = time.time() - start

            if elapsed > allowed or ans != prob.answer:
                dmg = self._damage()
                self.player_hp -= dmg
                print_func(f"❌  Wrong or too slow! You take {dmg} dmg → HP {self.player_hp}")
            else:
                dmg = self._damage()
                self.monster.hp -= dmg
                print_func(f"✅  Hit! {dmg} dmg dealt → Monster HP {self.monster.hp}")

            if self.player_hp <= 0 or self.monster.hp <= 0:
                break

        winner = "Player" if self.monster.hp <= 0 else "Monster"
        print_func(f"\n🏁  {winner} wins in {turns} turns!")
        return CombatResult(winner, turns)
