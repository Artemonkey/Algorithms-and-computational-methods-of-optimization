ksi_0 = int(input())
n = int(input())
step = 40

f = {
    40: [8, 6, 3, 4],
    80: [10, 9, 4, 6],
    120: [11, 11, 7, 8],
    160: [12, 13, 11, 13],
    200: [18, 15, 18, 16]
} # представляет из себя таблицу 1; 

f_len = len(f[40])

tab_2 = {
    40: [(4, 40), (4, 0), (6, 40), (8, 40)], 
    80: [(6, 80), (7, 40), (10, 40), (14, 40)], 
   120: [(8, 120), (9, 40), (13, 40), (18, 40)], 
   160: [(13, 160), (13, 0), (16, 80), (21, 40)], 
   200: [(16, 200), (18, 200), (19, 40), (24, 40)]
} # таблица 2(основная) с примерными данными

tab_3 = [] # таблица 3(вспомогательная)

# ksi_minus_one = [x for x in f.keys()]

x_k = []
for i in range(n + 2):
    if i > 0:
        x_k.append([])
        for i_1 in range(i + 1):
            x_k[i - 1].append(i_1 * step)

ksi_k = []
for i in range(n + 1):
    ksi_k.append(x_k[i][::-1])

for i in range(n - 1):
    tab_3.append({x: {} for x in f.keys()})

for i in range(n - 1):
    for i_1 in range(n + 1):
        a_2 = 0
        for i_2 in range(i_1 + 2):
            current_x_k = x_k[len(x_k) - 1][i_2]
            current_ksi_k = ksi_k[i_1][i_2]
            
            if i_2 == 0:
                f_x = 0
            else:
                f_x = f[current_x_k][f_len-i-2]
            
            if i_2 == i_1 + 1:
                Z_ksi = 0
            else:
                if i > 0:
                    if i_2 == 0:
                        key = max(tab_3[i-1][(i_1 + 1) * step], key=tab_3[i-1][(i_1 + 1) * step].get)
                        Z_ksi = tab_3[i-1][(i_1 + 1) * step][key]
                    else:
                        if i_2 == 1:
                            Z_ksi = tab_3[i][(i_1) * step][(i_2-1) * step]
                        else:
                            Z_ksi = tab_3[i][(i_1) * step][(i_2-1) * step] - f[x_k[len(x_k) - 1][i_2 - 1]][f_len-i-2]
                else:
                    Z_ksi = f[current_ksi_k][-a_2-1]
            
            tab_3[i][(i_1 + 1) * step].update({current_x_k: f_x + Z_ksi})
        a_2 += 1

print(tab_3)