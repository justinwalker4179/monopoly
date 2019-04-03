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


chance_deck = {
        1:"You have been elected chairman of the board, pay each player $50",
        2:"Take a ride on the reading, if you pass GO collect $200",
        3:"Take a walk on the board walk, advance token to board walk",
        4:"Advance to go, collect $200",
        5:"Advance token to the nearest Railroad and pay owner Twice the " +
         " Rental owed. If Railroad is unowned you may buy it from the bank",
        6:"Advance token to the nearest Railroad and pay owner Twice the" +
         " Rental owed. If Railroad is unowned you may buy it from the bank",
        7:"Get out of jail free. This card may be kept until needed or sold",
        8:"Go directly to jail. Do not pass Go, do not collect $200",
        9:"Bank pays you dividend of $50",
        10:"Advance to Illinois Ave",
        11:"Pay poor tax of $15",
        12:"Make general repairs on all your property. For each house pay " +
         "$25, for each hotel $100",
        13:"Advance to St. Charles Place. If you pass Go, collect $200",
        14:"Your building and loan matures. Collect $150",
        15:"Advance token to nearest utility. If Unowned you may buy it " +
         "from the bank. If owned throw dice and pay owner ten times the " +
         "amount thrown",
        16:"Go back 3 spaces"
    }

community_deck = {
        1:"Get out of jail free. This card may be kept until needed or sold",
        2:"From sale of stock, you get $45",
        3:"Grand opera opening." + 
         "Collect $50 from every player for opening night seats",
        4:"Advance to Go, collect $200",
        5:"Xmas fund matures, collect $100",
        6:"Go directly to jail. Do not pass Go. Do not collect $200",
        7:"Life insurance matures, collect $200",
        8:"You are assessed for street repairs. $40 per house," +
         "$115 per hotel",
        9:"Pay hospital $100",
        10:"Income tax refund, collect $20",
        11:"Doctor's fee, pay $50",
        12:"You inherit $100",
        13:"Pay school tax of $150",
        14:"Receive for services $25",
        15:"Bank error in your favor, collect $200",
        16:"You have won second prize in a beauty contest, collect $10"
    }

class board_space:
    def __init__(self, name, info):
        self.category = category
        self.name = name
        self.info = info

class property:
    def __init__(self,color, price, 
                 rent, one_house_rent, two_house_rent,
                 three_house_rent, four_house_rent, hotel_rent,
                 house_cost, hotel_cost):
        self.color = color
        self.price = price
        self.rents = {one_house:one_house_rent,
                      two_house:two_house_rent,
                      three_house:three_house_rent,
                      four_house:four_house_rent,
                      hotel:hotel_rent}
        self.costs = {house:house_cost,
                      hotel:hotel_cost}

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