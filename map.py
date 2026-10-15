import random
from room import room
from position import point

offset = {"north":(0,-1),
          "east":(1,0),
          "south":(0,1),
          "west":(-1,0)
          }

opposite = {"north":"south",
          "east":"west",
          "south":"north",
          "west":"east"
          }

class map:
    def __init__(self, rows, coloms):
        self.rows = rows
        self.coloms = coloms
        self.grid = [[" "] * coloms for _ in range(rows)]

        self.room_depth = 5

        self.fill_map()

    def get_rows(self):
        return self.rows

    def get_coloms(self):
        return self.coloms

    def get_grid(self):
        return self.grid

    def paint_grid(self):
        for row in self.grid:
            temp_row = []
            for cell in row:
                if isinstance(cell,room):
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
        side = random.randrange(4)
        if side == 0:
            return self.create_room(point(random.randrange(self.coloms), 0))
        elif side == 1:
            return self.create_room(point(random.randrange(self.coloms), self.rows - 1))
        elif side == 2:
            return self.create_room(point(0, random.randrange(self.rows)))
        else:
            return self.create_room(point(self.coloms - 1, random.randrange(self.rows)))

    def create_room(self, position, door_open=None):
        new_room = room(point(position.get_x(),position.get_y()))
        if door_open is not None:
            new_room.set_exits(door_open,True)
        self.set_cell(new_room.get_point(),new_room)
        return new_room

    def valid_grid_position(self,position):
        return (position.get_y() < self.rows and position.get_y() >= 0) and (position.get_x() < self.coloms and position.get_x() >= 0)

    def valid_room_position(self, position):
        return self.valid_grid_position(position) and self.is_cell_empty(position)

    def close_room_door(self,position,orientation):
        self.get_cell(position).set_exits(orientation,False)
        
    def create_adjacent_rooms(self, room:room , counter=0):
        if counter >= self.room_depth:
            room_exits = room.get_exits()

            for orientation in list(room_exits.keys()):

                if room_exits[orientation]:
                    adjacent_point = point(
                        room.get_point().get_x() + offset[orientation][0],
                        room.get_point().get_y() + offset[orientation][1]
                        )
                    
                    if not self.valid_grid_position(adjacent_point):
                        room.set_exits(orientation,False)

                    elif self.is_cell_empty(adjacent_point):
                        room.set_exits(orientation,False)

                    elif not self.get_cell(adjacent_point).get_exits()[opposite[orientation]]:
                        self.close_room_door(adjacent_point,opposite[orientation])
        else:
            room_exits = room.get_exits()

            for orientation in list(room_exits.keys()):

                if room_exits[orientation]:
                    new_room_point = point(
                        room.get_point().get_x() + offset[orientation][0],
                        room.get_point().get_y() + offset[orientation][1]
                        )
                    
                    if self.valid_room_position(new_room_point):
                        new_room = self.create_room(new_room_point, opposite[orientation])
                        self.create_adjacent_rooms(new_room, counter + 1)

                    elif self.valid_grid_position(new_room_point):
                        self.close_room_door(new_room_point,opposite[orientation])

    def fill_map(self):
        self.create_adjacent_rooms(self.create_random_start_room())


