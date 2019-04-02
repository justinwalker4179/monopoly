import random

class Monopoly:
    def __init__(self):
        pass

    def start(self):
        pass

    def check_win(self):
        pass

    def take_turn(self):
        pass
    def roll_and_move(self):
        pass
    
    def buy_property(self):
        pass
    def auction_property(self):
        pass

    def go_to_jail(self):
        pass

    def draw_chance_card(self):
        pass
    def draw_community_card(self):
        pass

game_board = [
    [ [],[],[],[],[],[],[],[],[],[],[] ],
    [ [],                           [] ],
    [ [],                           [] ],
    [ [],                           [] ],
    [ [],                           [] ],
    [ [],                           [] ],
    [ [],                           [] ],
    [ [],                           [] ],
    [ [],                           [] ],
    [ [],                           [] ],
    [ [],[],[],[],[],[],[],[],[],[],[] ]
]

chance_deck =
    [
        ["You have been elected chairman of the board, pay each player $50"],
        ["Take a ride on the reading, if you pass GO collect $200"],
        ["Take a walk on the board walk, advance token to board walk"],
        ["Advance to go, collect $200"],
        ["Advance token to the nearest Railroad and pay owner Twice the Rental owed. If Railroad is unowned, you may buy it from the bank"],
        ["Advance token to the nearest Railroad and pay owner Twice the Rental owed. If Railroad is unowned, you may buy it from the bank"],
        ["Get out of jail free. This card may be kept until needed or sold"],
        ["Go directly to jail. Do not pass Go, do not collect $200"],
        ["Bank pays you dividend of $50"],
        ["Advance to Illinois Ave"],
        ["Pay poor tax of $15"],
        ["Make general repairs on all your property. For each house pay $25, for each hotel $100"],
        ["Advance to St. Charles Place. If you pass Go, collect $200"],
        ["Your building and loan matures. Collect $150"],
        ["Advance token to nearest utility. If Unowned you may buy it from the bank. If owned throw dice and pay owner ten times the amount thrown"],
        ["Go back 3 spaces"]
    ]

community_deck =
    [
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]