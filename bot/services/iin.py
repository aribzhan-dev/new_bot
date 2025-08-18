from datetime import datetime

def check_iin(iin: str) -> bool:
    # 1) Проверка длины и формата
    if not (iin.isdigit() and len(iin) == 12):
        return False

    # 2) Проверка даты рождения
    year = int(iin[0:2])
    month = int(iin[2:4])
    day = int(iin[4:6])
    century_gender = int(iin[6])

    if century_gender in (1, 2):
        year += 1800
    elif century_gender in (3, 4):
        year += 1900
    elif century_gender in (5, 6):
        year += 2000
    else:
        return False

    try:
        datetime(year, month, day)  # Проверка существования даты
    except ValueError:
        return False

    # 3) Контрольная сумма
    digits = [int(x) for x in iin]
    weights1 = range(1, 12)  # 1..11
    checksum = sum(d * w for d, w in zip(digits[:11], weights1)) % 11

    if checksum == 10:
        weights2 = range(3, 14)  # 3..13
        checksum = sum(d * w for d, w in zip(digits[:11], weights2)) % 11

    return checksum == digits[11]


