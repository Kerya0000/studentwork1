#Приветствие
print("Добро пожаловать в игру крестики-нолики.\n"
      "Ваша задача - выстроить подряд три крестика.\n"
      "Победа также будет засчитана, если крестики выставлены по диагонали\n"
      "Координаты нужно вводить через запятую без пробелов\n"
      "Сначала вводится ордината 'y', затем абсцисса 'x'\n"
      "Вводить координаты уже занятой крестиком или ноликом клетки нельзя\n"
      "Удачи!")

print("------------------------------------------------")
#Скелет поля для игры
a, b, c, d, e, f, g, h, i = "-","-","-","-","-","-","-","-","-"


#Игровая логика
count = 0

while count <= 9:
    #Ход первого игрока
    Player1 = input("Введите координаты для крестика:")
    if Player1 == "1,1":
        a = "x"
    elif Player1 == "1,2":
        b = "x"
    elif Player1 == "1,3":
        c = "x"
    elif Player1 == "2,1":
        d = "x"
    elif Player1 == "2,2":
        e = "x"
    elif Player1 == "2,3":
        f = "x"
    elif Player1 == "3,1":
        g = "x"
    elif Player1 == "3,2":
        h = "x"
    elif Player1 == "3,3":
        i = "x"

    count += 1

    print(f"  1 2 3")
    print(f"1 {a} {b} {c}")
    print(f"2 {d} {e} {f}")
    print(f"3 {g} {h} {i}")
    #Условия победы первого игрока
    if a == "x" and b == "x" and c == "x":
        print("Победил первый игрок")
        break
    elif d == "x" and e == "x" and f == "x":
        print("Победил первый игрок")
        break
    elif g == "x" and h == "x" and i == "x":
        print("Победил первый игрок")
        break
    elif a == "x" and e == "x" and i == "x":
        print("Победил первый игрок")
        break
    elif a == "x" and d == "x" and g == "x":
        print("Победил первый игрок")
        break
    elif b == "x" and e == "x" and h == "x":
        print("Победил первый игрок")
        break
    elif c == "x" and f == "x" and i == "x":
        print("Победил первый игрок")
        break

    #Ход второго игрока
    Player2 = input("Введите координаты для нолика:")

    if Player2 == "1,1":
        a = "0"
    elif Player2 == "1,2":
        b = "0"
    elif Player2 == "1,3":
        c = "0"
    elif Player2 == "2,1":
        d = "0"
    elif Player2 == "2,2":
        e = "0"
    elif Player2 == "2,3":
        f = "0"
    elif Player2 == "3,1":
        g = "0"
    elif Player2 == "3,2":
        h = "0"
    elif Player2 == "3,3":
        i = "0"

    count += 1

    print(f"  1 2 3")
    print(f"1 {a} {b} {c}")
    print(f"2 {d} {e} {f}")
    print(f"3 {g} {h} {i}")

    # Условия победы второго игрока
    if a == "0" and b == "0" and c == "0":
        print("Победил второй игрок")
        break
    elif d == "0" and e == "0" and f == "0":
        print("Победил второй игрок")
        break
    elif g == "0" and h == "0" and i == "0":
        print("Победил второй игрок")
        break
    elif a == "0" and e == "0" and i == "0":
        print("Победил второй игрок")
        break
    elif a == "0" and d == "0" and g == "0":
        print("Победил второй игрок")
        break
    elif b == "0" and e == "0" and h == "0":
        print("Победил второй игрок")
        break
    elif c == "0" and f == "0" and i == "0":
        print("Победил второй игрок")
        break

print("Игра окончена")
