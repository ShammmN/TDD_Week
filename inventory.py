{
    "items": [],          # list of item name strings
    "capacity": 10,       # maximum number of items allowed
    "locked": False       # if True, inventory cannot be modified
}


def add_item(inventory, item):
    if inventory["locked"]:
        return inventory
    if item == "":
        raise ValueError("The item can not be an empty string!")
    if len(inventory["items"]) >= inventory["capacity"]:
        raise ValueError("The inventory of items is at capacity!")
    inventory["items"].append(item)
    return inventory


def remove_item(inventory, item):
    if inventory["locked"]:
        return inventory
    if item not in inventory["items"]:
        raise ValueError("This item is not in the inventory!")
    inventory["items"].remove(item)
    return inventory


def get_item_count(inventory):
    return len(inventory["items"])
