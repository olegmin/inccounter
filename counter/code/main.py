from file_handlers import csv_reader, csv_writer
from tools import get_config, compare_time, compare_values


def count_incedents(conf, dT=0.3):
    """Главный механизм, обрабатывающий все события программы.
    :return: ничего, заставляет работать других
    """
    # TODO: insert path to CSV file. Config data from command line.
    res = []
    for sample in csv_reader():
        res.append({
            'id': sample[0],
            'count': 0
        })
        for data in csv_reader():
            # Same ID
            if data[0] == res[-1]['id']:
                continue
            # Not valid time
            if not compare_time(dT, sample[3], data[3]):
                continue
            # Not matched values
            if not compare_values(sample, data):
                continue
            res[-1]['count'] += 1
    return res


if __name__ == "__main__":
    conf = get_config()
    res = count_incedents(conf)

    for val in res:
        print(val)