# -*- coding: utf-8 -*-
"""
Задана строка S и символ С. За один ход можно поменять местами два соседних символа. Сколько потребуется ходов чтобы переместить все символы С в строке в начало строки, не меняя при этом порядок следования между остальным символами.

Например, имеется строка abcabcabc, и задан символ b. После перемещения всех символов b в начало строки, получится строка 
bbbacacac, на это уйдёт 9 ходов, ниже указаны строки получившиеся после кажого хода.
1. bacabcabc

2. bacbacabc

3. batcacabe

4. bbacacabc

5. bbacacbac

6. bbacabcac 

7. bbacbacac

8. bbabcacac 

9. bbbacacac
Входные данные

Задана строка 5, состоящая из прописных бука латинского алфавита, и символ С через пробел. Длина строки не превышает 100 символов. Гарантируется, что символ С встречается в строке 5.

Выходные данные

Выведите единственное числе количество ходов, которое потребуется, чтобы переместить все символы с начало строки

Примеры

входные данные

аbrahcabe b

выходные данные
9


@author: workk
"""
def count_moves(s, c):
    moves = 0
    c_count = 0
    current_c_cont = 0

    for char in s :
        if char == c:
            c_count += 1
            moves += current_c_conut
        else:
            current_c_count += 1
            return moves 
        input_str, target_char = input().split()
        moves_required = count_moves(input_str, target_char)
print ( moves_required )
