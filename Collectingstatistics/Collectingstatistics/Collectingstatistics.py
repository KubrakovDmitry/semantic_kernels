import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

# получение входных данных
labelsCountDict = dict()
input = open('E:\\MAI\\Dissertation\\program part\\clusterization\\clusterization\\result.txt', 'r', encoding='utf8')

# подсчёт количества текстов в каждом кластере
separator = ' <---*---> '
line = input.readline()     # самая первая строка в из файла. Она нужна для входа в цикл и участвует в сборе сведений о кластерах
count = 1
while line:
    label = int(line.split(separator)[1])
    if label in labelsCountDict.keys():
        labelsCountDict[label] += 1
    else:
        labelsCountDict[label] = 1
    if count%100000 == 0:
        print(f'переработано записей {count}')
    line = input.readline()
    count += 1
# закрытие входных данных
input.close()

# сбор статистической информации
log = open('log.txt', 'w', encoding='utf8')
for cluster in range(0, 64):
    if cluster not in labelsCountDict.keys():
        print(f'кластер {cluster} абсолютно пустой, в нём нет тектсов')
        print(f'кластер {cluster} абсолютно пустой, в нём нет тектсов', file=log)
    else:
        print(f'в кластере {cluster} {labelsCountDict[cluster]} текстов')
        print(f'в кластере {cluster} {labelsCountDict[cluster]} текстов', file=log)

print(f'у самого большого кластера {max(labelsCountDict.values())} текстов')
print(f'у самого маленького кластера {min(labelsCountDict.values())} текстов')
print(f'средний размера кластера {round(mean(labelsCountDict.values()))} текстов')
print('пустых класторов нет!')
print(f'у самого большого кластера {max(labelsCountDict.values())} текстов', file=log)
print(f'у самого маленького кластера {min(labelsCountDict.values())} текстов', file=log)
print(f'средний размера кластера {round(mean(labelsCountDict.values()))} текстов', file=log)
print('пустых класторов нет!', file=log)
log.close()

# построение гистограммы
fig = plt.figure()
plt.bar(labelsCountDict.keys(), labelsCountDict.values())
plt.show()
fig.savefig('text distribution histogram1.png') # рисунок сохраняется пустым


print('Работа программы успешно завершена!')
