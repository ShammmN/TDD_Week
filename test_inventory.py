import pytest
from inventory import add_item, remove_item, get_item_count


def test_add_item_locked():
    inventory = {"items": ["apples", "oranges", "chicken"],
                 "capacity": 10,
                 "locked": True}
    result = add_item(inventory, "beef")
    assert result["items"] == ["apples", "oranges", "chicken"]


def test_add_item_empty_str():
    inventory = {"items": ["apples", "oranges", "chicken"],
                 "capacity": 10,
                 "locked": False}
    with pytest.raises(ValueError):
        add_item(inventory, "")


def test_add_item_valid():
    inventory = {"items": ["apples", "oranges", "chicken"],
                 "capacity": 10,
                 "locked": False}
    result = add_item(inventory, "beef")
    assert result["items"] == ["apples", "oranges", "chicken", "beef"]


def test_add_item_capacity():
    inventory = {"items": ["apples", "oranges", "chicken"],
                 "capacity": 3,
                 "locked": False}
    with pytest.raises(ValueError):
        add_item(inventory, "beef")


def test_remove_item_locked():
    inventory = {"items": ["apples", "oranges", "chicken"],
                 "capacity": 10,
                 "locked": True}
    result = remove_item(inventory, "chicken")
    assert result["items"] == ["apples", "oranges", "chicken"]


def test_remove_item_not_in_inventory():
    inventory = {"items": ["apples", "oranges", "chicken"],
                 "capacity": 10,
                 "locked": False}
    with pytest.raises(ValueError):
        remove_item(inventory, "beef")


def test_remove_item_valid():
    inventory = {"items": ["apples", "oranges", "chicken"],
                 "capacity": 10,
                 "locked": False}
    result = remove_item(inventory, "chicken")
    assert result["items"] == ["apples", "oranges"]


def test_get_item_count_valid():
    inventory = {"items": ["apples", "oranges", "chicken"],
                 "capacity": 10,
                 "locked": False}
    result = get_item_count(inventory)
    assert result == 3


def test_get_item_count_empty():
    inventory = {"items": [],
                 "capacity": 10,
                 "locked": False}
    result = get_item_count(inventory)
    assert result == 0


def test_get_item_count_locked():
    inventory = {"items": ["apples", "oranges", "chicken"],
                 "capacity": 10,
                 "locked": True}
    result = get_item_count(inventory)
    assert result == 3
