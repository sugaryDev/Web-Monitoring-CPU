import psutil


def core_utilization(interval: float) -> float | list[float]:
    """
    Метод возвращает список, усредненной загрузки каждого ядра.
    Номера ядер соответствуют порядку в списке.
    :param interval: Интервал времени
    :return:
    """
    return psutil.cpu_percent(interval, percpu=True)
