import pickle
import os
import matplotlib.pyplot as plt
import fasttext
import numpy as np
from statistics import mean


def getVariance(relatedict):
    n = len(relatedict.keys())
    Xi = list()
    Xi2 = list()

    for item in relatedict.values():
        Xi.append(item)

    for item in relatedict.values():
        Xi2.append(item ** 2)

    if n != 1:
        variance = ((n/(n-1)))*((1/n)*(sum(Xi2)) - (1/n**2)*((sum(Xi))**2))
    else:
        variance = ((1/n)*(sum(Xi2)) - (1/n**2)*((sum(Xi))**2))

    return  variance 

garbage = list()

# подключение модели fasttext
#modelpath = '..\\..\\..\\fastText models\\157 languages\\cc.en.300.bin\\cc.en.300.bin'
modelpath = '..\\..\\..\\fastText models\\157 languages\\cc.ru.300.bin\\cc.ru.300.bin'
print(f'Загрузка модели: {modelpath}')
model = fasttext.load_model(modelpath)              # загрузка модели

# загрузка классифификатора
print('загрузка классифификатора')
pathclassifier = '..\\..\\..\\program part\\Task_3\\task_3\\NewsClassifier.bin'
classifierFile = open(pathclassifier, 'rb')
classifier = pickle.load(classifierFile)
classifierFile.close()

#kernelsPath = '..\\..\\..\\tasks\\Task_3\\kernels'
#kernelsPath = '..\\..\\..\\tasks\\Task_3\\kernels2'
#kernelsPath = '..\\..\\..\\tasks\\Task_3\\kernels3'
kernelsPath = '..\\..\\..\\tasks\\Task_3\\kernels4'
dirList = list()
# получение списка директрорий
print('получение списка директрорий')
for path, dirs, files in os.walk(kernelsPath):
    for dir in dirs:
        kernel = os.path.join(path, dir)
        dirList.append(kernel)

clusterVarianceDic = dict()                         # словарь: ключ - кластер, значение - дисперсия

# работа с файлами в директориях
print('работа с файлами в директориях')
for kernel in dirList:
    print('кластер', kernel)
    countOfFiles = len(os.listdir(kernel))     # число файлов в кластере
    print('число файлов', countOfFiles)
    classCountFile = dict()                         # словарь: ключ - класс, значение - числов файлов в классе
    count = 0
    counterSomething = 0
    countUseFull = 0

    for file in os.listdir(kernel):
        fullFileName = os.path.join(kernel, file)
        currentfile = open(fullFileName, 'r', encoding='utf8')
        text = currentfile.read().replace('\n', ' ')
        vector = model.get_sentence_vector(text)
        label = classifier.predict([vector])
        label = label[0].tolist()
        if (sum(label) != 0):
            label = label.index(1)
            countUseFull += 1
        else:
            garbage.append(fullFileName)
            counterSomething += 1
            continue
        if label not in classCountFile.keys():
            classCountFile[label] = 1
        else:
            classCountFile[label] += 1
    
        count += 1
        if count % 10000 == 0:
            print('переработано файлов в кластере', count)
            print('непонятное counterSomething', counterSomething)
            print('полезное countUseFull', countUseFull)
    classRelationship = dict()
    for key in classCountFile.keys():
        classRelationship[key] = classCountFile[key] / (countOfFiles - counterSomething)

    print('число файлов в каждом классе', classCountFile)
    print('отношение файлов из классов к файла кластера', classRelationship)

    varianceValue = getVariance(classRelationship)
    print('значение дисперсии -', varianceValue)
    kernel = kernel.replace('.txt', '')
    clusterVarianceDic[kernel] = varianceValue

X = list()
Y = list()


sorted_tuple = sorted(clusterVarianceDic.items(), key=lambda x: x[1])


meanValue = mean(clusterVarianceDic.values())

for i, j in sorted_tuple:
    X.append(os.path.basename(i))
    Y.append(j)

plt.bar(X,Y)
plt.show()


writeXY = open('XY4.txt', 'w', encoding='utf8')
for i, j in sorted_tuple:
    print(f'{i} - {j}', file=writeXY)
writeXY.close()
print('meanValue =', meanValue)

garbagefile = open('garbage4.txt', 'w', encoding='utf8')
for item in garbage:
    print(item, file=garbagefile)
garbagefile.close()

print('работа программы успешно завершена!')


