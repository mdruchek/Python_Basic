site = {
	'html': {
		'head': {
			'title': 'Мой сайт'
		},
		'body': {
			'h2': 'Здесь будет мой заголовок',
			'div': 'Тут, наверное, какой-то блок',
			'p': 'А вот здесь новый абзац'
		}
	}
}

def search_key(site, key, depth = None):
	if key in site:
		return site[key]
	for i_value in site.values():
		if isinstance(i_value, dict):
			if depth is not None:
				depth -= 1
				if depth == 0:
					result = None
					break
			result = search_key(i_value, key, depth)
			if result:
				break
	else:
		result = None

	return result

key = input('Введите искомый ключ: ')
question = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if question == 'y':
	depth = int(input('Введите максимальную глубину: '))
	value = search_key(site, key, depth=depth)
else:
	value = search_key(site, key)

print('Значение ключа: {}'.format(value))