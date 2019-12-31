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

    # Reading all data
    all_data = pd.read_csv(conf['input_file'], sep=';', usecols=['feature1', 'feature2', 'time'])
    # Test data
    print(all_data)


if __name__ == "__main__":
    count_incedents()
