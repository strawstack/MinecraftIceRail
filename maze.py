import math
import random

size = 65
edges = []
union_find = {}

# Init self loops
for xx in range(size + 2):
    for yy in range(size + 2):
        union_find[(xx, yy)] = (xx, yy)

def union(union_find, a, b):
    ga = find(union_find, a)
    gb = find(union_find, b)
    union_find[ga] = gb

def find(union_find, a):
    c = a
    while union_find[c] != c:
        c = union_find[c]
    union_find[a] = c
    return c

funt_name = "maze"
out = open(f"{funt_name}.mcfunction", "a")

rooms = []
for xx in range(0, size, 2):
    for yy in range(0, size, 2):
        rooms.append(
            (xx, yy)
        )

edges = []
for room in rooms:
    edges.append(
        (
            (room[0], room[1]),
            (room[0], room[1] + 2)
        )
    )
    edges.append(
        (
            (room[0], room[1]),
            (room[0] + 2, room[1])
        )
    )

random.shuffle(edges)

def getEid(edge):
    r1 = edge[0]
    r2 = edge[1]

    if r1[0] != r2[0]:
        return (r1[0] + 1, r1[1])
    else:
        return (r1[0], r1[1] + 1)

used_edges = {}

for edge in edges:
    r1 = edge[0]
    r2 = edge[1]

    g1 = find(union_find, r1)
    g2 = find(union_find, r2)

    if g1 != g2:
        eid = getEid(edge)
        used_edges[eid] = True
        union(union_find, g1, g2)

block = "oak_log"
out.write(f"fill ~ ~ ~ ~{size} ~5 ~{size} minecraft:air\n")
out.write(f"fill ~ ~ ~ ~{size} ~ ~{size} minecraft:dirt\n")

for xx in range(0, size):
    for yy in range(0, size):
        if xx % 2 == 0 and yy % 2 == 1:
            eid = (xx, yy)
            if eid not in used_edges:
                # Unused horizontal edge
                out.write(f"fill ~{xx} ~ ~{yy} ~{xx} ~5 ~{yy} minecraft:{block}\n")

        elif xx % 2 == 0 and yy % 2 == 0:
            pass # this is a room

        elif xx % 2 == 1 and yy % 2 == 1:
            # Pillar - never used
            out.write(f"fill ~{xx} ~ ~{yy} ~{xx} ~5 ~{yy} minecraft:{block}\n")


        elif xx % 2 == 1 and yy % 2 == 0:
            eid = (xx, yy)
            if eid not in used_edges:
                # Unused vertical edge
                out.write(f"fill ~{xx} ~ ~{yy} ~{xx} ~5 ~{yy} minecraft:{block}\n")

# out.write(f"fill ~{xx} ~ ~{yy} ~{xx} ~4 ~{yy} minecraft:oak_leaves\n")

out.close()