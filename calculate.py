test_data = [
    {"input1": 1, "input2": 2, "output": 3},
    {"input1": 2, "input2": 3, "output": 5},
    {"input1": 1, "input2": 1, "output": 2},
    {"input1": 5, "input2": 2, "output": 7},
    {"input1": 12, "input2": 3, "output": 15},
    {"input1": 4, "input2": 4, "output": 8},
]  # просто сложение двух значение, но можно и что то сложение типа (a + b) * 2

# задаются начальные веса (рандом)
weight1 = 0
weight2 = 0.2

i = 0

# делается 10к повторений для расчета весов
while i < 10000:
    i += 1

    for data in test_data:
        # берется расчет нейросетки
        output = data['input1'] * weight1 + data['input2'] * weight2
        # обсчитывается ошибка (разница результата нейросетки и реального значения)
        error = output - data['output']
        # этап регулировки, смотрится в какую сторону необходимо проводить регулировку для каждого из весов
        # делается из расчета что чем меньше ошибка, тем меньше регулировка, но здесь это не учитывается
        adj1 = 0.01 * error * data['input1']
        adj2 = 0.01 * error * data['input2']
        # непосредственно сама регулировка для каждого из весов
        if adj1 > 0:
            weight1 -= 0.00001
        else:
            weight1 += 0.00001
        if adj2 > 0:
            weight2 -= 0.00001
        else:
            weight2 += 0.00001

with open('weights', 'w') as file:
    file.write(f"weight1: {weight1}; weight2: {weight2}")
