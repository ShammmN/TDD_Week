import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score

def test_add_points_rejects_negative(game):
    with pytest.raises(ValueError):
        add_points(game, -5)

def test_apply_multiplier(game):
   with pytest.raises(ValueError):
       apply_multiplier(game, -5)

def reset_score(game):
    game["score"] = 0
    game["multiplier"] = 1
    return game


def test_is_high_score():
    pass