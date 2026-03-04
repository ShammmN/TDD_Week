import pytest
from score import add_points, apply_multiplier, reset_score, is_high_score

def test_add_points_valid():
    game = {"score": 90, "multiplier": 2, "active": True}
    result = add_points(game, 5)
    assert result["score"] == 100

def test_add_points_rejects_negative(game):
    with pytest.raises(ValueError):
        add_points(game, -5)

def test_add_points_inactive():
    game = {"score": 90, "multiplier": 2, "active": False}
    result = add_points(game, 5)
    assert result["score"] == 90

def test_apply_multiplier(game):
   with pytest.raises(ValueError):
       apply_multiplier(game, -5)

def test_apply_multiplier_valid():
    game = {"score": 90, "multiplier": 2, "active": True}
    result = apply_multiplier(game, 4)
    assert result["multiplier"] == 4

def test_reset_score():
   game = {"score": 90, "multiplier": 2, "active": False}
   result = reset_score(game)
   assert result["score"] == 0
   assert result["multiplier"] == 1

def test_apply_multiplier_inactive():
    game = {"score":90, "multiplier": 2, "active": False}
    result = apply_multiplier(game, 4)
    assert result["multiplier"] == 2

def test_is_high_score():
    game = {"score": 90, "multiplier": 2, "active": False}
    with pytest.raises(ValueError):
        is_high_score(game , -5)

def test_is_high_score_true():
    game = {"score": 90, "multiplier": 2, "active": True}
    assert is_high_score(game, 45) == True

def test_is_high_score_false_equal():
    game = {"score": 90, "multiplier": 2, "active": True}
    assert is_high_score(game, 90) == False

def test_is_high_score_false_less():
    game = {"score": 90, "multiplier": 2, "active": True}
    assert is_high_score(game, 180) == False
