import math
import random

funt_name = "pit"
out = open(f"{funt_name}.mcfunction", "a")

pit_radius = 64 
num_torches = 300
depth_lookup = {}

# Examples
# fill ~2 ~-1 ~ ~128 ~-1 ~ minecraft:blue_ice
# setblock ~2 ~-1 ~-1 minecraft:torch

for xp in range(-1 * pit_radius, pit_radius + 1):
    for zp in range(-1 * pit_radius, pit_radius + 1):
        
        sq = pow(xp, 2) + pow(zp, 2)
        if math.sqrt( sq ) <= pit_radius:

            depth = math.floor(
                math.sqrt(
                    pow(pit_radius, 2) - sq
                )
            )

            depth_lookup[(xp, zp)] = depth

            out.write(f"fill ~{xp} ~{10} ~{zp} ~{xp} ~-{depth} ~{zp} minecraft:air\n")
            out.write(f"fill ~{xp} ~-{depth + 4} ~{zp} ~{xp} ~-{depth + 4} ~{zp} minecraft:dirt\n")
            out.write(f"fill ~{xp} ~-{depth + 1} ~{zp} ~{xp} ~-{depth + 3} ~{zp} minecraft:sand\n")

for i in range(num_torches):
    xp = random.randint(-1 * pit_radius, pit_radius)
    zp = random.randint(-1 * pit_radius, pit_radius)
    if (xp, zp) in depth_lookup:
        depth = depth_lookup[(xp, zp)]
        out.write(f"setblock ~{xp} ~-{depth - 1} ~{zp} minecraft:torch\n")

out.close()