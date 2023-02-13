# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.

list_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
list_2 = ['D', 'G']
list_3 = ['B', 'C', 'M', 'P']
list_4 = ['F', 'H', 'V', 'W', 'Y']
list_5 = ['K']
list_6 = ['J', 'X']
list_7 = ['Q', 'Z']
counter = 0

my_list = []
my_str = 'BOOK'

for i in my_str:
    my_list.append(i)
print(my_list)

for i in range(len(list_1)):
    for item in my_list:
        if item == list_1[i]:
            counter += 1
for i in range(len(list_2)):
    for item in my_list:
        if item == list_2[i]:
            counter += 2
for i in range(len(list_3)):
    for item in my_list:
        if item == list_3[i]:
            counter += 3
for i in range(len(list_4)):
    for item in my_list:
        if item == list_4[i]:
            counter += 4
for i in range(len(list_5)):
    for item in my_list:
        if item == list_5[i]:
            counter += 5
for i in range(len(list_6)):
    for item in my_list:
        if item == list_6[i]:
            counter += 6
for i in range(len(list_7)):
    for item in my_list:
        if item == list_7[i]:
            counter += 7

print(f'Стоимость слова = {counter}')