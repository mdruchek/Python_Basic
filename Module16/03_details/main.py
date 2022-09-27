def get_input_product():
    return input('Название детали: ')


def product_search(product, shop):
    summ_cost = 0
    count = 0
    for i_product in range(len(shop)):
        if shop[i_product][0] == product:
            summ_cost += shop[i_product][1]
            count += 1
    return count, summ_cost


def display_result(count, summ_cost):
    print('\nКол-во деталей - ', count)
    print('Общая стоимость - ', summ_cost)


shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100],
        ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

product = get_input_product()
count, summ_cost = product_search(product, shop)
display_result(count, summ_cost)