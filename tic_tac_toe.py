def check_winner(field):
    main_d, sec_d = [], []
    for i in range(len(field)):
        cur_col = []
        if len(set(field[i])) == 1:
            return field[i][0]
        for j in range(len(field[i])):
            main_d.append(field[i][j]) if i == j else None
            sec_d.append(field[i][len(field) - j - 1]) if i == len(field) - j - 1 else None
            cur_col.append(field[j][i])
        if len(set(cur_col)) == 1:
            return cur_col[0]
    return main_d[1] if len(set(main_d)) == 1 or len(set(sec_d)) == 1 else False
def create_field():
    field = []
    count = 1
    for i in range(3):
        field.append([])
        for j in range(3):
            field[i].append(count)
            count += 1
    return field
def check_coor(field, coor):
    coor = int(coor)
    for i in range(len(field)):
        if coor in field[i]:
            return True
    return False
def game():
    while True:
        field = create_field()
        for c in range(9):
            print("\n" * 50)
            print("Добро пожаловать в игру Крестики-Нолики!", end="\n" * 2) if c == 0 else None
            for k in range(len(field)):
                print(*field[k], sep=" | ")
                print("-" * 9)
            cur_sign = "X" if c % 2 == 0 else "O"
            print(f"Ход игрока {cur_sign}!")
            coor = input("Введите координаты точки на поле (доступное число от 1 до 9): ")
            while (not coor.isdigit()) or (not check_coor(field, coor)):
                coor = input("Введите координаты еще раз! ")
            coor = int(coor)
            Flag = False
            for k in range(len(field)):
                for j in range(len(field[k])):
                    if field[k][j] == coor:
                        field[k][j] = cur_sign
                        Flag = True
                        break
                if Flag:
                    break
            if check_winner(field):
                print(f"Выиграл игрок, который ставил {check_winner(field)}")
                break
            elif c == 8:
                print("Ничья!")
        game_again = input("Хотите сыграть еще раз? (+/-) ")
        while game_again not in "+-":
            game_again = input("Введите + или - ")
        if game_again == "-":
            print("До свидания, удачного дня!")
            break
game()