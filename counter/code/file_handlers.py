import csv


def convert(data):
    data[0] = int(data[0])
    data[1] = int(data[1])
    data[2] = int(data[2])
    data[3] = float(data[3])
    return data


def csv_reader(path="/data/incedents.csv"):
    with open(path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            # Head of table - continue reading file
            if 'id' in row:
                continue
            # Return converted line from file
            yield convert(row)


def csv_writer(path):
    # TODO: finish this code
    pass