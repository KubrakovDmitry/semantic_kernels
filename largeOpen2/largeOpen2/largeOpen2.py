print('Работа началась!')

path = '..\\..\\..\\program part\\clusterization\\clusterization\\result.txt'
path2 = 'part of result.txt'

input = open(path, 'r', encoding='utf8')
output = open(path2, 'w', encoding='utf8')

count = 0
while count < 20:
    line = input.readline()
    print(line, file=output)
    count += 1

input.close()
output.close()

print('Работа программы успешно завершена!')