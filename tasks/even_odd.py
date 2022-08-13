__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    if len(arr) in (0, 1):
        return 0

    evens = 0
    odds = 0
    for i in arr:
        if i % 2 == 0:
            evens = evens + i
        else:
            odds = odds + i

    if odds == 0:
        return 0

    return evens / odds
