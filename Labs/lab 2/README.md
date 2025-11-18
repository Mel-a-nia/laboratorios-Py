# python-labs

## Лабораторная работa 2

### Задание 1.1

<img width="1434" height="1280" alt="foto_1 1" src="https://github.com/user-attachments/assets/e550a874-8dd4-4329-a58c-e9000669540f" />

```
def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, (tuple, list)) or len(rec) != 3:
        raise ValueError("rec debe contener (fio, group, gpa)")
    fio, group, gpa = rec
    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("fio y group deben ser str")
    if not isinstance(gpa, (int, float)):
        raise TypeError("gpa debe ser numérico")
    fio = " ".join(fio.split())
    group = group.strip()
    if not fio or not group:
        raise ValueError("fio y group no pueden estar vacíos")
    parts = fio.split()
    if len(parts) < 2:
        raise ValueError("fio debe contener фамилию и имя")
    surname = parts[0].capitalize()
    initials = "".join(n[0].upper() + "." for n in parts[1:3])
    gpa_str = f"{float(gpa):.2f}"
    return f"{surname} {initials}, гр. {group}, GPA {gpa_str}"
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("сидорова анна сергеевна", "ABB-01", 3.999)))

```

<img width="1227" height="376" alt="foto_1 1_resultado" src="https://github.com/user-attachments/assets/0a764ac3-4114-42da-bd96-6dda77053cb0" />


### Задание1.2

<img width="1434" height="824" alt="foto_1 2" src="https://github.com/user-attachments/assets/f7ba6531-f2ab-47a5-85d7-2f8556de70eb" />


```
def min_max(nums: list [float | int])-> tuple [float | int, float | int]:
    if not nums: 
        raise ValueError ("пустой список")
    return(min(nums), max(nums))
def unique_sorted (nums:list [float | int])-> list [float | int]:
    return sorted(set(nums))
def flatten(mat:list[list | tuple])-> list:
    result=[]
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("строка не является ни списком, ни кортежем")
        result.extend(row)
    return result 
print(min_max([]))

```

<img width="906" height="165" alt="foto_1 2_resultado" src="https://github.com/user-attachments/assets/cc62fde5-06cb-4c56-9f79-0531e9b28f21" />

### Задание 2b.1

<img width="1650" height="1508" alt="foto_2B 1" src="https://github.com/user-attachments/assets/6068d8e8-6a81-44a5-b00e-3713c1784175" />


```
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
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))

```
<img width="1142" height="167" alt="foto_2B 1_resultado" src="https://github.com/user-attachments/assets/2269842e-e4fe-4492-b082-866365066d87" />


### Задание 2b.2

<img width="1650" height="1166" alt="foto_2B 2" src="https://github.com/user-attachments/assets/e22654e7-7544-4e19-95ac-2659bdaf598e" />


```
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
print(transpose([[1, 2], [3]]))

```

<img width="1118" height="160" alt="foto_2B 2_resultado" src="https://github.com/user-attachments/assets/ae9ca82e-f8ae-48d5-8ae9-2cbdc9b98bc0" />


### Задание 2b.3

<img width="1650" height="1166" alt="foto_2B 3" src="https://github.com/user-attachments/assets/75d5a4e3-32a2-46cd-a5d9-70eab5e7d381" />


```
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
print(row_sums([[1, 2], [3]]))

```

<img width="1120" height="171" alt="foto_2B 3_resultado" src="https://github.com/user-attachments/assets/bdce2fc7-8803-4239-ba8d-a188aa4e6f89" />


### Задание 2b.4

<img width="1650" height="1166" alt="foto_2B 4" src="https://github.com/user-attachments/assets/0bf9bc42-18d5-4915-b02d-018124f23cdf" />


```
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

```
<img width="1220" height="212" alt="foto_2B 4_resultado" src="https://github.com/user-attachments/assets/23de1af4-ee12-4e8d-8af2-8a20f9100e52" />

 
### Задание c

<img width="1326" height="1166" alt="foto_c" src="https://github.com/user-attachments/assets/c6918b07-89d6-4a55-88d9-e0ebf6039f39" />


```
def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, (tuple, list)) or len(rec) != 3:
        raise ValueError("rec debe contener (fio, group, gpa)")
    fio, group, gpa = rec
    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("fio y group deben ser str")
    if not isinstance(gpa, (int, float)):
        raise TypeError("gpa debe ser numérico")
    fio = " ".join(fio.split())
    group = group.strip()
    if not fio or not group:
        raise ValueError("fio y group no pueden estar vacíos")
    parts = fio.split()
    if len(parts) < 2:
        raise ValueError("fio debe contener фамилию и имя")
    surname = parts[0].capitalize()
    initials = "".join(n[0].upper() + "." for n in parts[1:3])
    gpa_str = f"{float(gpa):.2f}"
    return f"{surname} {initials}, гр. {group}, GPA {gpa_str}"
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("сидорова анна сергеевна", "ABB-01", 3.999)))
```
<img width="1376" height="118" alt="foto_c_resultado" src="https://github.com/user-attachments/assets/3715fe59-1db5-4fa0-a456-ef2e4a078720" />



