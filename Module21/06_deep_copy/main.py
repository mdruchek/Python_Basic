site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {product} недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на {product}',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

def output_site_structure(struct, product, depth = 1, len_previous_structure = None, previous_number_key = None):
    if depth == 1:
        print('site = {')
    number_key = 0
    flag = False

    for i_key, i_value in struct.items():
        number_key += 1

        if isinstance(i_value, dict):
            print("{indent}'{key}': {{".format(indent='\t'*2*depth,key=i_key))
            output_site_structure(i_value, product, depth+1, len(struct), number_key)
        else:

            print("{indent}'{key}': '{value}'".format(indent='\t' * 2 * depth,
                                                      key=i_key,
                                                      value=i_value.format(product=product)),
                  end='{}'.format(',\n' if len(struct) != number_key else '\n'))

    print("{indent}}}".format(indent='\t'*(depth-1)*2),
          end='{}'.format(',\n' if len_previous_structure != previous_number_key else '\n'))


number_sites = int(input('Сколько сайтов: '))
sites = []
for index in range(number_sites):
    product = input('Введите название продукта для нового сайта: ')
    sites.append(product)
    for product in sites:
        print('Сайт для {}:'.format(product))
        output_site_structure(site, product)
        print()