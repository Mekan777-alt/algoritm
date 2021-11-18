"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"]

users = int(input("Введите номер буквы: "))
if users <= 26:
    users -= 1
    a = alphabet.pop(users)
    print(a)
else:
    print("error")
