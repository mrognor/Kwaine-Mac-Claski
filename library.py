#  Функция для получения координат вершин
def interpret_matrix(localmas):
    newmas = []
    for i in range(len(localmas)):
        for j in range(len(localmas)):
            if localmas[i][j] != "0":

                localmas[i][j] = ("0" * (len(localmas)//2 - len(str(bin(int(i)))[2::]))) + str(bin(int(i)))[2::]\
                                 + ("0" * (len(localmas)//2 - len(str(bin(int(j)))[2::]))) + str(bin(int(j)))[2::]
                newmas.append(localmas[i][j])
    return newmas

# Функция для склейки прямо как в методе Квайна
def concat(str1, str2):
    newstr = ""
    for i in range(len(str1)):
        if (str1[i] == "-" and str2[i] != "-") or (str2[i] == "-" and str1[i] != "-"):
            return "false"

        if str1[i] != str2[i]:
            newstr += "-"
        else:
            newstr += str1[i]

    if newstr.count("-") == str1.count("-")+1 and newstr.count("-") == str2.count("-")+1:
        # print("Yes", str1, str2, newstr)
        return newstr
    else:
        # print("No", str1, str2, newstr)
        return "false"

# Функция которая делает одну склейку по методу Квайна
def progon(localmas):
    newmas = []
    usedmas = []

    for i in range(len(localmas)):
        for j in range(i, len(localmas)):
            tmp = concat(localmas[i], localmas[j])
            if tmp != "false" and tmp not in newmas:
                newmas.append(tmp)

            if tmp != "false":
                if localmas[i] not in usedmas:
                    usedmas.append(localmas[i])
                if localmas[j] not in usedmas:
                    usedmas.append(localmas[j])

    tmpmas = []
    for i in localmas:
        if i not in usedmas:
            tmpmas.append(i)

    return newmas + tmpmas


# Функция для проверки принадлежности вершины носителю
def is_vershin_in_nos(vershina, nositel):

    for i in range(len(vershina)):
        if (vershina[i] == "1" and nositel[i] == "0") or (vershina[i] == "0" and nositel[i] == "1"):
            return False
    return True

# print(concat("-10", "1-0"))
