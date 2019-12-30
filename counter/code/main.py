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
    pass



if __name__ == "__main__":
    conf = get_config()

    count_incedents(conf)
