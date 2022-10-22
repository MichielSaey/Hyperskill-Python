# Write your code here


class Block:
    list_of_all_blocks = []

    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates

    @classmethod
    def block_finder(cls, block_to_print):
        for block in Block.list_of_all_blocks:
            if block.name == block_to_print:
                return block


class Grid:
    GRID = [
        ["-", "-", "-", "-"],
        ["-", "-", "-", "-"],
        ["-", "-", "-", "-"],
        ["-", "-", "-", "-"]
    ]

    # def __init__(self):

    @classmethod
    def to_string(cls, coordinates = []):
        string_grid = ""
        count = 0
        for row in cls.GRID:
            row_to_print = ""
            for i in row:
                if count in coordinates:
                    row_to_print += "0 "
                else:
                    row_to_print += i + " "
                count += 1
            string_grid += row_to_print + "\n"

        return string_grid


def block_creator():
    o_block = Block("O", [[5, 6, 9, 10], [5, 6, 9, 10], [5, 6, 9, 10], [5, 6, 9, 10]])
    i_block = Block("I", [[1, 5, 9, 13], [4, 5, 6, 7], [1, 5, 9, 13], [4, 5, 6, 7]])
    s_block = Block("S", [[6, 5, 9, 8], [5, 9, 10, 14], [6, 5, 9, 8], [5, 9, 10, 14]])
    z_block = Block("Z", [[4, 5, 9, 10], [2, 5, 6, 9], [4, 5, 9, 10], [2, 5, 6, 9]])
    l_block = Block("L", [[1, 5, 9, 10], [2, 4, 5, 6], [1, 2, 6, 10], [4, 5, 6, 8]])
    j_block = Block("J", [[2, 6, 9, 10], [4, 5, 6, 10], [1, 2, 5, 9], [0, 4, 5, 6]])
    t_block = Block("T", [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]])
    Block.list_of_all_blocks.extend([o_block, i_block, s_block, z_block, l_block, j_block, t_block])


def main():
    block_creator()

    block_to_print = input()
    block = Block.block_finder(block_to_print)

    print(Grid.to_string())

    for rotation in block.coordinates:
        print(Grid.to_string(rotation))

    print(Grid.to_string(block.coordinates[0]))

if __name__ == "__main__":
    main()
