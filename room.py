import random

class room:
    def __init__(self,point):

        self.exits = {"north":random.choice([True,False]),
                      "east" :random.choice([True,False]),
                      "south":random.choice([True,False]),
                      "west" :random.choice([True,False])
                      }

        self.point = point


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

