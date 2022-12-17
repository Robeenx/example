
def find_median(arr: list[int]) -> int | float:
    """Возвращает среднее значение между центральными элементами списка,
    если в списке четное колличество элементов, иначе медианное значение.
    """

    len_ = len(arr)
    half = len_ // 2
    surp = len_ % 2

    res = sum(sorted(arr)[half - i] for i in range([2, 1][surp])) / [2, 1][surp]

    return int(res) if int(res) == res else res


if __name__ == '__main__':
    data = (
        ([1, 5, 2, 3, 6], 3),
        ([100, 5, 2, 4, 3, 6], 4.5),
    )
    for arr, value in data:
        res = find_median(arr)
        assert res == value
        assert isinstance(res, type(value))
