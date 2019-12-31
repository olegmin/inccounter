from file_handlers import csv_reader, csv_writer
from tools import get_config, print_config, timer
from compares import compare_time, compare_values


@timer
def count_incedents():
    """Главный механизм, выполнен в виде генератора для экономии памяти.
        :yield: расчетные данные по каждому значению в файле
    """
    # Getting configuration of programm
    conf = get_config()
    print_config(conf)

    # Prepare CSV writer coroutine
    writer = csv_writer(conf['output_file'])

    # Working with data
    for sample in csv_reader(conf['input_file']):
        counter = 0
        for data in csv_reader(conf['input_file']):
            # Same ID
            if data[0] == sample[0]:
                continue
            # Not valid time
            if not compare_time(conf['delta_time'], sample[3], data[3]):
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
    count_incedents()
