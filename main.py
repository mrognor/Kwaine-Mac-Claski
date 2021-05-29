from math import sqrt
import library
import DecartovoProisvedenie

#  Задаем строку функции и определяем размерность матрицы
print("Введите вашу функцию")  # Выводим подсказку в консоль
func = input()  # Вводим с клавиатуры значение в переменную func. Там будет хранится двоичное представление нашей функции
matrix_size = int(sqrt(len(func)))  # Определяем размерность матрицы(только для красивого вывода на экран)

#  Проверяем на возмжность работы с функцией
if str(bin(len(func)))[2::].count("1") != 1:  # Проверяем на то что количество элементов это степень двойки
    print("Нельзя для данной функции")
    exit(0)  # Генерируем выход из программы

#  Задаем массив функции(только для красивого вывода на экран)
funcmas = [["0" for i in range(matrix_size)] for j in range(matrix_size)]
for i in range(matrix_size):
    for j in range(matrix_size):
        funcmas[i][j] = func[i*matrix_size + j]

#  Выводим исходную матрицу(красивый вывод на экран)
print("Ваша матрица")
for i in range(matrix_size):
    for j in range(matrix_size):
        print(funcmas[i][j], end="")
    print()

#  Выводим матрицу координат. Тут я выведу координаты всех едениц
print("Координаты матрицы")
mas_vershin = library.interpret_matrix(funcmas)  # Присваиваю массиву результат работы функции из второго файла
for i in range(matrix_size):  # Вывод на экран координат всех вершин вместе с нулями
    for j in range(matrix_size):
        print(funcmas[i][j], end=" ")
    print()

#  Выводим координаты носителей
print("Координаты носителей")
print(mas_vershin)

# Этот код ищет максимальные интервалы
mas_to_sravn = []
mas_nositel = mas_vershin

while mas_to_sravn != mas_nositel:
    mas_to_sravn = mas_nositel
    mas_nositel = library.progon(mas_nositel)  # тут вызывается функция из другого файла

#  Выводим максимальные интервалы
print("Максимальные интервалы")
print(mas_nositel)

# этот блок кода ищет максимальные интервалы
cores = []
for i in mas_vershin:
    count = 0
    tmp_nos = ""
    for j in mas_nositel:
        if library.is_vershin_in_nos(i, j):  # Функция из соседнего файла, проверяет принадлежность вершины носителю
            count += 1
            tmp_nos = j

    if count == 1 and tmp_nos not in cores:
        cores.append(tmp_nos)

# Выводим все ядровые интервалы
print("Ядровые интервалы")
print(cores)

#  Закидываем все не ядровые в массив
no_cores = []
for i in mas_nositel:
    if i not in cores:
        no_cores.append(i)

# Выводим все не ядровые интервалы
print("Не ядровые интервалы")
print(no_cores)

# Формируем строку для метода Патрика
patric_str = ""
for i in mas_vershin:
    flag = True
    flag2 = True
    for p in cores:
        if library.is_vershin_in_nos(i, p):
            flag2 = False

    for j in no_cores:
        if library.is_vershin_in_nos(i, j):
            if flag and flag2:
                patric_str += "Vershina:" + i + " "
                flag = False
            if flag2:
                patric_str += j + " "


print(patric_str)

patric_mass_tmp = patric_str.split("Vershina:")
patric_mass = []

for i in patric_mass_tmp:
    if i != "":
        patric_mass.append(i[5:len(i)-1].split(" "))

print("Массив Патрика")
print(patric_mass)
print("Перебор по методу Патрика")
lastmas = DecartovoProisvedenie.MakePatricMass(patric_mass)
print(lastmas)

# 1100110000010101
# 1010111110100111
