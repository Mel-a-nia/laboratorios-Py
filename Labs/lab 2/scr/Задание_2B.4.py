from typing import List, Union

Number = Union[int, float]


def _check_rectangular(mat: List[List[Number]]) -> None:
    if not mat:
        return
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError("рваная матрица")


def transpose(mat: List[List[Number]]) -> List[List[Number]]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]


def row_sums(mat: List[List[Number]]) -> List[float]:
    _check_rectangular(mat)
    return [float(sum(row)) for row in mat]


def col_sums(mat: List[List[Number]]) -> List[float]:
    _check_rectangular(mat)
    if not mat:
        return []
    return [float(sum(mat[i][j] for i in range(len(mat)))) for j in range(len(mat[0]))]


print(col_sums([[1, 2], [3]]))
