import pandas as pd
import os
import fasttext
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.model_selection import train_test_split


from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.preprocessing import label_binarize
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import PrecisionRecallDisplay

from sklearn.metrics import roc_auc_score

import matplotlib.pyplot as plt

import pickle

path = '..\\..\\..\\tasks\\Task_3'

files = list()
dictTextCls = dict()
rows = list()
classList = list()

# создание списка файлов
print('создание списка файлов')
for file in os.listdir(path):
    files.append(os.path.join(path, file))

# формирование словаря текст - метки 
print('формирование словаря текст - метки')
for file in files:
    print(file)
    if 'kernels' in file:
        continue
    dataset = pd.read_csv(file, delimiter=',')
    for i in range(0, dataset.shape[0]):
        head = dataset['news_headline'][i]
        article = dataset['news_article'][i]
        category = dataset['news_category'][i]
        row = head+article
        rows.append(row)
        classList.append(category)
        if row not in dictTextCls.keys():
            dictTextCls[row] = -1
            if category == 'automobile':
                dictTextCls[row] = 0
            if category == 'politics':
                dictTextCls[row] = 1
            if category == 'sports':
                dictTextCls[row] = 2
            if category == 'entertainment':
                dictTextCls[row] = 3
            if category == 'technology':
                dictTextCls[row] = 4
            if category == 'world':
                dictTextCls[row] = 5
            if category == 'science':
                dictTextCls[row] = 6
        else:
            continue
            


# подключение модели fasttext
#modelpath = '..\\..\\..\\fastText models\\157 languages\\cc.en.300.bin\\cc.en.300.bin'
modelpath = '..\\..\\..\\fastText models\\157 languages\\cc.ru.300.bin\\cc.ru.300.bin'
print(f'Загрузка модели: {modelpath}')
model = fasttext.load_model(modelpath)              # загрузка модели

# создание X и Y  вектор-метки
print('создание X и Y  вектор-метки')
listVectors = list()
listLabels = list()
for key in dictTextCls.keys():
    text = key.replace('\n', ' ')
    labels = dictTextCls[key]
    listLabels.append(labels)
    vector = model.get_sentence_vector(text)
    listVectors.append(vector)

X = np.array(listVectors)
y = np.array(listLabels)

Y = label_binarize(y, classes=[0, 1, 2, 3, 4, 5, 6])

# разделение исходных данных на обучающую и проверяющую выборки
print('разделение исходных данных на обучающую и проверяющую выборки')
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.9, random_state=42)

# построение многометочного классификатора Random Forest
print('построение многометочного классификатора')
classifier = OneVsRestClassifier(
    make_pipeline(StandardScaler(), LinearSVC(random_state=42))
)

classifier.fit(X_train, Y_train)
y_score = classifier.decision_function(X_test)


# применение классификатора
print('применение классификатора')

precision = dict()
recall = dict()
average_precision = dict()
for i in range(7):
    precision[i], recall[i], _ = precision_recall_curve(Y_test[:, i], y_score[:, i])
    average_precision[i] = average_precision_score(Y_test[:, i], y_score[:, i])

precision["micro"], recall["micro"], _ = precision_recall_curve(
    Y_test.ravel(), y_score.ravel()
)
average_precision["micro"] = average_precision_score(Y_test, y_score, average="micro")

display = PrecisionRecallDisplay(
    recall=recall["micro"],
    precision=precision["micro"],
    average_precision=average_precision["micro"],
)
display.plot()
_ = display.ax_.set_title("Micro-averaged over all classes")

plt.show()


ROC_value = roc_auc_score(Y_test, y_score, multi_class='ovr')
print('ROC =', ROC_value)

# сохранение классификатора новостей
modelFileName = 'NewsClassifier.bin'
modelFile = open(modelFileName, 'wb')
pickle.dump(classifier, modelFile)
modelFile.close()

print('работа программы успешно завершена!')