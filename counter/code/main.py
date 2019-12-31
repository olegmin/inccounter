from file_handlers import csv_reader, csv_writer
from tools import get_config, print_config, timer
from compares import compare_time, compare_values
import pandas as pd

@timer
def count_incedents():
    """Главный механизм, выполнен в виде генератора для экономии памяти.
        :yield: расчетные данные по каждому значению в файле
    """
    # Getting configuration of programm
    conf = get_config()

    # # Prepare CSV writer coroutine
    # writer = csv_writer(conf['output_file'])

    # Reading all data
    all_data = pd.read_csv(conf['input_file'], sep=';')
    print(all_data)

    res = all_data.groupby(['feature1', 'feature2'])['id'].count()
    print(res)

    # # Working with data
    # for sample in all_data:
    #     counter = 0
    #     for data in all_data:
    #         # Same ID
    #         if data[0] == sample[0]:
    #             continue
    #         # Not valid time
    #         if not compare_time(conf['delta_time'], sample[3], data[3]):
    #             continue
    #         # Not matched values
    #         if not compare_values(sample, data):
    #             continue
    #         # Increment counter
    #         counter += 1
    #     # Write results to file
    #     writer.send([sample[0], counter])
    #
    # # Close writer coroutine
    # writer.close()


if __name__ == "__main__":
    count_incedents()
