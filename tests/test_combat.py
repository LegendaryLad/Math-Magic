"""Tests for the Math&Magic combat engine."""
from math_magic.combat import CombatEngine, CombatResult


def test_player_can_win(monkeypatch):
    """Player should defeat level-1 monster if all answers are correct."""
    inputs = iter(["0.75"] * 5)
    monkeypatch.setattr("builtins.input", lambda: next(inputs))
    engine = CombatEngine(topic="Fractions", level=1)
    result: CombatResult = engine.run_battle(
        input_func=lambda: next(inputs, "0.75"), print_func=lambda *_: None
    )
    assert result.winner == "Player"
