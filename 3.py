f = open('scientist.txt', encoding='utf-8')
table = []

a = f.readline()
for stroke in f: # переносим данные из файла в список
    ScientistName, preparation, date, components = stroke.split('#')
    table.append([date, ScientistName, preparation, components[:-1]])

table.sort()

while True: # выполняем поиск по списку нужной даты, если дата не найдена выводим: В этот день ученые отдыхали
    dataa = input()
    if dataa == 'эксперимент':
        break
    if dataa.count('.') != 2:
        break
    d1, d2, d3 = dataa.split('.')
    dataa = d1+'-'+d2+'-'+d3
    cnt = 0
    for stroke in table:
        if stroke[0] == dataa:
            print(f'Ученый {stroke[1]} создал препарат: {stroke[2]} - {stroke[0]}')
            cnt += 1
    if cnt == 0:
        print('В этот день ученые отдыхали')