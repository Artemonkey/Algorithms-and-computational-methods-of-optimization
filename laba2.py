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

# tab_2 = {
#     40: [(4, 40), (4, 0), (6, 40), (8, 40)], 
#     80: [(6, 80), (7, 40), (10, 40), (14, 40)], 
#    120: [(8, 120), (9, 40), (13, 40), (18, 40)], 
#    160: [(13, 160), (13, 0), (16, 80), (21, 40)], 
#    200: [(16, 200), (18, 200), (19, 40), (24, 40)]
# }
tab_2 = {}

# tab_3 = [
#     {
#         40: {
#             0: 4, 
#             40: 3
#         }, 
#         80: {
#             0: 6, 
#             40: 7,
#             80: 4
#         }
#     },
#     {},
#     {}
# ]
tab_3 = []


# Преобразование второй таблицы
ksi_list = [i for i in range(step, ksi_0 + 1, step)]
for i in range(n):
    for ksi in ksi_list:
        if i == 0:
            tab_2[ksi] = [(f[ksi][n - 1], ksi)]
            continue
        key = max(tab_3[i - 1][ksi], key=tab_3[i - 1][ksi].get)
        tab_2[ksi].append((tab_3[i - 1][ksi][key], key))

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

print(tab_2)
print("max_profit:", max_profit)
print(funds_distirbution)
