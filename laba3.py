ksi_0 = int(input())
n = int(input())
step = 1
f = {
    1: [5, 7, 6],
    2: [9, 9, 10],
    3: [12, 11, 13],
    4: [14, 13, 15],
    5: [15, 16, 16],
    6: [18, 19, 18],
    7: [20, 21, 21],
    8: [24, 22, 22],
    9: [27, 25, 25]
} # представляет из себя таблицу 1 для 6 задачи;

# f = {
#     1: [5, 7, 6],
#     2: [9, 9, 10],
#     3: [12, 11, 13],
#     4: [14, 13, 15],
#     5: [15, 16, 16],
#     6: [18, 19, 18],
#     7: [20, 21, 21],
#     8: [24, 22, 22],
#     9: [27, 25, 25],
#     10: [30, 28, 26],
#     11: [34, 35, 29],
#     12: [38, 40, 33],
# } # представляет из себя таблицу 1 для 7 задачи

f_len = len(f[1])

tab_2 = {} # таблица 2(основная)

tab_3 = [] # таблица 3(вспомогательная)

ksi_list = [i for i in range(step, ksi_0 + 1, step)]

x_k = [] # таблица параметров
for i in range(1, len(ksi_list) + 1):
    x_k.append([])
    for i_1 in range(i + 1):
        x_k[i - 1].append(i_1 * step)

ksi_k = [] # таблица вложений
for i in range(len(ksi_list)):
    ksi_k.append(x_k[i][::-1])

for i in range(n - 1):
    tab_3.append({x: {} for x in ksi_list})

for i in range(n - 1):
    for i_1 in range(len(ksi_list) + 1):
        if i_1 >= len(ksi_list):
            continue
        a = 0
        for i_2 in range(i_1 + 2):
            current_x_k = x_k[len(x_k) - 1][i_2]
            current_ksi_k = ksi_k[i_1][i_2]
            if i == 0 and current_ksi_k > max(f):
                tab_3[i][(i_1 + 1) * step].update({current_x_k: 0})
                continue
            if i_2 == 0:
                f_x = 0
            elif current_x_k in f.keys():
                f_x = f[current_x_k][f_len - i - 2]
            else:
                f_x = 0
            if i_2 == i_1 + 1:
                Z_ksi = 0
            else:
                if i > 0:
                    if i_2 == 0:
                        key = max(tab_3[i - 1][(i_1 + 1) * step], 
                                  key=tab_3[i - 1][(i_1 + 1) * step].get)
                        Z_ksi = tab_3[i - 1][(i_1 + 1) * step][key]
                    else:
                        if i_2 == 1:
                            Z_ksi = tab_3[i][(i_1) * step][(i_2 - 1) * step]
                        else:
                            Z_ksi = tab_3[i][(i_1) * step][(i_2 - 1) * step] - \
                            f[x_k[len(x_k) - 1][i_2 - 1]][f_len - i - 2]
                else:
                    if current_ksi_k > max(f):
                        Z_ksi = tab_3[i][(i_1) * step][(i_2) * step]
                    else:
                        Z_ksi = f[current_ksi_k][-a - 1]
            tab_3[i][(i_1 + 1) * step].update({current_x_k: f_x + Z_ksi})
        a += 1

# Преобразование второй таблицы
for i in range(n):
    for ksi in ksi_list:
        if i == 0:
            tab_2[ksi] = [(f[ksi][n - 1], ksi)] if ksi in f else [(0, 0)]
            continue
        key = max(tab_3[i - 1][ksi], key=tab_3[i - 1][ksi].get)
        tab_2[ksi].append((tab_3[i - 1][ksi][key], key))

print(tab_2)
# Получение ответа
max_profit = tab_2[ksi_0][n - 1][0]
funds_distirbution = []

funds_remain = ksi_0
for i in range(n - 1, -1, -1):
    value = tab_2[funds_remain][i][1]
    funds_distirbution.append(value)

    funds_remain -= value
    if funds_remain == 0:
        break

print("max_profit:", max_profit)
print(funds_distirbution)