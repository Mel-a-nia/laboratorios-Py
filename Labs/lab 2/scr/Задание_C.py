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
