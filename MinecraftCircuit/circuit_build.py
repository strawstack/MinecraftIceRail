from PIL import Image

im = Image.open(r"img/wires.png")
px_wires = im.load()
filter_wires = lambda x: x[0] == 255

im = Image.open(r"img/first_stone.png")
px_first_stone = im.load()
filter_first_stone = lambda x: x[3] == 255

im = Image.open(r"img/second_stone.png")
px_second_stone = im.load()
filter_second_stone = lambda x: x[0] != 0

im = Image.open(r"img/gates.png")
px_gates = im.load()
filter_gates = lambda x: x[0] == 255

width, height = im.size 

# px_wires
px_wires_list = []
for row in range(height):
    for col in range(width):
        if filter_wires(px_wires[col, row]):
            px_wires_list.append((col, row))

# px_first_stone
px_first_stone_list = []
for row in range(height):
    for col in range(width):
        if filter_first_stone(px_first_stone[col, row]):
            px_first_stone_list.append((col, row))

# px_second_stone
px_second_stone_list = []
for row in range(height):
    for col in range(width):
        if filter_second_stone(px_second_stone[col, row]):
            px_second_stone_list.append((col, row))

# gates
gates_list = []
for row in range(height):
    for col in range(width):
        if filter_gates(px_gates[col, row]):
            gates_list.append((col, row))

def inside(p, region):
    col, row = p
    r_col, r_row, chunk = region
    c1 = col >= r_col and col < r_col + chunk
    c2 = row >= r_row and row < r_row + chunk
    return c1 and c2

files = []

chunk = 120
os = {"x": 75, "y": 64, "z": 116}
for row in range(0 + os["x"], height + os["x"], chunk):
    for col in range(0 + os["z"], width + os["z"], chunk):
        
        osx = os["x"]
        osz = os["z"]
        fid = f"{(col - osz) // chunk}_{(row - osx) // chunk}"
        out = open(f"circuit_out/circuit_build_{fid}.mcfunction", "a")
        files.append(out)

        start_height = row
        end_height = row + chunk - 1

        start_width = col
        end_width = col + chunk - 1

        #print(start_height, end_height)
        #print(start_width, end_width)
        #print("")

        # Platform
        osy = os["y"]
        for h in range(0, 70, 2):
            out.write(f"fill -{start_height} {osy + h} {start_width} -{end_height} {osy + h + 1} {end_width} minecraft:air\n")
        out.write(f"fill -{start_height} {osy - 1} {start_width} -{end_height} {osy - 1} {end_width} minecraft:stone\n")

        for (p_col, p_row) in filter(lambda x: inside(x, (col - os["z"], row - os["x"], chunk)), px_wires_list):
            out.write(f"setblock -{p_row + osx} {osy} {p_col + osz} minecraft:redstone_wire\n")

        for (p_col, p_row) in filter(lambda x: inside(x, (col - os["z"], row - os["x"], chunk)), px_first_stone_list):
            out.write(f"setblock -{p_row + osx} {osy} {p_col + osz} minecraft:stone\n")
            out.write(f"setblock -{p_row + osx} {osy + 1} {p_col + osz} minecraft:redstone_wire\n")

        for (p_col, p_row) in filter(lambda x: inside(x, (col - os["z"], row - os["x"], chunk)), px_second_stone_list):
            out.write(f"setblock -{p_row + osx} {osy + 1} {p_col + osz} minecraft:stone\n")
            out.write(f"setblock -{p_row + osx} {osy + 2} {p_col + osz} minecraft:redstone_wire\n")

        for (p_col, p_row) in filter(lambda x: inside(x, (col - os["z"], row - os["x"], chunk)), gates_list):
            out.write(f"setblock -{p_row + osx} {osy} {p_col + osz} minecraft:redstone_block\n")

for f in files:
    f.close()