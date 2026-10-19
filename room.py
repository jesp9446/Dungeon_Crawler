import random

opposite = {"north":"south",
          "east":"west",
          "south":"north",
          "west":"east"
          }

class room:
    def __init__(self,point , open_door=None):

        self.exits = {"north":False,
                    "east":False,
                    "south":False,
                    "west":False
                    }

        self.point = point

        self.starting_exits(open_door)

    def starting_exits(self, open_door):

        directions = ["north","south","east","west"]
        random_int = random.randint(1,100)

        if open_door is not None:
            directions.remove(open_door)
            if random_int <= 80:
                self.exits[open_door] = True
                self.exits[opposite[open_door]] = True
                amount_of_exits = 0
            elif random_int <= 90:
                amount_of_exits = 2
                chosen_exits = random.sample(directions,amount_of_exits)

                self.exits = {direction: direction in chosen_exits for direction in directions}
                self.exits[open_door] = True
            else:
                amount_of_exits = 3

                chosen_exits = random.sample(directions,amount_of_exits)

                self.exits = {direction: direction in chosen_exits for direction in directions}
                self.exits[open_door] = True

        else:
            if random_int <= 40:
                amount_of_exits = 2
            else:
                amount_of_exits = 3

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

