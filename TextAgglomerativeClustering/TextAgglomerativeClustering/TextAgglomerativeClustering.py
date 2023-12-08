import os
import fasttext
import numpy as np
from sklearn.cluster import AgglomerativeClustering
import sys
import pickle


#получение списка файлов с векторами
counterPass = 0
counterFail = 0
#count = 0
print('получение списка файлов с векторами')
inputpath = '..\\..\\..\\tasks\\Task_2\\vectors'    # путь к директории с файлами с векторами
filenames = os.listdir(inputpath)                   # список имён файлов с векторами
filepaths = list()                                  # список путей к файлам с векторами
for filename in filenames:
    filepath = os.path.join(inputpath, filename)
    filepaths.append(filepath)

vetorlist = list()
for filepath in filepaths:
    file = open(filepath, 'r', encoding='utf8')
    try:
        text = file.read().replace("\n"," ")
    except:
        counterFail += 1
        continue
    text = text.split('<---*--->')[1].replace('[', ' ').replace(']', ' ')

    vector = np.fromstring(text, dtype=float, sep=' ')
    vetorlist.append(vector)
    counterPass += 1
    file.close()
    if counterPass % 100000 == 0:
        print(f'число считанных файлов {counterPass}')
    if (counterFail % 10 == 0) and (counterFail > 0):
        print(f'число неудачных файлов {counterFail}')


print(f' тип списка vetorlist = {type(vetorlist)}')
print(f' размер списка vetorlist = {sys.getsizeof(vetorlist)}')
print(f' длина списка vetorlist = {len(vetorlist)}')

# кластеризация
print('кластеризация')
vetorlist = np.array(vetorlist)
print(vetorlist.shape)       
print(vetorlist.dtype)

clustering = AgglomerativeClustering(n_clusters=None, distance_threshold=0, linkage='single').fit(vetorlist)    # кластеризация текстов
labels= clustering.labels_

print(f'число меток в списке метов - {len(labels)}')
print(f'число файлов в списке метов - {(vetorlist)}')

# создание директории для кластеров
outputClustersPath = '..\\..\\..\\tasks\\Task_2'
nameDir = 'clusters'
clusterDir = os.path.join(outputClustersPath, nameDir)
if not os.path.exists(clusterDir):
    os.mkdir(clusterDir)

# сохранение модели, данных на диске
# сохранение источников текстов
print('сохранение источников текстов')
fileListName = 'writtenList_2.txt'
listPath = os.path.join(outputClustersPath, fileListName)
writtenList = open(listPath, 'w', encoding='utf8')
for filepath in filepaths:
    print(filepath, file=writtenList)
writtenList.close()

# сохранение вектров текстов
print('сохранение вектров текстов')
vectorFileTDName = 'vectorsTD_2.txt'
vectorPathTD = os.path.join(outputClustersPath, vectorFileTDName)
np.savetxt(vectorPathTD, vetorlist, encoding='utf8')

# сохранение модели
print('сохранение модели')
modelFileName = 'model_2.pkl'
modelPath = os.path.join(outputClustersPath, modelFileName)
modelFile = open(modelPath, 'wb')
pickle.dump(clustering, modelFile)
modelFile.close()

# сохранение кластеров
print('работа программы успешно завершена!')