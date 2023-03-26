import pytest

#Пока протестировано только 2 функции

keys_dict = {2: {'ant_key': '1', 'raw': 0, 'column': 1, 'qwer_key': '1'},
             3: {'ant_key': '2', 'raw': 0, 'column': 2, 'qwer_key': '2'},
             4: {'ant_key': '3', 'raw': 0, 'column': 3, 'qwer_key': '3'},
             5: {'ant_key': '4', 'raw': 0, 'column': 4, 'qwer_key': '4'},
             6: {'ant_key': '5', 'raw': 0, 'column': 5, 'qwer_key': '5'},
             7: {'ant_key': '6', 'raw': 0, 'column': 6, 'qwer_key': '6'},
             8: {'ant_key': '7', 'raw': 0, 'column': 7, 'qwer_key': '7'},
             9: {'ant_key': '8', 'raw': 0, 'column': 8, 'qwer_key': '8'},
             10: {'ant_key': '9', 'raw': 0, 'column': 9, 'qwer_key': '9'},
             11: {'ant_key': '0', 'raw': 0, 'column': 10, 'qwer_key': '0'},
             12: {'ant_key': '*', 'raw': 0, 'column': 11, 'qwer_key': '-'},
             13: {'ant_key': '=', 'raw': 0, 'column': 12, 'qwer_key': '='},
             14: {'ant_key': '', 'raw': 0, 'column': 0, 'qwer_key': ''},
             15: {'ant_key': '', 'raw': 0, 'column': 0, 'qwer_key': ''},
             16: {'ant_key': 'ц', 'raw': 1, 'column': 1, 'qwer_key': 'й'},
             17: {'ant_key': 'ь', 'raw': 1, 'column': 2, 'qwer_key': 'ц'},
             18: {'ant_key': 'я', 'raw': 1, 'column': 3, 'qwer_key': 'у'},
             19: {'ant_key': ',', 'raw': 1, 'column': 4, 'qwer_key': 'к'},
             20: {'ant_key': '.', 'raw': 1, 'column': 5, 'qwer_key': 'е'},
             21: {'ant_key': 'з', 'raw': 1, 'column': 6, 'qwer_key': 'н'},
             22: {'ant_key': 'в', 'raw': 1, 'column': 7, 'qwer_key': 'г'},
             23: {'ant_key': 'к', 'raw': 1, 'column': 8, 'qwer_key': 'ш'},
             24: {'ant_key': 'д', 'raw': 1, 'column': 9, 'qwer_key': 'щ'},
             25: {'ant_key': 'ч', 'raw': 1, 'column': 10, 'qwer_key': 'з'},
             26: {'ant_key': 'ш', 'raw': 1, 'column': 11, 'qwer_key': 'х'},
             27: {'ant_key': 'щ', 'raw': 1, 'column': 12, 'qwer_key': 'ъ'},
             28: {'ant_key': '', 'raw': 0, 'column': 0, 'qwer_key': ''},
             29: {'ant_key': '', 'raw': 0, 'column': 0, 'qwer_key': ''},
             30: {'ant_key': 'у', 'raw': 2, 'column': 1, 'qwer_key': 'ф'},
             31: {'ant_key': 'и', 'raw': 2, 'column': 2, 'qwer_key': 'ы'},
             32: {'ant_key': 'е', 'raw': 2, 'column': 3, 'qwer_key': 'в'},
             33: {'ant_key': 'о', 'raw': 2, 'column': 4, 'qwer_key': 'а'},
             34: {'ant_key': 'а', 'raw': 2, 'column': 5, 'qwer_key': 'п'},
             35: {'ant_key': 'л', 'raw': 2, 'column': 6, 'qwer_key': 'р'},
             36: {'ant_key': 'н', 'raw': 2, 'column': 7, 'qwer_key': 'о'},
             37: {'ant_key': 'т', 'raw': 2, 'column': 8, 'qwer_key': 'л'},
             38: {'ant_key': 'с', 'raw': 2, 'column': 9, 'qwer_key': 'д'},
             39: {'ant_key': 'р', 'raw': 2, 'column': 10, 'qwer_key': 'ж'},
             40: {'ant_key': 'й', 'raw': 2, 'column': 11, 'qwer_key': 'э'},
             41: {'ant_key': 'ё', 'raw': 0, 'column': 0, 'qwer_key': 'ё'},
             42: {'ant_key': '', 'raw': 0, 'column': 0, 'qwer_key': ''},
             43: {'ant_key': '', 'raw': 0, 'column': 0, 'qwer_key': ''},
             44: {'ant_key': 'ф', 'raw': 3, 'column': 1, 'qwer_key': 'я'},
             45: {'ant_key': 'э', 'raw': 3, 'column': 2, 'qwer_key': 'ч'},
             46: {'ant_key': 'х', 'raw': 3, 'column': 3, 'qwer_key': 'с'},
             47: {'ant_key': 'ы', 'raw': 3, 'column': 4, 'qwer_key': 'м'},
             48: {'ant_key': 'ю', 'raw': 3, 'column': 5, 'qwer_key': 'и'},
             49: {'ant_key': 'б', 'raw': 3, 'column': 6, 'qwer_key': 'т'},
             50: {'ant_key': 'м', 'raw': 3, 'column': 7, 'qwer_key': 'ь'},
             51: {'ant_key': 'п', 'raw': 3, 'column': 8, 'qwer_key': 'б'},
             52: {'ant_key': 'г', 'raw': 3, 'column': 9, 'qwer_key': 'ю'},
             53: {'ant_key': 'ж', 'raw': 3, 'column': 10, 'qwer_key': '.'},
             54: {'ant_key': '', 'raw': 3, 'column': 10, 'qwer_key': ','},
             55: {'ant_key': '', 'raw': 0, 'column': 0, 'qwer_key': ''},
             56: {'ant_key': '', 'raw': 0, 'column': 0, 'qwer_key': ''},
             57: {'ant_key': ' ', 'raw': 0, 'column': 0, 'qwer_key': ' '},
             58: {'ant_key': '', 'raw': 0, 'column': 0, 'qwer_key': ''}}


