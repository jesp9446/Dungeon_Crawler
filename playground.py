import random



exits = {"north":random.choice([True,False]),
        "east" :random.choice([True,False]),
        "south":random.choice([True,False]),
        "west" :random.choice([True,False])
        }


directions = ["north","south","east","west"]

random_int = random.randint(1,100)
if random_int <= 10:
    amount_of_exits = 1
elif random_int <= 60:
    amount_of_exits = 2
elif random_int <= 90:
    amount_of_exits = 3
else:
    amount_of_exits = 4

chosen_exits = random.sample(directions,amount_of_exits)

exits = {direction: direction in chosen_exits for direction in directions}

print(amount_of_exits)
print(chosen_exits)





'''
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
                            
'''
