from file_handlers import csv_reader, csv_writer


def get_config():
    """Читает командную строку.
    :return: словарь с конфигурационными данными
    """
    return {}


def count_incedents(conf):
    """Главный механизм, обрабатывающий все события программы.
    :return: ничего, заставляет работать других
    """
    # TODO: insert path to CSV file. Config data from command line.
    reader = csv_reader()
    for data in reader:
        print(f"{data}\n")


if __name__ == "__main__":
    conf = get_config()

    count_incedents(conf)
