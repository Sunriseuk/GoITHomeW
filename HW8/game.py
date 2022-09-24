# Generate game map
from random import randint

size_n = 10
size_m = 10


def generate_map(n, m):

    game_map = []
    for _ in range(n):
        row = [' ' for _ in range(m)]
        game_map.append(row)

    return game_map


def print_map(game_map):
    for row in game_map:
        print(f"|{'|'.join(row)}|")


# Generate game world
def generate_world(game_map):
    # X - character
    # O - gold
    # & - monster
    # _ - trap
    objs = {'X': 1, 'O': 2, '&': 2, '_': 2}
    size_n, size_m = len(game_map), len(game_map[0])
    rnd_cells = []

    for obj, n in objs.items():
        for i in range(n):
            rnd_cell = randint(0, size_n - 1), randint(0, size_m - 1)
            if rnd_cell not in rnd_cells:  # проверка на одну и ту же ячейку размещения
                rnd_cells.append(rnd_cell)
            else:
                rnd_cell = randint(size_n), randint(size_m)
                rnd_cells.append(rnd_cell)

            game_map[rnd_cell[0]][rnd_cell[1]] = obj
    return game_map


game_map = generate_map(size_n, size_m)
game_world = generate_world(game_map)
print_map(game_world)
