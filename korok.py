lista = []


def kor_beker():
    i = 0
    szoveg = ""
    print("Adj meg 5 egész számot 0 és 120 között:")
    lista.append(int(input("1.szám: ")))
    lista.append(int(input("2.szám: ")))
    lista.append(int(input("3.szám: ")))
    lista.append(int(input("4.szám: ")))
    lista.append(int(input("5.szám: ")))
    while i < len(lista):
        if i == len(lista) - 1:
            szoveg += str(lista[i])
        else:
            szoveg += str(lista[i]) + " : "
        i += 1
    print(f"II/A, B, C:\n\t{szoveg}")
    elso_idos()


def elso_idos():
    i = 0
    kor_index = 0
    while i < len(lista):
        if lista[i] > 70:
            kor_index = i + 1
        i += 1
    return kor_index


def konzolra_ir(kor_index):
    return f"II/D, E:\n\tElső idős ember korának helye a listában: {kor_index}"


def fajl_ir():
    print("II/F:")
    fajl = open("oreg.txt", "w", encoding="UTF-8")
    fajl.write(f"II/D, E:\n\tElső idős ember korának helye a listában: {kor_index}")
    fajl.close()
