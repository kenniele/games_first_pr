from random import shuffle
def get_field():
    field = [["."] * 4 for _ in range(4)]
    while not check_field(field):
        temp = list(range(1, 16))
        temp.append(".")
        shuffle(temp)
        j = 0
        for k in range(4):
            for m in range(4):
                field[k][m] = temp[j]
                j += 1
    return field
def check_field(field):
    k = 0
    if sum([x.count(".") for x in field]) > 1:
        return False
    for i in range(4):
        temp = [x for x in field[i] if x != "."]
        for j in range(1, len(temp)):
            if temp[j - 1] > temp[j]:
                k += 1
    return k % 2 == 0
def step(field, num):
    x, y = 0, 0
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == num:
                x, y = i, j
    xe, ye = -1, -1
    for i in range(x - 1 if x - 1 >= 0 else 0, x + 2 if x + 2 <= 4 else 4):
        for j in range(y - 1 if y - 1 >= 0 else 0, y + 2 if y + 2 <= 4 else 4):
            if field[i][j] == ".":
                xe, ye = i, j
                break
        if xe != -1 and ye != -1:
            break
    if xe == -1 and ye == -1:
        return False
    field[x][y], field[xe][ye] = ".", num
    return field
def check_win(field):
    n = 0
    if field[3][3] != ".":
        return False
    for i in range(len(field)):
        for j in range(len(field[i])):
            if n == 15:
                break
            if field[i][j] - n == 1:
                n = field[i][j]
            else:
                return False
    return True
def game():
    playing = True
    while playing:
        field = get_field()
        while True:
            for i in range(len(field)):
                for j in range(len(field[i])):
                    print(str(field[i][j]).ljust(3), end="")
                print()
            num = input("Введите число от 1 до 15 чтобы походить: ")
            while not(num.isdigit()) or (not(1 <= int(num) <= 15)):
                num = input("Введите валидное число: ")
            temp_field = step(field, int(num))
            while not temp_field:
                num = input("Введите число, которое стоит рядом с точкой! ")
                temp_field = step(field, int(num))
            field = temp_field
            if check_win(field):
                print("Игра закончена")
                break
        game_again = input("Хотите сыграть еще? +/- ")
        while game_again not in "+-":
            game_again = input("Введите валидный знак! ")
        if game_again == "-":
            playing = False
game()