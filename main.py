import re


from keysdikt import keys_dict

counter_fingers = {'f5l': 0, 'f4l': 0, 'f3l': 0, 'f2l': 0, 'f1l': 0, 'f1r': 0, 'f2r': 0, 'f3r': 0, 'f4r': 0, 'f5r': 0}
# словарь для подсчета колличества шагов пройденных каждым пальцем


def get_cords(sim_from_text):
    """
    Функция для получения координат символа из keys_dict

    :параметр sim_from_text: строчный символ для которого нужно получить координвты
    :return: функция фозвращает список с 2-мя элементами, где 0-й элемент это строка, а 1-й - столбец
    """
    for key in keys_dict.keys():
        for value in keys_dict[key]['ant_key']:
            if value == sim_from_text:
                return [keys_dict[key]['raw'],
                        keys_dict[key]['column']]  # первый элемент возвращаемого списка - строка, второй - столбец


# функция для записи шагов пройденных каждым пальцем. Поступает номер колонки и колличество шагов,
# в зависимости от ряда выбирается палец и записывается кол-во шагов


def value_passing_fingers(column, value):
    """
    Функция для записи шагов пройденных каждым пальцем. Поступает номер колонки и колличество шагов,
    в зависимости от ряда выбирается палец и записывается кол-во шагов

    параметр column: номер столбца
    параметр value: колличество шагов которое прошёл палец
    return: функция ничего не возвращает, а записывает значения в counter_fingers
    """
    match column:
        case 0 | 1:
            counter_fingers['f5l'] += value
        case 2:
            counter_fingers['f4l'] += value
        case 3:
            counter_fingers['f3l'] += value
        case 4 | 5:
            counter_fingers['f2l'] += value
        case 6 | 7:
            counter_fingers['f2r'] += value
        case 8:
            counter_fingers['f3r'] += value
        case 9:
            counter_fingers['f4r'] += value
        case 10 | 11 | 12:
            counter_fingers['f5r'] += value


# функция для подсчета шагов. При поступлении 2-х символов, считает шаги затраченные на нажатие второго.


def count_steps(first_sim, second_sim):
    """
    Функция для подсчета шагов. При поступлении 2-х символов, считает шаги затраченные на нажатие второго.

    :param first_sim: предыдущий символ текста
    :param second_sim: последующий символ текста
    :return: функция ничего не возвращает, а передаёт значения в функцию для записи шагов value_passing_fingers
    """
    if get_cords(first_sim)[1] - get_cords(second_sim)[1] == 0:  # если символы находятся в одном столбце
        value_passing_fingers(get_cords(second_sim)[1], abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]))
        # записываем в словаль колличество шагов в зависимости от разности номеров строк в которые входят элементы
    else:  # если же символы находятся в разных столбцах
        if get_cords(first_sim)[0] != get_cords(second_sim)[0]:  # если символы в разных строках
            match get_cords(second_sim)[1]:  # в зависимости от номеров столбцов записывам кол-во шагов в словарь
                case 5 | 6:  # т.к. 5й и 6й столбцы бьются 1м пальцем(л. или п. указательным)
                    # прибавляем 1 шаг для занятия позиции от home ряда
                    if get_cords(second_sim)[0] == 2:
                        value_passing_fingers(get_cords(second_sim)[1], 1)
                    else:
                        value_passing_fingers(get_cords(second_sim)[1],
                                              abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:  # столбцы бьющиеся 1м пальцем
                    if get_cords(second_sim)[0] == 2:
                        pass
                    else:
                        value_passing_fingers(get_cords(second_sim)[1],
                                              abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]))
                case 11:  # 11 и 12 бьются п.мезинцем поэтому прибавляем 1 или 2 шага для занятия позиции
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]) + 1)
                case 12:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(first_sim)[0] - get_cords(second_sim)[0]) + 2)
        if get_cords(first_sim)[0] == get_cords(second_sim)[0]:  # если символы в одинаковых строках
            match get_cords(second_sim)[1]:
                case 5 | 6 | 11:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(second_sim)[0] - 2) + 1)
                case 1 | 2 | 3 | 4 | 7 | 8 | 9 | 10:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(second_sim)[0] - 2))
                case 12:
                    value_passing_fingers(get_cords(second_sim)[1],
                                          abs(get_cords(second_sim)[0] - 2) + 2)


if __name__ == '__main__':
    with open('text.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    text = re.sub(r'[^А-Яа-я,*.]', '', text)
    text = list(text)
    list_upper_case = [i for i in text if i.isupper()]
    list_unsup_chr = [i for i in text if i == 'ъ']
    value_passing_fingers(0, (len(list_upper_case) + len(list_unsup_chr))*2)
    text = ''.join(text)
    text = list(re.sub(r'ъ', 'ь', text))
    text = [i.lower() for i in text]
    for i in range(1, len(text)):
        count_steps(text[i-1], text[i])
    print("Количество шагов для каждого пальца", counter_fingers)


