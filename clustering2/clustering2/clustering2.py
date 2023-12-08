import os
import fasttext
from sklearn.cluster import KMeans
import numpy as np
import pickle

# путь к новым ядрам 
#pathKernels2 = r'E:\MAI\Dissertation\tasks\Task_3\kernels2'
#pathKernels2 = r'E:\MAI\Dissertation\tasks\Task_3\kernels3'
pathKernels2 = r'E:\MAI\Dissertation\tasks\Task_3\kernels4'

# загрузка модели fasttext
print('подключение модели fasttext')
modelpath = '..\\..\\..\\fastText models\\157 languages\\cc.ru.300.bin\\cc.ru.300.bin'
print(f'Загрузка модели: {modelpath}')
model = fasttext.load_model(modelpath)              # загрузка модели

# создание списка директорий с файлами
print('создание списка директорий с файлами')
#sourcePath = r'..\..\..\program part\cluste_selection\cluste_selection\XY.txt'
#sourcePath = r'..\..\..\program part\cluste_selection\cluste_selection\XY2.txt'
sourcePath = r'..\..\..\program part\cluste_selection\cluste_selection\XY3.txt'
sourcefile = open(sourcePath, 'r', encoding='utf8')

directories = list()

counterFile = 0
line = sourcefile.readline()
while line:
    counterFile += 1
    if counterFile < 32:                    # 34 - 1ая итерация, 34 - 2ая итерация
        line = sourcefile.readline()
    else:
        line = line.split(' - ')[0]
        directories.append(line)
        line = sourcefile.readline()

sourcefile.close()

# получение списка файлов кластеров
print('получение списка файлов кластеров')
fileList = list()
for dir in directories:
    for file in os.listdir(dir):
        fullFileName = os.path.join(dir, file)
        fileList.append(fullFileName)
  
# векторизация
print('векторизация')
vectors = list()
counterVector = 0  
for filePath in fileList:
    openedfile = open(filePath, 'r', encoding='utf8')
    text = openedfile.read().replace('\n', '')
    vector = model.get_sentence_vector(text)
    vectors.append(vector)
    counterVector += 1
    if counterVector % 100000 == 0:
        print(f'векторизовано {counterVector} текстов')

# перекластеризация
print('перекластеризация')
X = np.array(vectors)

clusteringModel = KMeans(n_clusters = 64)
clusteringModel.fit(X)

# сохранение новых ядер на диске
print('сохранение новых ядер на диске')
labels = clusteringModel.labels_
count = 0
countFile = len(fileList)
while count < countFile:
    fullFileName = fileList[count]
    fileName = os.path.basename(fullFileName)
    dirName = str(labels[count])
    dirName = os.path.join(pathKernels2, dirName)
    if not os.path.isdir(dirName):
        os.mkdir(dirName)
    newFullFileName = os.path.join(dirName, fileName)
    input = open(fullFileName, 'r', encoding='utf8')
    text = input.read()
    output = open(newFullFileName, 'w', encoding='utf8')
    print(text, file=output)
    input.close()
    output.close()
    count += 1
    if count % 100000 == 0:
        print(f'прочитано {count} файлов')



# сохранение модели для кластеризации на диске
#fileModel = open('clusteringModel.bin', 'wb')
#fileModel = open('clusteringModel2.bin', 'wb')
fileModel = open('clusteringModel3.bin', 'wb')
pickle.dump(clusteringModel, fileModel)
fileModel.close()

print('работа программы успешно завершена!')
