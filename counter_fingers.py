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

print(value_passing_fingers(1, 7), counter_fingers['f5l'])