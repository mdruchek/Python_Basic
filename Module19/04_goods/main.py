goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for good_goods in goods:
    product_found = False

    for good_store in store:

        if good_store == goods[good_goods]:
            product_found = True
            quantity_sum = 0
            price_sum = 0

            for count in store[good_store]:
                quantity = int(count['quantity'])
                price = int(count['price']) * quantity
                quantity_sum +=quantity
                price_sum += price

                if price_sum % 10 == 4:
                    ending_format = 'я'
                else:
                    ending_format = 'ей'

            print('{good} - {quantity} штук, стоимость {price} рубл{ending}'.format(
                good = good_goods,
                quantity = quantity_sum,
                price = price_sum,
                ending = ending_format
            ))

        if product_found:
            break