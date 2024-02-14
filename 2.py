f = open('scientist.txt', encoding='utf-8')
table = []

a = f.readline()
for stroke in f: # переносим данные из файла в список
    ScientistName, preparation, date, components = stroke.split('#')
    table.append([date, ScientistName, preparation, components[:-1]])

table.sort()

cnt = 0
for stroke in table: # Выводим первые пять препаратов
    if cnt < 5:
        print(stroke[1], stroke[2])
    else:
        break
    cnt += 1