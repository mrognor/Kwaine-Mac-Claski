def backend(mas):
    bmax = len(mas)
    mmax = len(mas[0])

    for i in mas:
        if len(i) > mmax:
            mmax = len(i)

    if bmax > mmax:
        max = bmax
    else:
        max = mmax

    if len(mas) < max:

        while len(mas) < max:
            mas.append(["ptr1" for i in range(max)])

    for i in mas:
        if len(i) < max:
            while len(i) < max:
                i.append("ptr2")


def MakePatricMass(mass):
    backend(mass)

    n = len(mass[0])
    newmas = [[] for i in range(n)]
    patricmas = []

    for i in range(n):  # Проход по всем массивам
        for k in range((n ** i)):  # Печатаем наюор элементов несколько раз
            for j in range(n):  # Проход по внутренности массива
                for p in range(n ** (n - i - 1)):
                    # print(mas[i][j])
                    newmas[i].append(mass[i][j])

    for i in range(len(newmas[0])):
        str = ""
        for j in range(len(newmas)):
            if newmas[j][i] != "ptr1" and newmas[j][i] not in str:
                str += newmas[j][i]
                str += " "
            # print(newmas[j][i], end=" ")
        if "ptr2" not in str and str not in patricmas:
            patricmas.append(str)

    return patricmas
    # print()
