def task_a():
    list_1 = [i for i in range(0, 100, 10)]
    list_2 = [i for i in range(0, 100, 10)]
    return list_1, list_2

def task_b(list_1):
    print(f"Второй элемент первого списка: {list_1[1]}\n")

def task_c(list_2):
    list_2[len(list_2) - 1] = 200
    print("Второй список после присвоения последнему элементу значения 200:")
    for i in list_2:
        print(i)

def task_d(list_1, list_2):
    list_full = list_1+list_2
    print("Объединённый список:")
    for i in list_full:
        print(i)
    return list_full

def task_e (list_full):
    list_new = list_full[1::2]
    print("Срез объединённого списка:")
    for i in list_new:
        print(i)
    return list_new

def task_f(list_new):
    print("Новый список с элементами '13' и '666'")
    list_new.append(13)
    list_new.append(666)
    for i in list_new:
        print(i)
    return list_new

def task_g(list_full):
    print("Минимальный элемент объединённого списка:", min(list_full))
    print("Максимальный элемент объединённого списка:", max(list_full))

def main():
    list_1, list_2 = task_a()
    task_b(list_1)
    task_c(list_2)
    list_full = task_d(list_1, list_2)
    list_new = task_e(list_full)
    task_f(list_new)
    task_g(list_full)

if __name__ == '__main__':
    main()