import random
def generate_field():
    chips_q = random.randint(6, 32)
    field = [1 for _ in range(chips_q)]
    for _ in range(64 - chips_q):
        field.append(".")
    random.shuffle(field)
    fin_field = []
    for i in range(8):
        fin_field.append([])
        for j in range(8):
            fin_field[i].append(field[i + j * 8])
    return fin_field
def get_coord(player, type):
    mes = input(f"Ходит {player} игрок. Введите номер строки или столбца (пример: строка 1, столбец 5) ")
    while mes.count(" ") != 1 or mes.split()[0].lower() not in ["строка", "столбец"] or (not mes.split()[1].isdigit()) or (not (1 <= int(mes.split()[1]) <= 8)):
        mes = input("Введите корректную команду! ")
    return mes.split()[0].lower(), int(mes.split()[1]) - 1
def rec(field, type, num):
    temp = [field[num][i] for i in range(8)] if type == 0 else [field[i][num] for i in range(8)]
    while temp.count(".") == 8:
        type, num = get_coord(1, 1)
        temp = [field[num][i] for i in range(8)] if type == 0 else [field[i][num] for i in range(8)]
    return type, num
def erase(field, type, num):
    type, num = rec(field, type, num)
    if type == 0:
        for i in range(len(field)):
            field[num][i] = "."
    else:
        for i in range(len(field)):
            field[i][num] = "."
    return field
def check_win(field):
    for i in range(len(field)):
        if 1 in field[i]:
            return False
    return True
def game():
    while True:
        field = generate_field()
        for i in range(16):
            player = "первый" if i % 2 == 0 else "второй"
            print("\n" * 50)
            print("Добро пожаловать в игру СуперНим!", end="\n" * 2) if i == 0 else None
            for i in range(len(field)):
                print(*field[i])
            mes = get_coord(player, 0)
            type = 0 if mes[0] == "строка" else 1
            num = mes[1]
            field = erase(field, type, num)
            if check_win(field):
                print(f"Победил {player} игрок!")
                break
        game_again = input("Хотите продолжить? Введите + или - ")
        while game_again not in "+-":
            game_again = input("Введите + или - ")
        if game_again == "-":
            break
game()