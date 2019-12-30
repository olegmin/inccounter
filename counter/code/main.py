from file_handlers import csv_reader, csv_writer
from tools import get_config
from compares import compare_time, compare_values


def count_incedents():
    """Главный механизм, выполнен в виде генератора для экономии памяти.
        :yield: расчетные данные по каждому значению в файле
    """
    # TODO: insert path to CSV file. Config data from command line.
    dT = 0.3
    # Getting configuration of programm
    # conf = get_config()
    # Prepare CSV writer coroutine
    writer = csv_writer()
    # Working with data
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
        # Write result to file
        writer.send([ sample[0], counter])
    # Close writer coroutine
    writer.close()


if __name__ == "__main__":
    # count_incedents()

    print(get_config())
