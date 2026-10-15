import random

class room:
    def __init__(self,point):

        self.exits = None

        self.point = point

        self.starting_exits()

    def starting_exits(self):
        directions = ["north","south","east","west"]
        random_int = random.randint(1,100)

        if random_int <= 30:
            amount_of_exits = 1
        elif random_int <= 70:
            amount_of_exits = 2
        elif random_int <= 90:
            amount_of_exits = 3
        else:
            amount_of_exits = 4

        chosen_exits = random.sample(directions,amount_of_exits)

        self.exits = {direction: direction in chosen_exits for direction in directions}


    def get_point(self):
        return self.point

    def get_exits(self):
        return self.exits

    def set_exits(self, orientation, bool):
        self.exits[orientation] = bool
    
    def exits_on_edge_map(self, coords, map):
        if coords[1] == 0:
            self.exits["north"] = False
        if coords[0] == 0:
            self.exits["west"] = False
        if coords[1] == map.get_rows() - 1:
            self.exits["south"] = False
        if coords[0] == map.get_coloms() - 1:
            self.exits["east"] = False

