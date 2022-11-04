# Write your code here


class Block:
    list_of_all_blocks = []

    def __init__(self, name, shape, coordinates=None):
        if coordinates is None:
            coordinates = [0, 0]

        self.name = name
        self.shape = shape
        self.rotation = 0
        self.coordinates = coordinates

    # block move [0, 0]
    def


    #block rotate



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

        for i in range(1, x):
            self.GRID[0].append("-")

        row = self.GRID[0]
        for i in range(1, y):
            self.GRID.append(row)

    @classmethod
    def to_string(cls, block=None):
        string_grid = ""
        location = [0, 0]
        for row in cls.GRID:
            row_to_print = ""
            for i in row:
                if block is not None:
                    point_locations = []
                    for point in block.shape[block.rotation]:
                        x = point[0] + block.coordinates[0]
                        y = point[1] + block.coordinates[1]
                        point_locations.append([x, y])
                    if location in point_locations:
                        row_to_print += "0 "
                    else:
                        row_to_print += i + " "
                else:
                    row_to_print += i + " "
                location[1] += 1
            string_grid += row_to_print + "\n"
            location[0] += 1
            location[1] = 0

        return string_grid


def block_creator():
    # shape[0] is rotation
    # shape[1] is shape
    # shape[2] is location of individual points

    o_block = Block("O", [[[0, 4], [1, 4], [1, 5], [0, 5]]])

    i_block = Block("I", [[[0, 4], [1, 4], [2, 4], [3, 4]],
                          [[0, 3], [0, 4], [0, 5], [0, 6]]])

    s_block = Block("S", [[[0, 5], [0, 4], [1, 4], [1, 3]],
                          [[0, 4], [1, 4], [1, 5], [2, 5]]])

    z_block = Block("Z", [[[0, 4], [0, 5], [1, 5], [1, 6]],
                          [[0, 5], [1, 5], [1, 4], [2, 4]]])

    l_block = Block("L", [[[0, 4], [1, 4], [2, 4], [2, 5]],
                          [[0, 5], [1, 5], [1, 4], [1, 3]],
                          [[0, 4], [0, 5], [1, 5], [2,5]],
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
    block = Block.block_finder(block_to_print)

    grid_size = input().split()
    grid = Grid(int(grid_size[0]), int(grid_size[1]))

    print(grid.to_string())

    # for rotation in block.shape:
        # print(Grid.to_string(rotation))

    print(grid.to_string(block))


if __name__ == "__main__":
    main()
