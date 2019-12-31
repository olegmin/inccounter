import sys
import argparse


def get_config():
    """Читает командную строку.
    :return: словарь с конфигурационными данными
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-inf', '--input_file', default="/data/incedents.csv", type=str)
    parser.add_argument('-otf', '--output_file', default="/data/counts.csv", type=str)
    parser.add_argument('-dt', '--delta_time', default=0.3, type=float)

    ns = parser.parse_args(sys.argv[1:])

    return {
        'input_file': ns.input_file if ns.input_file else ns.inf,
        'output_file': ns.output_file if ns.output_file else ns.otf,
        'delta_time': ns.delta_time if ns.delta_time else ns.dt
    }


def coroutine(f):
    def wrap_coro(*args,**kwargs):
        gen = f(*args,**kwargs)
        gen.send(None)
        gen.send(['id', 'counts'])
        return gen
    return wrap_coro


@coroutine
def csv_writer(path):
    """ Write data to a CSV file path"""
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        while True:
            data = yield
            writer.writerow(data)