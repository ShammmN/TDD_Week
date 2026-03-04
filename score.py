{
    "score":      0,      # current score, always >= 0
    "multiplier": 1,      # score multiplier, always >= 1
    "active":     True   # whether the game is currently active
}
def add_points(game, amount):
    if game["active"] == False:
        return game
    game["score"] += amount * game["multiplier"]
    if game["score"] < 0:
        raise ValueError("The score can not be negative")
    return game 

def apply_multiplier(game, multiplier):
    if game["active"] == False:
        return game
    game["multiplier"] = multiplier
    if game["multiplier"] < 1:
        raise ValueError("The multiplier must be eqaul to or greater than 1")
    return game

def reset_score(game):
    pass

def is_high_score(game, threshold):
    pass