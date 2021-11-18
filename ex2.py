'''
Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
Объяснить полученный результат.
'''

x = 5
y = 6

print(f"Результат логических побитовых операции 'И' = {bin(x & y)}, и 'ИЛИ' = {bin(x | y)} "
      f"\nБитовый оператор ~ (инверсия) = {bin(~x)}, {bin(~y)}"
      f"\nБитовый оператор ^ (исключающее ИЛИ, XOR) = {bin(x ^ y)}"
      f"\nРезультат над числом 5 побитовый сдвиг вправо на два знака = {bin(x >> 2)}"
      f"\nРезультат над числом 5 побитовый сдвиг влева на два знака = {bin(x << 2)}")

"""
Операторы сдвига влево << и сдвига вправо >> сдвигают каждый бит на одну или несколько позиций влево или вправо
Каждый бит сдвигается влево или на правно, при этом в конце сдвига добавляется 0
"""



