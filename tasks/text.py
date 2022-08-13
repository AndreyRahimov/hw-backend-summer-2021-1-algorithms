from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    lst = [i.strip() for i in text.split()]

    if len(lst) == 0:
        return (None, None)

    shortest = lst[0]
    longest = ''

    for word in lst:
        if len(word) < len(shortest):
            shortest = word
        if len(word) > len(longest):
            longest = word

    if shortest == '':
        shortest = None
    if longest == '':
        longest = None

    return (shortest, longest)
