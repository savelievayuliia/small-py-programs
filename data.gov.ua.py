import csv

total = 0
with open('zp-cherven-2019.csv', newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=';')
    data = [tuple(row) for row in reader]
    numbers = []
    number_of_zp = 0
    average = 0.0
    for item in data:
        numbers.append(item[2])
    del numbers[0]
    oklad = []
    for zp in numbers:
        if zp != "":
            zp = zp.replace(",", ".")
            zp = float(zp)
            oklad.append(zp)
            average += float(zp)
            number_of_zp += 1
    average = average / number_of_zp
    print("Средний оклад сотрудников: ", format(average, ",.2f"), "UAH")
    print("Минимальный оклад сотрудников: ", format(min(oklad), ",.2f"), "UAH")
    print("Максимальный оклад сотрудников: ", format(max(oklad), ",.2f"), "UAH")
