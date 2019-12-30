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
        'if': ns.input_file if ns.input_file else ns.inf,
        'of': ns.output_file if ns.output_file else ns.otf,
        'dt': ns.delta_time if ns.delta_time else ns.dt
    }
