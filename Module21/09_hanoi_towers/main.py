def move(n, x, y, z=0, start=True, rods=dict()):
    if start:
        z = 6 - x - y
        rods = {x: [i for i in range(n, 0, -1)], y: [], z: []}
    if start or rods[x] == [cound for cound in range(len(rods[x]), 0, -1)]:
        rods[z].append(rods[x].pop())
        rods[y].append(rods[x].pop())
        rods[y].append(rods[z].pop())
    if not start:
        if len(rods[y]) == 0 and n != 0:
            rods[y].append(rods[x].pop())
            rods[x].append(rods[z].pop())
            rods[y].append(rods[z].pop())
            rods[y].append(rods[x].pop())
        if len(rods[z]) == 0 and n != 0:
            rods[z].append(rods[x].pop())
            rods[x].append(rods[y].pop())
            rods[z].append(rods[y].pop())
            rods[z].append(rods[x].pop())
        if len(rods[x]) == 0:
            rods[x].append(rods[y].pop())
            rods[y].append(rods[z].pop())
            rods[x].append(rods[z].pop())
            rods[x].append(rods[y].pop())
            rods[z].append(rods[y].pop())
        if len(rods[x]) != 0 and len(rods[y]) != 0 and len(rods[z]) != 0 and n != 0:
            if len(rods[y]) > len(rods[z]):
                rods[z].append(rods[y].pop())
                rods[x].append(rods[y].pop())
                rods[x].append(rods[z].pop())
                rods[y].append(rods[z].pop())
                rods[z].append(rods[x].pop())
                rods[y].append(rods[x].pop())
                rods[y].append(rods[z].pop())
            if len(rods[z]) > len(rods[y]):
                rods[y].append(rods[z].pop())
                rods[x].append(rods[z].pop())
                rods[x].append(rods[y].pop())
                rods[y].append(rods[y].pop())
                rods[y].append(rods[x].pop())
                rods[z].append(rods[x].pop())
                rods[z].append(rods[y].pop())

    if len(rods[y]) != n:
        move(n, x, y, z, False, rods)
    else:
        return

move(5, 1, 2)