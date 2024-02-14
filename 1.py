f = open('scientist.txt', encoding='utf-8')
table = []

a = f.readline()
for stroke in f: # переносим данные из файла в список
    ScientistName, preparation, date, components = stroke.split('#')
    table.append([date, ScientistName, preparation, components[:-1]])

table.sort()

print('Разработчиками Аллопуринола были такие люди')
cnt = 0
original = ''
for stroke in table:
    if stroke[2] == 'Аллопуринол':
        if cnt > 0:
            print(stroke[1], stroke[0])
        else:
            original = "Оригинальный рецепт принадлежит: " + stroke[1]
        cnt += 1
print(original)






