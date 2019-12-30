from file_handlers import csv_reader, csv_writer
from tools import get_config
from compares import compare_time, compare_values


def count_incedents(conf, dT=0.3):
    """Главный механизм, выполнен в виде генератора для экономии памяти.
        :yield: расчетные данные по каждому значению в файле
    """
    # TODO: insert path to CSV file. Config data from command line.
    for sample in csv_reader():
        counter = 0
        for data in csv_reader():
            # Same ID
            if data[0] == sample[0]:
                continue
            # Not valid time
            if not compare_time(dT, sample[3], data[3]):
                continue
            # Not matched values
            if not compare_values(sample, data):
                continue
            # Increment counter
            counter += 1
        yield [sample[0], counter]


if __name__ == "__main__":
    conf = get_config()
    writer = csv_writer()
    for val in count_incedents(conf):
        print(f"Write next value: {val}")
        writer.send(val)
    writer.close()
