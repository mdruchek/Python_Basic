players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

print([(i_key[0], i_key[1], i_value[0], i_value[1], i_value[2])
       for i_key, i_value in players.items()])
