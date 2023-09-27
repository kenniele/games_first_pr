def score(field):
    pass
def game():
    while True:
        field = [["." for _ in range(5)] for _ in range(4)]
        for i in range(20):
            cur_sign = "П" if i % 2 == 0 else "В"
            coor = input("Введите координаты x, y через пробел (от 0 до 9). Следите за тем, чтобы клетка с такими координатами не была занята: ")
            pass