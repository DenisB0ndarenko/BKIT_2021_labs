from enum import Enum

# Токент бота
TOKEN = "5084251495:AAGvFx_LRatbRHFGi68RI-dHZCyPb0QtwUs"

# Файл базы данных Vedis
db_file = "db.vdb"

# Матрицы для знаков зодиака
love_comp = [[True, False, False, False],
             [False, True, False, True],
             [False, False, False, True],
             [False, True, False, False]]

work_comp = [[True, False, True, False],
             [True, True, True, False],
             [False, False, True, True],
             [True, False, False, False]]

# Словарь для знаков зодиака
Zodiac = {
    0: "Овен",
    1: "Телец",
    2: "Близнецы",
    3: "Рак"
}


# Функция при полученных знаках и типе отношения
def conclusion(s1, s2, rltn):
    n1 = int(s1)
    n2 = int(s2)
    res = True
    if rltn == 'Любовь':
        res = love_comp[n1][n2]
    elif rltn == 'Работа':
        res = work_comp[n1][n2]
    return res


# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"


# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_FIRST_NUM = "STATE_FIRST_NUM"
    STATE_SECOND_NUM = "STATE_SECOND_NUM"
    STATE_OPERATION = "STATE_OPERATION"