def get_cords(sim_from_text):
    for key in keys_dict.keys():
        for value in keys_dict[key]['ant_key']:
            if value == sim_from_text:
                return [keys_dict[key]['raw'],
                        keys_dict[key]['column']]  # первый элемент возвращаемого списка - строка, второй - столбец


def test_cords_1():
    res = get_cords('1')
    assert res == [0, 1]


def test_cords_2():
    res = get_cords('2')
    assert res == [0, 6]


def test_cords_3():
    res = get_cords('3')
    assert res == [2]


def test_cords_4():
    x = 1
    res = get_cords('4')
    assert res == [0, x]


def test_cords_5():
    res = get_cords('5')
    assert res == [5, 0]


counter_fingers = {'f5l': 0, 'f4l': 0, 'f3l': 0, 'f2l': 0, 'f1l': 0, 'f1r': 0, 'f2r': 0, 'f3r': 0, 'f4r': 0, 'f5r': 0}


def value_passing_fingers(column, value):
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


def test_finger_1():
    value_passing_fingers(6, 1)
    assert counter_fingers['f5l'] == 1
# значение column не соответствует counter_fingers (0 != 4)


# def test_finger_2():
#    value_passing_fingers(2, 1)
#    assert counter_fingers['f4l'] == 4
# значение counter_fingers не соответсвует 4 (0 != 4)


def test_finger_2():
    value_passing_fingers(3, 3)
    assert counter_fingers['f3l'] == 5
# значение value не соответсвует значению 5


def test_finger_3():
    value_passing_fingers(3, 1)
    assert counter_fingers['f3l'] == 4
# верно
