import csv


def csv_reader(path="/data"):
    # TODO: fix this function on csv reading
    with open(path) as f:
        yield f.readline()


def csv_writer(path):
    # TODO: finish this code
    pass