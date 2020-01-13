import csv


def convert(data):
    data[0] = int(data[0])
    data[1] = int(data[1])
    data[2] = int(data[2])
    data[3] = float(data[3])
    return data


def csv_reader(path):
    """Read lines from CSV file path"""
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            # Head of table - continue reading file
            if 'id' in row:
                continue
            # Return converted line from file
            yield convert(row)


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
