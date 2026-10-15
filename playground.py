import random

exits = {"north":random.choice([True,False]),
        "east" :random.choice([True,False]),
        "south":random.choice([True,False]),
        "west" :random.choice([True,False])
        }

print(list(exits.keys()))



'''
def create_adjacent_room(self, coords):
    exits = self.get_cell(coords[0],coords[1]).get_exits()
    if exits["north"]:
        new_coords = (coords[0],coords[1] - 1)
        self.set_cell(new_coords[0],new_coords[1], room().set_south(True))
        #self.create_adjacent_room(new_coords)
    if exits["east"]:
        new_coords = (coords[0] + 1,coords[1])
        self.set_cell(new_coords[0],new_coords[1], room().set_west(True))
        #self.create_adjacent_room(new_coords)
    if exits["south"]:
        new_coords = (coords[0], coords[1] + 1)
        self.set_cell(new_coords[0],new_coords[1], room().set_north(True))
        #self.create_adjacent_room(new_coords)
    if exits["west"]:
        new_coords = (coords[0] - 1, coords[1])
        self.set_cell(new_coords[0],new_coords[1], room().set_east(True))
        #self.create_adjacent_room(new_coords)



        
def create_adjacent_rooms(self, room:room , counter=0):
    if counter < 5:
        room_exits = room.get_exits()
        room_exits_keys = list(room_exits.keys())
        for key in room_exits_keys:
            if room_exits[key]:
                match key:
                    case "north":
                        new_room_point = point(room.get_point().get_x(),room.get_point().get_y() - 1)
                        if self.valid_room_position(new_room_point):
                            new_room = self.create_room(new_room_point, "south")
                            self.create_adjacent_rooms(new_room, counter + 1)
                    case "east":
                        new_room_point = point(room.get_point().get_x() + 1,room.get_point().get_y())
                        if self.valid_room_position(new_room_point):
                            new_room = self.create_room(new_room_point, "west")
                            self.create_adjacent_rooms(new_room, counter + 1)
                    case "south":
                        new_room_point = point(room.get_point().get_x(),room.get_point().get_y() + 1)
                        if self.valid_room_position(new_room_point):
                            new_room = self.create_room(new_room_point, "north")
                            self.create_adjacent_rooms(new_room, counter + 1)
                    case "west":
                        new_room_point = point(room.get_point().get_x() - 1,room.get_point().get_y())
                        if self.valid_room_position(new_room_point):
                            new_room = self.create_room(new_room_point, "east")
                            self.create_adjacent_rooms(new_room, counter + 1)
'''
