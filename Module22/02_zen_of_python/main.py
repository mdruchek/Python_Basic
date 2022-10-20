def zen_on_contrary(file):
    file_zen = open('zen.txt', 'r', encoding='utf8')
    file_zen_list = []
    for i_str in file_zen:
        file_zen_list.append(i_str)
    file_zen.close()

    file_zen_list.reverse()
    for i_str in file_zen_list:
        print(i_str, end='' if file_zen_list.index(i_str) != 0 else '\n')


zen_on_contrary('zen.txt')