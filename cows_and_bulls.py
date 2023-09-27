def check_number(n):
    while any([not x.isdigit() for x in n]) or len(n) != 4:
        n = input("Введите валидное число! ")
    return n
while True:    
    guessed = input("Введите четырехзначное число (можно со значащими нулями), которое хотите загадать (попросите, чтобы второй игрок отвернулся): ")
    guessed = check_number(guessed)
    cur = ""
    count = 0
    while guessed != cur:
        count += 1
        cows, bulls = 0, 0
        cur = input("Введите число: ")
        cur = check_number(cur)
        for i in range(len(cur)):
            if cur[i] == guessed[i]:
                bulls += 1
            elif cur[i] in guessed:
                cows += 1
        print(f"Количество коров: {cows}.", f"Количество быков: {bulls}.", sep="\n")
    print(f"Игра закончена! Количество понадобившихся попыток: {count}.")
    f = input("Хотите сыграть еще раз? (+/-): ")
    while f not in "+-":
        a = input("Введите + или -: ")
    if a == "-":
        break