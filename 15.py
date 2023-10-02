from random import shuffle
def get_field():
    field = [["."] * 4 for _ in range(4)]
    while not check_field(field):
        temp = list(range(1, 16))
        j = 0
        for k in range(4):
            for m in range(4):
                if j == len(temp):
                    field[k][m] = "."
                else:
                    field[k][m] = temp[j]
                    j += 1
        shuffle(temp)
    return field
def check_field(field):
    k = 0
    if sum([x.count(".") for x in field]) > 1:
        return False
    for i in range(4):
        for j in range(1, 4):
            if ("." not in [field[i][j - 1], field[i][j]]) and field[i][j - 1] > field[i][j]:
                k += 1
    return k % 2 == 0
def step(field, num):
    x, y = 0, 0
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == num:
                x, y = i, j
    xe, ye = -1, -1
    
    if xe == -1 and ye == -1:
        return False
    field[x][y], field[xe][ye] = ".", num
    return field
def check_win(field):
    n = 0
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] - n == 1:
                n = field[i][j]
            else:
                return False
    return True
def game():
    while True:
        field = get_field()
        for i in range(len(field)):
            print(*field[i])
        num = input("Введите число от 1 до 15 чтобы походить: ")
        while not(num.isdigit()):
            num = input("Введите валидное число: ")
        if check_win(field):
            print("Игра закончена")
game()