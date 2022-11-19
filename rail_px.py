funt_name = "rail_px"
out = open(f"{funt_name}.mcfunction", "a")

# function rail_px
# fill ~2 ~2 ~-2 ~128 ~-2 ~2 minecraft:glass
# fill ~2 ~1 ~-1 ~128 ~-1 ~1 minecraft:air
# fill ~2 ~-1 ~ ~128 ~-1 ~ minecraft:blue_ice

# setblock ~2 ~-1 ~1 minecraft:torch
# setblock ~2 ~-1 ~-1 minecraft:torch

tunnle_length = 128
tunnle_width = 5
tw = tunnle_width//2

out.write(f"fill ~2 ~{tw} ~-{tw} ~{tunnle_length} ~-{tw} ~{tw} minecraft:glass\n")
out.write(f"fill ~2 ~{tw - 1} ~-{tw - 1} ~{tunnle_length} ~-{tw - 1} ~{tw - 1} minecraft:air\n")
out.write(f"fill ~2 ~-1 ~ ~{tunnle_length} ~-1 ~ minecraft:blue_ice\n")

depth = 2
torch_space = 8
while depth <= tunnle_length:
    out.write(f"setblock ~{depth} ~-1 ~1 minecraft:torch\n")
    out.write(f"setblock ~{depth} ~-1 ~-1 minecraft:torch\n")
    depth += torch_space

out.close()