from random import randint
#функция генерирующая поле для морского боя
def get_field(field):
    for i in range(1, 5): #количество кораблей
        leng = 5 - i #длина корабля
        k = 0 #счетчик для количества кораблей, уже поставленных на поле
        while k != i:
            x, y = randint(0, 9), randint(0, 9) #генератор рандомных координат
            st = [[[x, y]] for _ in range(4)] #для генерации координат кораблей, смотрящих в разные стороны
            for j in range(4): #4 стороны
                cur = st[j]
                for _ in range(leng - 1):
                    x, y = cur[-1][0], cur[-1][1]
                    if j == 0: #вверх
                        cur.append([x - 1, y])
                    elif j == 2: #вниз
                        cur.append([x + 1, y])
                    elif j == 1: #вправо
                        cur.append([x, y + 1])
                    else: #влево
                        cur.append([x, y - 1])
            coord = [] #массив с итоговыми возможными координатами
            for j in range(len(st)):
                cur = st[j]
                flag = True
                for m in cur:
                    x, y = m
                    if (not(0 <= x <= 9)) or (not(0 <= y <= 9)): #если не выходит за границы поля
                        flag = False
                        break
                if flag:
                    coord.append(st[j]) #добавление хороших координат
            for r in range(len(coord)):
                current_coord = coord[r]
                if get_intersect(field, current_coord):
                    new_field = get_intersect(field, current_coord)
                    k += 1
                    break
    for x in range(len(field)):
        for y in range(len(field[x])):
            if field[x][y] == "1":
                field[x][y] = "1".ljust(3)
            else:
                field[x][y] = "0".ljust(3)
    return field
def rebuild():
    coord = input("Введите координаты по типу а8, и1: ") #ввод координат
    d = {"а": 0, "б": 1, "в": 2, "г": 3, "д": 4, "е": 5, "ж": 6, "з": 7, "и": 8, "к": 9} #перевод буквенных координат в числовые
    while (len(coord) != 2) or (not coord[0].isalpha()) or (not coord[1].isdigit()) or (coord[0] not in d.keys()) or not(0 <= int(coord[1]) - 1 <= 9): #если есть какая то ошибка в координатах или введенные координаты неправильны
        coord = input("Введите валидные координаты: ")
    y = d[coord[0]] #перевод буквенной координаты в числовую
    x = int(coord[1]) - 1
    return (x, y)
#функция для определения пересечений с уже существующими кораблями (и для генерации направления )
def get_intersect(field, coord):
    for i in range(len(coord)):
        x, y = coord[i]
        if field[x][y] in "1з": #если попал в запретную зону
            return []
    for i in range(len(coord)):
        x, y = coord[i]
        field[x][y] = "1"
    new_field = get_suffer_zone(field, coord, "1", "з")
    return new_field
#функция для определения защитной зоны (вокруг корабля) по координатам
def get_suffer_zone(field, coord, check, fill):
    for k in coord:
        x_c, y_c = k
        for x in range(x_c - 1, x_c + 2): #два цикла с обходов координат (формально очерчиваем прямоугольником корабль)
            for y in range(y_c - 1, y_c + 2):
                if (0 <= x <= 9) and (0 <= y <= 9) and (field[x][y] != check): #если координаты валидны
                    field[x][y] = fill
    return field
