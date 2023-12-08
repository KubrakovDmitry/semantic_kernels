#import sklearn
import GenerateVectors
from sklearn.cluster import KMeans
import numpy as np
import pickle


separator = '<---*--->'
textVecDict = dict()                              # словарь вида {id: vector}
# усточник текста
path = 'E:\\MAI\\Dissertation\\program part\\generateIDs\\generateIDs\\trio triplets with IDs.txt'
#path = 'E:\\MAI\\Dissertation\\program part\\generateIDs\\generateIDs\\unique_ru_triplets with IDs.txt'
# модель векторизации
modelPath = 'E:\\MAI\\Dissertation\\fastText models\\157 languages\\cc.ru.300.bin\\cc.ru.300.bin'
# вызов функции для генерации вектор текста
textVecDict = GenerateVectors.generateVectors(path, modelPath)    

model = KMeans(n_clusters=64)                      # создание модели к-средних для разделения на 64 кластера 
#keys = textVecDict.keys()                         # тексты, которые будут кластеризироваться
listVectors = list()
# распаковка векторов из значений словаря
for key in textVecDict.keys():
    listVectors.append(textVecDict[key])
X = np.array(listVectors)
#print(type(X[0]))
#print(X)

print('Кластеризация')
model.fit(X)                                      # кластеризация текстов

#сохранение модели
print('сохранение модели')
modelFileName = 'clusteringModel.bin'
modelFile = open(modelFileName, 'wb')
pickle.dump(model, modelFile)
modelFile.close()

# определение к какому кластеру относится каждый текст
result = open(path.split('\\')[-1].split()[0] + 'result.txt', 'w', encoding='utf8')
print('Определение у какаго текста какая метка кластера')
count_text_label = 1
for key in textVecDict.keys():
    vector = textVecDict[key]
    np_vector = np.array([vector])
    text_label = model.predict(np_vector)[0]
    print(f'{key} {separator} {text_label}', file=result)
    if count_text_label%100000 == 0:
        print(f'обработано {count_text_label} записей')
    count_text_label += 1
result.close()



#textcluster = model.labels_                        # определение к какому кластеру односится каждый текст
#outputLabels = open('The labels for everyone text.txt', 'w', encoding='utf8')
#print('Вывод результатов кластеризации в файл')
##print(f'textcluster = {textcluster}')
#print(textcluster, file=outputLabels)
#outputLabels.close()

print('Работа программы успешно завершена!')