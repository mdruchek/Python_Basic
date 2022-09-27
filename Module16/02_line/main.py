def sort_ascending_order(unsorted_list):
    sorted_list = []
    sorted_list.append(unsorted_list[0])
    for i_list in range(1, len(unsorted_list)):
        for i_sorted_list in range(len(sorted_list)):
            if unsorted_list[i_list] <= sorted_list[i_sorted_list]:
                sorted_list.insert(i_sorted_list, unsorted_list[i_list])
                break
            if i_sorted_list == len(sorted_list) - 1:
                sorted_list.append(unsorted_list[i_list])
    return sorted_list


class_1 = list(range(160, 176 + 1, 2))
class_2 = list(range(162, 180 + 1, 3))

class_1.extend(class_2)

print('Отсортированный список учеников: ', sort_ascending_order(class_1))