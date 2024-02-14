f = open('scientist.txt', encoding='utf-8')
table = []

a = f.readline()
for stroke in f: # переносим данные из файла в список
    ScientistName, preparation, date, components = stroke.split('#')
    table.append([date, ScientistName, preparation, components[:-1]])

table.sort()
preps = []
for stroke in table: # Проходимся по списку и ищем настоящих ученых
    if stroke[2] not in preps:
        print(stroke[1]+'#'+stroke[2]+'#'+stroke[0]+'#'+stroke[3])
    preps.append(stroke[2])