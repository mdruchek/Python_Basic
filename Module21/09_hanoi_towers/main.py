def print_movements_disks(num_disk, source_rod, destination_rod):
    print('Переложить диск {} со стержня {} на стержень {}'.format(num_disk, source_rod, destination_rod))


def interim_calculations(rods):
    flag_disk_odd = False
    flag_rod_null = False
    for rod, val in rods.items():
        if len(val) == 0:
            rod_null = rod
            flag_rod_null = True
        else:
            if not flag_rod_null:
                rod_null = None
        if len(val) != 0 and val[len(val) - 1] == 1:
            rod_num_disk_12 = rod
        if len(val) != 0 and val[len(val) - 1] % 2 != 0 and val[len(val) - 1] != 1:
            rod_num_disk_odd = rod
            flag_disk_odd = True
        else:
            if not flag_disk_odd:
                rod_num_disk_odd = None
    return rod_null, flag_rod_null, rod_num_disk_12, rod_num_disk_odd, flag_disk_odd


def move(n, x, y, z=0, start=True, rods=dict(), source_rod=0):
    if start:
        source_rod = x
        z = 6 - x - y
        rods = {x: [i for i in range(n, 0, -1)], y: [], z: []}
        if n % 2 != 0:
              y, z = z, y
    if len(rods[source_rod]) == 0:
        for rod, val in rods.items():
            if len(val) != 0 and val[len(val) - 1] == 1:
                source_rod = rod
    print_movements_disks(rods[x][len(rods[x]) - 1], x, z)
    rods[z].append(rods[x].pop())
    print_movements_disks(rods[x][len(rods[x]) - 1], x, y)
    rods[y].append(rods[x].pop())
    print_movements_disks(rods[z][len(rods[z]) - 1], z, y)
    rods[y].append(rods[z].pop())

    if len(rods[source_rod]) == 0 and len(rods[z]) == 0:
        return

    rod_null, flag_rod_null, rod_num_disk_12, rod_num_disk_odd, flag_disk_odd = interim_calculations(rods)

    if rod_num_disk_12 != source_rod and flag_rod_null:
        #if flag_rod_null:
        print_movements_disks(rods[source_rod][len(rods[source_rod]) - 1], source_rod, rod_null)
        rods[rod_null].append(rods[source_rod].pop())
    else:
        min_disk_excluding_12 = n
        for rod, val in rods.items():
            if rod != rod_num_disk_12 and val[len(val) - 1] < min_disk_excluding_12:
                min_disk_excluding_12 = val[len(val) - 1]
                rod_min_disk_excluding_12 = rod
        print_movements_disks(rods[rod_min_disk_excluding_12][len(rods[rod_min_disk_excluding_12]) - 1], rod_min_disk_excluding_12, 6 - rod_min_disk_excluding_12 - rod_num_disk_12)
        rods[6 - rod_min_disk_excluding_12 - rod_num_disk_12].append(rods[rod_min_disk_excluding_12].pop())

    rod_null, flag_rod_null, rod_num_disk_12, rod_num_disk_odd, flag_disk_odd = interim_calculations(rods)

    if flag_disk_odd:
        destination_disk = rod_num_disk_odd
    else:
        destination_disk = rod_null
    move(n, rod_num_disk_12, destination_disk, z=6-rod_num_disk_12-destination_disk, start=False, rods=rods, source_rod=source_rod)


quantity_disks = int(input('Введите количество дисков: '))
move(quantity_disks, 1, 3)