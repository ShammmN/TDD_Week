import pytest
from health import take_damage, is_alive, heal


@pytest.fixture
def player():
    return {
        "health": 100,
        "max_health": 100,
        "alive": True,
    }


def test_take_damage_reduces_health(player):
    result = take_damage(player, 30)
    assert result["health"] == 70


def test_heal_adds_health(player):
    result = heal(player, 30)
    assert result["health"] == 100


def test_is_alive_false(player):
    result = take_damage(player, 100)
    assert is_alive(result) is False
