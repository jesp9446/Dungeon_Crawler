from map import map
from room import room

play_map = map(5,5)
cell_start = play_map.create_random_start_room()
play_map.create_adjacent_rooms(cell_start)

play_map.paint_grid()
print(cell_start.get_point().get_coords())

'''
play_map.get_cell(cell_start[0],cell_start[1]).exits_on_edge_map(cell_start,play_map)

play_map.create_adjacent_room(cell_start)

play_map.paint_grid()
print(cell_start)

'''
