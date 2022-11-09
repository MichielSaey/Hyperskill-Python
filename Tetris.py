from collections import deque
import copy

class Block:
    list_of_all_blocks = []

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
    def move(self, x, y, dimensions):
        if not self.bottom_reached:
            # rotation = self.shape[self.rotation]
            new_shape = []
            for rotation in self.shape:
                old_rotation = copy.deepcopy(rotation)
                # move
                for point in rotation:
                    point[1] += x
                    point[0] += y

                # after all are moved check is correct:
                position_correct = True
                for point in rotation:
                    # y
                    if not 0 <= point[0] <= int(dimensions[1]) - 1:
                        position_correct = False
                    # x
                    if not 0 <= point[1] <= int(dimensions[0]) - 1:
                        position_correct = False

                if position_correct is False:
                    new_shape.append(old_rotation)
                else:
                    new_shape.append(rotation)

            self.shape = new_shape
            rotation = self.shape[self.rotation]
            for point in rotation:
                if point[0] == int(dimensions[1]) - 1:
                    self.bottom_reached = True


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

    @classmethod
    def block_finder(cls, block_to_print):
        for block in Block.list_of_all_blocks:
            if block.name == block_to_print:
                return block


class Grid:
    GRID = [
        ["-"],
    ]

    def __init__(self, x=None, y=None):
        if x is None:
            x = 10
        if y is None:
            y = 20

        self.dimensions = [x, y]
        for i in range(1, x):
            self.GRID[0].append("-")

        row = self.GRID[0]
        for i in range(1, y):
            self.GRID.append(row)
        self.blocks_in_grid = deque()

    def to_string(self):
        # array of all points on screen
        points = []
        for block in self.blocks_in_grid:
            rotation = block.shape[block.rotation]
            for point in rotation:
                points.append(point)

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


def block_creator():
    # shape[0] is rotation
    # shape[0][0] is shape
    # shape[0][0][0] is location of individual points

    o_block = Block("O", [[[0, 4], [1, 4], [1, 5], [0, 5]]])

    i_block = Block("I", [[[0, 4], [1, 4], [2, 4], [3, 4]],
                          [[0, 3], [0, 4], [0, 5], [0, 6]]])

    s_block = Block("S", [[[0, 5], [0, 4], [1, 4], [1, 3]],
                          [[0, 4], [1, 4], [1, 5], [2, 5]]])

    z_block = Block("Z", [[[0, 4], [0, 5], [1, 5], [1, 6]],
                          [[0, 5], [1, 5], [1, 4], [2, 4]]])

    l_block = Block("L", [[[0, 4], [1, 4], [2, 4], [2, 5]],
                          [[0, 5], [1, 5], [1, 4], [1, 3]],
                          [[0, 4], [0, 5], [1, 5], [2, 5]],
                          [[0, 6], [0, 5], [0, 4], [1, 4]]])

    j_block = Block("J", [[[0, 5], [1, 5], [2, 5], [2, 4]],
                          [[1, 5], [0, 5], [0, 4], [0, 3]],
                          [[0, 5], [0, 4], [1, 4], [2, 4]],
                          [[0, 4], [1, 4], [1, 5], [1, 6]]])

    t_block = Block("T", [[[0, 4], [1, 4], [2, 4], [1, 5]],
                          [[0, 4], [1, 3], [1, 4], [1, 5]],
                          [[0, 5], [1, 5], [2, 5], [1, 4]],
                          [[0, 4], [0, 5], [0, 6], [1, 5]]])

    Block.list_of_all_blocks.extend([o_block, i_block, s_block, z_block, l_block, j_block, t_block])


def main():
    block_creator()

    block_to_print = input()
    grid_size = input().split()

    block = Block.block_finder(block_to_print)
    grid = Grid(int(grid_size[0]), int(grid_size[1]))

    print(grid.to_string())
    grid.blocks_in_grid.append(block)

    print("")
    print(grid.to_string())

    # for rotation in block.shape:
    # print(Grid.to_string(rotation))

    while True:
        control = input()
        print("")
        if control == "rotate":
            block.rotate()
        elif control == "left":
            block.move(-1, 0, grid_size)
        elif control == "right":
            block.move(1, 0, grid_size)
        elif control == "exit":
            break

        block.move(0, 1, grid_size)
        print(grid.to_string())


if __name__ == "__main__":
    main()
