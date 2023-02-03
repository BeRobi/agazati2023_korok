import random


def vel_szam():
    szam = int(random.random() * 50 + 1)
    print(f"I/A:\n\tA generált szám: {szam}")
    oszthato(szam)


def oszthato(szam):
    print("I/B:")
    if szam % 5 == 0:
        print(f"\tA szám öttel osztható!")
    elif szam % 3 == 0:
        print(f"\tA szám hárommal osztható!")
    elif szam % 5 == 0 and szam % 3 == 0:
        print(f"\tA szám öttel és hárommal is osztható!")

