import fasttext
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_recall_fscore_support
import matplotlib.pyplot as plt
from sklearn.metrics import roc_auc_score
import numpy as np
from sklearn.metrics import auc
from sklearn import preprocessing


pathTestData = '..\\..\\..\\program part\\prepareTrainAndTest\\prepareTrainAndTest\\test_trio.txt'
pathModel = '..\\..\\..\\program part\\trainFastTextClassifier\\trainFastTextClassifier\\classifier_trio.bin'
pathTestResult = 'testResult.txt'
pathPredResult = 'predResult.txt'
pathProba = 'probaResult.txt'

listLabelTest = list()
listLabelPred = list()
listDataText = list()
listProba = list()

fileTestData = open(pathTestData, 'r', encoding='utf8')
line = fileTestData.readline()

counter = 0

while line:
    if line == '\n':
        line = fileTestData.readline()
        continue
    else:
        label, text = line.split(' ', 1)
        listLabelTest.append(int(label.replace('__label__', '')))
        listDataText.append(text)
        line = fileTestData.readline()
        counter += 1
        if counter % 100000 == 0:
            print(f'прочитано {counter} записей')



print('загрузка модели')
module = fasttext.load_model(pathModel)

counter = 0

for item in listDataText:
    item = item.replace("\n"," ")
    label = module.predict(item)
    listLabelPred.append(int(label[0][0].replace('__label__', '')))
    label = float(label[1])
    label = round(label, 4)
    if  label >= 1.0:
        continue
    listProba.append(label)
    counter += 1
    if counter % 100000 == 0:
        print(f'предсказано {counter} меток')

# вычисление точности и полноты

precision = precision_score(listLabelTest, listLabelPred, average=None)
recall = recall_score(listLabelTest, listLabelPred, average=None)

recall = recall.tolist()
precision = precision.tolist()

recall.sort()
precision.sort(reverse=True) 

# построение кривой точности и полноты
fig, ax = plt.subplots()
ax.plot(recall, precision, color='purple')

# добавление осей меток
ax.set_title('Precision-Recall Curve')
ax.set_ylabel('Precision')
ax.set_xlabel('Recall')

# отображение графика
plt.show()

# сохранение графика
fig.savefig('Precision-Recall-Curve.png')

AUCfile = open('aut.txt', 'w', encoding='utf-8')
print('len(np.matrix(listLabelTest)) =', np.array(listLabelTest).shape)
print('len(np.matrix(listProba)) =', np.array(listProba).shape)
auc_val = roc_auc_score(np.array(listLabelTest), np.array(listProba).reshape(534940 , 1), multi_class='ovo')
AUCfile.close()

# очистак списка
listLabelTest.clear()
listLabelPred.clear()
listDataText.clear()
listProba.clear()

print('Изображение с графиком точности-полноты сохранён!\n')
print('Работа программы успешно завершена!')
