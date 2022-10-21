def string_validation(line):
    line_list = line.split()
    if len(line_list) != 3:
        raise IndexError
    if not line_list[0].isalpha():
        raise NameError
    if '@' not in line_list[1] or '.' not in line_list[1]:
        raise SyntaxError
    if not 10 <= int(line_list[2]) <= 99:
        raise ValueError

def verification_registration_data(registrations_file, good_log_file, bad_log_file):

        with open(registrations_file, 'r', encoding='utf8') as registrations, open(good_log_file, 'a', encoding='utf8') as good_log, open(bad_log_file, 'a', encoding='utf8') as bad_log:
            for line in registrations:
                if '\n' in line:
                    line =line[:len(line) - 1]
                try:
                    string_validation(line)
                except IndexError:
                    bad_log.write('{}    НЕ присутствуют все три поля\n'.format(line))
                except NameError:
                    bad_log.write('{}    Поле имени содержит НЕ только буквы\n'.format(line))
                except SyntaxError:
                    bad_log.write('{}    Поле «Имейл» НЕ содержит @ и .(точку)\n'.format(line))
                except ValueError:
                    bad_log.write('{}    Поле «Возраст» НЕ является числом от 10 до 99\n'.format(line))
                else:
                    good_log.write('{}\n'.format(line))

verification_registration_data('registrations.txt', 'registrations_good.log', 'registrations_bad.log')
