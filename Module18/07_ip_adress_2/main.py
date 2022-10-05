ip = input('Введите IP: ').split('.')

ip_correct = True
for number in ip:
    if not number.isdigit():
        print('{} - это не целое число.'.format(number))
        ip_correct = False
        break
    if int(number) > 255:
        print('{} превышает 255.'.format(number))
        ip_correct = False
        break
    if len(ip) != 4:
        print('Адрес - это четыре числа, разделённые точками.')
        ip_correct = False
        break

if ip_correct:
    print('IP-адрес корректен.')