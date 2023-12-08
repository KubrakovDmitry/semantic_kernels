inputf = open('E:\\MAI\\Dissertation\\program part\\generateIDs\\generateIDs\\trio triplets with IDs.txt', 'r', encoding='utf8')
outputf = open('part of trio triplets with IDs.txt', 'w', encoding='utf8')
count = 0
line = inputf.readline()
while line:
    if line == '\n':
        line = inputf.readline()
        continue
    if (count >= 0 and count <= 10) or (count >= 1000000 and count <= 1000010) or (count >= 3000000 and count <= 3000010):
        outputf.write(line)
        line = inputf.readline()
        count += 1
    else:
        line = inputf.readline()
        count += 1
    if count % 100000 == 0:
        print('переработано записей', count)
    if count > 3000020:
        break

inputf.close()
outputf.close()
print('Работа программы успешно завершена!')
print('Для выхода нажмите любую клавишу!')