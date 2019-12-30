def get_config():
    """Читает командную строку.
    :return: словарь с конфигурационными данными
    """
    return {}


def compare_time(dT:float, t1:float, t2:float):
    return 0 < (t1-t2) <= dT


def compare_values(d1, d2):
    return d1[1] == d2[1] and d1[2] == d2[2]
