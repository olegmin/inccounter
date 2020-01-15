
import time


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
        print(f"\n\nFinish in {run_time // 1000}.{(run_time % 100):03d} seconds.\n\n")

    return wrap_counter
