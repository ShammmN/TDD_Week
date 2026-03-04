{
    "score":      0,      # current score, always >= 0
    "multiplier": 1,      # score multiplier, always >= 1
    "active":     True   # whether the game is currently active
}
def add_points(game, amount):
    game["score"] += amount * game["multiplier"]
    if game["score"] < 0:
        raise ValueError("The score can not be negative")

def apply_multiplier(game, multiplier):
    pass

def reset_score(game):
    pass

def is_high_score(game, threshold):
    pass