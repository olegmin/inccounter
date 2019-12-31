import sys
import argparse
import time


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


def print_config(c):
    print("Start working with config params:")
    for k,v in c.items():
        print(f"\t- {k}: {v}")


def timer(func):

    def now_in_ms():
        return int(round(time.time() * 1000))

    def wrap_counter(*args,**kwargs):
        start_time = now_in_ms()
        func(*args, **kwargs)
        run_time = now_in_ms()-start_time
        print(f"Finish in {run_time // 1000}.{(run_time % 100):03d} seconds.")

    return wrap_counter
