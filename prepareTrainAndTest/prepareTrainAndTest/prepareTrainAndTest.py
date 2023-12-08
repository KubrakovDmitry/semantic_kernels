import random
import os.path

print('Работа - началась!')
# путь к источнику выборок 
#path = '..\\..\\..\\program part\\generateLablesForFasttext\\generateLablesForFasttext\\unique_ru_tripletsidLabels.txt'
path = '..\\..\\..\\program part\\generateLablesForFasttext\\generateLablesForFasttext\\result.txtidLabels.txt'
source = open(path, 'r', encoding='utf8')

sourceSize = os.path.getsize(path)      # размер источника

generalList = list()                    # общий список записей

# файлы обучащей и проверяющей выборок
#trainPath = 'train_ru.txt'
#testPath = 'test_ru.txt'
trainPath = 'train_trio.txt'
testPath = 'test_trio.txt'

train = open(trainPath, 'w', encoding='utf-8')
test = open(testPath, 'w', encoding='utf-8')

train.close()
test.close()

# заполнение общего списка
line = source.readline()
counter = 0
while line:
    if line == '\n':
        line = source.readline()
        continue
    else:
        generalList.append(line)
        line = source.readline()
        counter += 1
        if counter % 100000 == 0:
            print(f'прочитано {counter} записей')

# перетосовка списка
random.shuffle(generalList)
elementNumber = 0           # номер текущего элемента

# создание обучающей выборки
print('запись обучающей выборки')
while os.path.getsize(trainPath) <= sourceSize * 0.8:
    train = open(trainPath, 'a', encoding='utf-8')
    train.write(generalList[elementNumber])
    train.close()
    elementNumber += 1
    if elementNumber % 100000 == 0:
        print(f'занесено {elementNumber} записей')

# создание проверяющей выборки
print('запись проверяющей выборки')
while os.path.getsize(testPath) <= sourceSize * 0.2:
    if not (elementNumber < len(generalList)):
        break
    test = open(testPath, 'a', encoding='utf-8')
    test.write(generalList[elementNumber])
    test.close()
    elementNumber += 1
    if elementNumber % 100000 == 0:
        print(f'занесено {elementNumber} записей')

print('Работа программы успешно завершена!')


