import random
from room import room
from position import point

offset = {"north":(0,-1,"south"),
          "east":(1,0,"west"),
          "south":(0,1,"north"),
          "west":(-1,0,"east")
          }

class map:
    def __init__(self, rows, coloms):
        self.rows = rows
        self.coloms = coloms
        self.grid = [[" "] * coloms for _ in range(rows)]

    def get_rows(self):
        return self.rows

    def get_coloms(self):
        return self.coloms

    def get_grid(self):
        return self.grid

    def paint_grid(self):
        for row in range(len(self.grid)):
            temp_row = []
            for cell in range(len(self.grid[row])):
                if isinstance(self.get_cell(point(cell,row)),room):
                    temp_row.append("R")
                else:
                    temp_row.append(" ")
            print(temp_row)

    def get_cell(self, position:point):
        return self.grid[position.get_y()][position.get_x()]

    def set_cell(self, position:point ,value):
        self.grid[position.get_y()][position.get_x()] = value

    def is_cell_empty(self, position:point):
        return self.get_cell(position) == " "
  
    def create_random_start_room(self):
        if random.choice([True,False]):
            randrange_col = random.randrange(self.coloms)

            if random.choice([True,False]):
                return self.create_room(point(randrange_col, 0))
            
            else:
                return self.create_room(point(randrange_col, self.rows - 1))

        else:
            randrange_row = random.randrange(self.rows)

            if random.choice([True,False]):
                return self.create_room(point(0, randrange_row))
            
            else:
                return self.create_room(point(self.coloms - 1, randrange_row))

    def create_room(self, position, door_open=None):
        new_room = room(point(position.get_x(),position.get_y()))
        if door_open is not None:
            new_room.set_exits(door_open,True)
        self.set_cell(new_room.get_point(),new_room)
        return new_room

    def valid_room_position(self, position):
        if (position.get_y() < self.rows and position.get_y() >= 0) and (position.get_x() < self.coloms and position.get_x() >= 0):
            return self.is_cell_empty(position)
        return False

        
    def create_adjacent_rooms(self, room:room , counter=0):
        if not counter >= 5:
            return
        else:
            room_exits = room.get_exits()
            room_exits_keys = list(room_exits.keys())
            for key in room_exits_keys:
                if room_exits[key]:
                    new_room_point = point(room.get_point().get_x() + offset[key][0],room.get_point().get_y() + offset[key][1])
                    if self.valid_room_position(new_room_point):
                        new_room = self.create_room(new_room_point, offset[key][2])
                        self.create_adjacent_rooms(new_room, counter + 1)
