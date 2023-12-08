inputf = open('E:\\MAI\\Dissertation\\program part\\uniqueTriplets\\uniqueTriplets\\unique_en.txt', 'r', encoding='utf8')
outputf = open('unique_en2.txt', 'w', encoding='utf8')

str_en = '\"\"@en'

line = inputf.readline()
count = 1
while line:
    if str_en not in line:
        print(line, file=outputf)
    if count%100000 == 0:
        print(f'прочитано записей {count}')
    line = inputf.readline()
    count += 1

outputf.close()
print('Работа программы успешно завершена!')