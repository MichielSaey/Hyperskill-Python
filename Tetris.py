from collections import deque
import copy


class Block:
    def __init__(self, name, shape, coordinates=None):
        if coordinates is None:
            coordinates = [0, 0]

        self.bottom_reached = False
        self.name = name
        self.shape = shape
        self.rotation = 0
        self.coordinates = coordinates

    # block move [0, 0]
    # relative position from current coordinates
    def move(self, x, y, grid):
        dimensions = grid.dimensions
        points = grid.grid_points_list(True)
        if not self.bottom_reached:
            # rotation = self.shape[self.rotation]
            new_shape = []
            for rotation in self.shape:

                # -- horizontal movement --
                new_rotation = copy.deepcopy(rotation)
                old_rotation = []
                # move
                for point in new_rotation:
                    point[1] += x

                # after all are moved check is correct:
                position_correct = True
                for point in new_rotation:
                    # x
                    if not 0 <= point[1] <= int(dimensions[0]) - 1:
                        position_correct = False

                    if point in points:
                        position_correct = False

                if position_correct is False:
                    new_rotation = copy.deepcopy(rotation)
                else:
                    old_rotation = copy.deepcopy(new_rotation)

                # -- vertical movement --
                for point in new_rotation:
                    point[0] += y

                # after all are moved check is correct:
                position_correct = True
                for point in new_rotation:
                    # y
                    if not 0 <= point[0] <= int(dimensions[1]) - 1:
                        position_correct = False

                    if point in points:
                        position_correct = False
                        self.bottom_reached = True

                if position_correct is False:
                    new_shape.append(old_rotation)
                else:
                    new_shape.append(new_rotation)

            self.shape = new_shape
            rotation = self.shape[self.rotation]
            for point in rotation:
                if point[0] == int(dimensions[1]) - 1:
                    self.bottom_reached = True
                if point[0] == 0:
                    raise Exception("Game Over!")

    # block rotate
    # default = 1 (90deg)
    def rotate(self, r=1):
        if not self.bottom_reached:
            r = r % len(self.shape)
            i = self.rotation

            while r > 0:
                if i < len(self.shape):
                    i += 1
                else:
                    i = 0
                r -= 1

            self.rotation = i % len(self.shape)


class Grid:
    GRID = deque()

    def __init__(self, x=None, y=None):
        if x is None:
            x = 10
        if y is None:
            y = 20

        self.dimensions = [x, y]
        self.GRID.append([" -"])
        for i in range(1, x):
            self.GRID[0].append("-")

        row = self.GRID[0]
        for i in range(1, y):
            self.GRID.append(row)
        self.blocks_in_grid = deque()

    def grid_points_list(self, without_last=False):
        points = []
        blocks = list(self.blocks_in_grid)

        if without_last:
            blocks.pop()

        for block in blocks:
            rotation = block.shape[block.rotation]
            for point in rotation:
                points.append(point)

        return points

    def to_string(self):
        # array of all points on screen
        points = self.grid_points_list()
        string_grid = ""
        location = [0, 0]
        for row in self.GRID:
            row_to_print = ""
            for i in row:
                if location in points:
                    row_to_print += "0 "
                else:
                    row_to_print += i + " "
                location[1] += 1
            string_grid += row_to_print.strip() + "\n"
            location[0] += 1
            location[1] = 0

        return string_grid

    def move(self, x, y):
        block = self.blocks_in_grid.pop()
        block.move(x, y)
        self.blocks_in_grid.append(block)

    def line_break(self):
        points = self.grid_points_list()
        location = [0, 0]

        for row in self.GRID:
            row_full = True
            for field in row:
                if location not in points:
                    row_full = False
                else:
                    full_row = location[0]
                location[1] += 1
            location[0] += 1
            location[1] = 0

            if row_full:
                for block in self.blocks_in_grid:
                    block_points = copy.deepcopy(block.shape[block.rotation])
                    for point in block_points:
                        if point[0] == full_row:
                            block.shape[block.rotation].remove(point)
                    for point in block.shape[block.rotation]:
                        point[0] += 1



def block_creator(type):
    # shape[0] is rotation
    # shape[0][0] is shape
    # shape[0][0][0] is location of individual points

    blocks = {
        "O": [[[0, 4], [1, 4], [1, 5], [0, 5]]],

        "I": [[[0, 4], [1, 4], [2, 4], [3, 4]],
              [[0, 3], [0, 4], [0, 5], [0, 6]]],

        "S": [[[0, 5], [0, 4], [1, 4], [1, 3]],
              [[0, 4], [1, 4], [1, 5], [2, 5]]],

        "Z": [[[0, 4], [0, 5], [1, 5], [1, 6]],
              [[0, 5], [1, 5], [1, 4], [2, 4]]],

        "L": [[[0, 4], [1, 4], [2, 4], [2, 5]],
              [[0, 5], [1, 5], [1, 4], [1, 3]],
              [[0, 4], [0, 5], [1, 5], [2, 5]],
              [[0, 6], [0, 5], [0, 4], [1, 4]]],

        "J": [[[0, 5], [1, 5], [2, 5], [2, 4]],
              [[1, 5], [0, 5], [0, 4], [0, 3]],
              [[0, 5], [0, 4], [1, 4], [2, 4]],
              [[0, 4], [1, 4], [1, 5], [1, 6]]],

        "T": [[[0, 4], [1, 4], [2, 4], [1, 5]],
              [[0, 4], [1, 3], [1, 4], [1, 5]],
              [[0, 5], [1, 5], [2, 5], [1, 4]],
              [[0, 4], [0, 5], [0, 6], [1, 5]]],
    }
    return Block(type, blocks.get(type))


def main():
    grid_size = input().split()
    grid = Grid(int(grid_size[0]), int(grid_size[1]))
    print(grid.to_string())

    while True:
        control = input()

        if control == "piece":
            block_to_print = input()
            block = block_creator(block_to_print)
            grid.blocks_in_grid.append(block)
            print(grid.to_string())
            continue

        if block:
            x = 0
            y = 1
            if control == "rotate":
                block.rotate()
            elif control == "left":
                x += -1
            elif control == "right":
                x += 1
            elif control == "break":
                grid.line_break()
            elif control == "exit":
                return

            try:
                block.move(x, y, grid)
            except Exception as e:
                print(grid.to_string())
                print(e)
                break
            print(grid.to_string())
            print("")


if __name__ == "__main__":
    main()
