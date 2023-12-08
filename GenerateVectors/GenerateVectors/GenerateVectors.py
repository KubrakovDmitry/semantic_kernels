import fasttext
import numpy as np
import os

def generateVectors(path, modelPath):
    textVecDict = dict()
    print(f'Загрузка модели: {modelPath}')
    model = fasttext.load_model(modelPath)      # загрузка модели
    print('Загрузка модели завершена!')

    print(f'Открытие источника: {path}')
    input = open(path, 'r', encoding='utf8')    # открытие источника

    output = open(os.path.basename(path).replace('.txt', '_') + 'vectors_string.txt', 'w', encoding='utf8')   # открытие файла для вывода результатов

    line = input.readline()                     # чтение первой записи/строки
    count = 1                                   # счётчик записей
    counterError = 0
    counterErrorTriplet = 0
    while line:

        if line == '\n':
            line = input.readline()
            continue
       
        if len(line.split('<---*--->')) == 1:
            counterErrorTriplet += 1
            print(f'некорректные триплеты {counterErrorTriplet}')
            line = input.readline()
            continue
        id = line.split('<---*--->')[0]         # выделение идентификатора
        text = line.split('<---*--->')[1]       # выделение текста
        text = text.replace("\n"," ")
        vector = model.get_sentence_vector(text)
        textVecDict[id] = vector
        strVector = vector.tostring()
        try:
            print(f'{id} <---*---> {strVector}', file=output)
        except:
            line = input.readline()
            counterError += 1
        if count%100000 == 0:
            print(f'переработано {count} записей')
            print(f'ошибочных записей - {counterError}')

        line = input.readline()
        count += 1

    output.close()
    input.close()
    return textVecDict

if __name__ == '__main__':
    # список источников текста
    #paths = [
    #            '..\\..\\..\\program part\\generateIDs\\generateIDs\\unique_ru_triplets with IDs.txt',
    #            '..\\..\\..\\program part\\generateIDs\\generateIDs\\unique_en_ru_triplets with IDs.txt',
    #            '..\\..\\..\\program part\\generateIDs\\generateIDs\\unique_en2_triplets with IDs.txt'
    #        ]
    #for path in paths:
    #    generateVector(path)    # вызов функции для генерации вектор текста
    path = 'E:\\MAI\\Dissertation\\program part\\generateIDs\\generateIDs\\unique_ru_triplets with IDs.txt'
    modelPath = 'E:\\MAI\\Dissertation\\fastText models\\157 languages\\cc.ru.300.bin\\cc.ru.300.bin'
    textVecDict = generateVectors(path, modelPath)    # вызов функции для генерации вектор текста
    if textVecDict != None:
        print('Словарь {идентификатор вектор: создан}')
    print('Работа программы успешно завершена!')