def get_coord(field_admin, x, y, mode="get_coord"):
    hit_arr = ["1".ljust(3), "X".ljust(3)] #массив с кораблями(буквально с координатами их нахождения или попадания)
    cur_row = field_admin[x] #текущая строка
    cur_col = [field_admin[i][y] for i in range(10)] #текущий столбец
    if (0 <= y + 1 <= 9 and cur_row[y + 1] in hit_arr) or (0 <= y - 1 <= 9 and cur_row[y - 1] in hit_arr): #проверяем, горизонтально ли расположен корабль
        m_arr = cur_row #ставим в главный массив строку
        m_c = y #ставим в главную координату- строки
        p_c = x #ставим в доп координату - стоблцы
    elif (0 <= x + 1 <= 9 and cur_col[x + 1] in hit_arr) or (0 <= x - 1 <= 9 and cur_col[x - 1] in hit_arr): #или вертикально
        m_arr = cur_col #ставим в главный массив столбец
        m_c = x #ставим в главную координату - стоблцы
        p_c = y #ставим в доп координату - строки
    elif field_admin[x][y] == "X".ljust(3): #или это вообще одиночный
        return True if mode == "check" else [[x, y]] #возвращаем, что он убит
    res = set()
    for i in range(m_c, m_c + 4 if m_c + 4 <= 10 else 10): #идем вправо или вниз по полю
        if m_arr[i] == "0".ljust(3): #если корабль кончился
            break
        elif m_arr[i] == "1".ljust(3): #если нашлась целая часть
            if mode == "check":
                return False
        elif m_arr[i] == "X".ljust(3):
            res.add((i, p_c)) if p_c == y else res.add((p_c, i))
    for i in range(m_c, m_c - 4 if m_c - 4 >= -1 else -1, -1): #идем влево или вверх по полю
        if m_arr[i] == "0".ljust(3): #если корабль кончился
            break
        elif m_arr[i] == "1".ljust(3): #если нашлась целая часть
            if mode == "check":
                return False
        elif m_arr[i] == "X".ljust(3):
            res.add((i, p_c)) if p_c == y else res.add((p_c, i))
    if mode == "check":
        return True #возвращаем, что все части корабля разрушены
    return sorted(list(res))
#функция для определений попаданий и потоплений кораблей
def hit(field_admin, field_player, x, y):
    while field_player[x][y] != "*".ljust(3):
        print("Эта точка была задействована!")
        x, y = rebuild()
    if field_admin[x][y] == "1".ljust(3): #если x,y ссылается на место в массиве с числом 1 (т.е с частью корабля)
        field_player[x][y] = "X".ljust(3) #ставим на это место на экране пользователя крестик
        field_admin[x][y] = "X".ljust(3)
        if get_coord(field_admin, x, y, "check"): #проверяем, убил или нет
            print("Убил")
            field_player = get_suffer_zone(field_player, get_coord(field_admin, x, y), "", ".".ljust(3)) #обводим точками корабль
        else:
            print("Задел")
    else:
        field_player[x][y] = ".".ljust(3) #если не попал, то ставим точку
        print("Не попал!")
    return [field_admin, field_player]
alph = [x.ljust(3) for x in "абвгдежзик"] #для того чтобы красиво напечаталась верхняя строка
alph.insert(0, "   ") #вставляем пустую строку в начало
def print_field(field):
    global alph
    print(*alph)
    for i in range(len(field)): #печать поля в начале
        print(str(i + 1).ljust(3), end=" ")
        print(*field[i])
#проверка окончания игры(если крестиков 20)
def end_game(field):
    if sum([x.count("X") for x in field]) == 20: #если количество разрушенных частей кораблей равно сумме длин всех кораблей
        return False
    return True
#основная функция, которая запускает игру
def game():
    field_admin = [["0".ljust(3)] * 10 for _ in range(10)] #поле админа, где будет информация о кораблях
    field_admin = get_field(field_admin) #генерация этого поля
    field_player = [["*".ljust(3)] * 10 for _ in range(10)] #поле игрока, заполненное звездами
    print_field(field_player)
    while end_game(field_admin): #пока не разрушены все корабли
        x, y = rebuild()
        print("\n" * 100)
        field_admin, field_player = hit(field_admin, field_player, x, y) #проверка попадания
        for i in range(len(field_admin)): #обновление попаданий для поля игрока
            for j in range(len(field_admin[i])):
                if field_admin[i][j] == "X".ljust(3):
                    field_player[i][j] = "X".ljust(3)
        print_field(field_player)
game()