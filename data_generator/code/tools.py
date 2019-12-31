import sys
import argparse


def get_config():
    """Читает командную строку.
    :return: словарь с конфигурационными данными
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-otf', '--output_file', default="/data/incedents.csv", type=str)
    parser.add_argument('-dc', '--data_count', default=1000, type=int)

    ns = parser.parse_args(sys.argv[1:])

    return {
        'output_file': ns.output_file if ns.output_file else ns.otf,
        'data_count': ns.delta_time if ns.delta_time else ns.dt
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