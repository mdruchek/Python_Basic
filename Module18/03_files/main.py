file = input('Название файла: ', )

if file[0] in '@№$%^&\*()':
    print('Ошибка: название начинается на один из специальных символов.')
elif not file.endswith('.txt') and not file.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx.')
else:
    print('Файл назван верно.')