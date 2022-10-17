def move(n, x, y, z=0, start=True, rods=dict(), source_rod=0):
    if start:
        source_rod = x
        z = 6 - x - y
        rods = {x: [i for i in range(n, 0, -1)], y: [], z: []}
    if rods[source_rod] == 0:
        for rod, val in rods.items():
            if len(val) != 0 and val[len(val) - 1] == 1:
                source_rod = rod
    rods[z].append(rods[x].pop())
    rods[y].append(rods[x].pop())
    rods[y].append(rods[z].pop())

    flag_disk_odd = False
    flag_rod_null = False
    for rod, val in rods.items():
        if len(val) == 0:
            rod_null = rod
            flag_rod_null = True
        if len(val) != 0 and val[len(val) - 1] == 1:
            rod_num_disk_12 = rod

    if rod_num_disk_12 != source_rod:
        if flag_rod_null:
            rods[rod_null].append(rods[source_rod].pop())
        else:
            min_disk_excluding_12 = n
            for rod, val in rods.items():
                if rod != rod_num_disk_12 and val[len(val) - 1] < min_disk_excluding_12:
                    min_disk_excluding_12 = val[len(val) - 1]
                    rod_min_disk_excluding_12 = rod
            rods[6 - rod_min_disk_excluding_12 - rod_num_disk_12].append(rods[rod_min_disk_excluding_12].pop())
    else:
        min_disk_excluding_12 = n
        for rod, val in rods.items():
            if rod != rod_num_disk_12 and val[len(val) - 1] < min_disk_excluding_12:
                min_disk_excluding_12 = val[len(val) - 1]
                rod_min_disk_excluding_12 = rod
        rods[6 - rod_min_disk_excluding_12 - rod_num_disk_12].append(rods[rod_min_disk_excluding_12].pop())

    for rod, val in rods.items():
        if len(val) != 0 and val[len(val) - 1] % 2 != 0 and val[len(val) - 1] != 1:
            rod_num_disk_odd = rod
            flag_disk_odd = True

    for rod, val in rods.items():
        if len(val) == 0:
            rod_null = rod
            flag_rod_null = True



    if flag_disk_odd:
        destination_disk = rod_num_disk_odd
    else:
        destination_disk = rod_null
    move(n, rod_num_disk_12, destination_disk, z=6-rod_num_disk_12-destination_disk, start=False, rods=rods, source_rod=source_rod)


move(6, 1, 2)