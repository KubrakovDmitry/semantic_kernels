import fasttext

print('обучение классификатора')
print('начало работы!')

# путь к обучающей выборке
pathTrain = '..\\..\\..\\program part\\prepareTrainAndTest\\prepareTrainAndTest\\train_trio.txt'
# путь к проверочной выборке
pathTest = '..\\..\\..\\program part\\prepareTrainAndTest\\prepareTrainAndTest\\test_trio.txt'
# путь для сохранения модели
pathSave = 'classifier_trio.bin'
# путь к файлу вывода результатов тестирования
pathResult = 'result_trio.txt'

print('начало обучения модели')
# обучение модели классфикатора
model = fasttext.train_supervised(input=pathTrain)
print('конец обучения модели')
# сохранение модели
print('сохраниение модели')
model.save_model(pathSave)
# тестирование модели
print('тестирование модели')
result = model.test(pathTest)
print(result)
output = open(pathResult, 'w', encoding='utf-8')
print(result, file=output)
output.close()
print('работа программы успешно завершена!')
