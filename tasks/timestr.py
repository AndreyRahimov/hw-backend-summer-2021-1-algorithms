__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """

    secs = seconds % 60
    mins = seconds // 60 % 60
    hours = seconds // 3600 % 24
    days = seconds // 86400
    result = ''
    result += f'{str(days) if days > 9 else "0" + str(days)}d' * (days > 0)
    result += f'{str(hours) if hours > 9 else "0" + str(hours)}h' * max(hours > 0, days > 0)
    result += f'{str(mins) if mins > 9 else "0" + str(mins)}m' * max(mins > 0, hours > 0, days > 0)
    result += f'{str(secs) if secs > 9 else "0" + str(secs)}s'

    return result
