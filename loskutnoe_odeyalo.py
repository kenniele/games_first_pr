def score(field):
    score_f, score_s = 0, 0
    for i in range(len(field)):
        for j in range(len(field)):
            t = check_neigb(field, i, j)
            if field[i][j] == "П":
                score_f += t
            else:
                score_s += t
    return score_f, score_s
def check_neigb(field, x, y):
    s = 0
    sign = field[x][y]
    for i in range(x - 1 if x - 1 >= 0 else 0, x + 2 if x + 2 <= 10 else 10):
        for j in range(y - 1 if y - 1 >= 0 else 0, y + 2 if y + 2 <= 10 else 10):
            if field[i][j] == sign:
                s -= 1
    return s
def game():
    while True:
        с = 0
        field = [["." for _ in range(5)] for _ in range(4)]
        for i in range(len(field)):
            print(*field[i])
        while sum([x.count(".") for x in field]) != 0:
            cur_sign = "П" if с % 2 == 0 else "В"
            coor = input("Введите номера строки и столбца (куда хотите поставить фишку) через пробел (от 1 до 10). Следите за тем, чтобы клетка с такими координатами не была занята: ")
            while (coor.count(" ") != 1) or (not coor.split()[0].isdigit()) or (not coor.split()[1].isdigit()) or (not (1 <= int(coor.split()[0]) <= 4)) \
                or (not (1 <= int(coor.split()[1]) <= 5)) or (field[int(coor.split()[0]) - 1][int(coor.split()[1]) - 1] != "."):
                coor = input("Введите валидные координаты: ")
            x, y = map(int, coor.split())
            field[x - 1][y - 1] = cur_sign
            for j in range(len(field)):
                print(*field[j])
            с += 1
        score_f, score_s = score(field)
        print("Первый игрок победил!") if score_f > score_s else print("Второй игрок победил!")
        print(f"Количество очков у Первого игрока - {score_f}, у второго - {score_s}")
        game_again = input("Хотите сыграть еще раз? (+/-) ")
        while game_again not in "+-":
            game_again = input("Введие + или - ")
        if game_again == "-":
            break
game()