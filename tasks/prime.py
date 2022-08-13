__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    if number in range(2):
        return False

    if number == 2:
        return True

    for i in range(2, int(number ** 0.5) + 2):
        if number % i == 0:
            return False
    return True
