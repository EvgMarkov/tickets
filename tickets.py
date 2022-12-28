n = int(input('Введите количество билетов\n'))

cost = []
for i in range(n):
    print('Введите возраст покупателя билета №', i + 1)
    age = int(input())
    if (age < 18):
        cost.append(0)
    elif (18 <= age < 25):
        cost.append(990)
    else:
        cost.append(1390)

totalCost = 0
for i in range(n):
    totalCost += cost[i]

if (n > 3):
    totalCost = totalCost * 0.9

print('Сумма к оплате: ', totalCost)


