import os
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import fasttext
from sklearn.svm import SVC
import numpy as np
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

import time

# получение списка файлов
print('получение списка файлов')
sourcePath = '..\\..\\..\\tasks\\Task_3\\kernels4'
filelist = list()

for root, dirs, files in os.walk(sourcePath):
    for file in files:
        filePath = os.path.join(root, file)
        filelist.append(filePath)

# загрузка модели fasttext
print('загрузка модели fasttext')
modelPath = '..\\..\\..\\fastText models\\157 languages\\cc.ru.300.bin\\cc.ru.300.bin'
modelFasttext = fasttext.load_model(modelPath)

# формирование выборки
print('формирование выборки')
X = list()
Y = list()

counter = 0
for file in filelist:
    input = open(file, 'r', encoding='utf8')
    text = input.read().replace('\n', '')
    input.close()
    vector = modelFasttext.get_sentence_vector(text)
    label = int(file.split('\\')[-2])
    X.append(vector)
    Y.append(label)
    counter += 1
    if counter % 10000 == 0:
        print(f'сформировано {counter} записей для выборки')
    

# построение классификатора для получение дополнительного вектора
print('построение классификатора для получение дополнительного вектора')
X = np.array(X)
Y = np.array(Y)
clf = make_pipeline(StandardScaler(), SVC(gamma='auto', probability=True))
clf.fit(X, Y)

# формирование выборок для построения целевых классификаторов
print('формирование выборок для построения целевых классификаторов')
sourcePath2 = '..\\..\\..\\tasks\\Task_3\\part_2'
filelist = list()

for root, dirs, files in os.walk(sourcePath2):
    for file in files:
        filePath = os.path.join(root, file)
        filelist.append(filePath)

X = list()
Y = list()

for file in filelist:
    input = open(file, 'r', encoding='utf8')
    text = input.read().replace('\n', '')
    input.close()
    vector = modelFasttext.get_sentence_vector(text)
    label = int(file.split('\\')[-2])
    X.append(vector)
    Y.append(label)


X = np.array(X)
Y = np.array(Y)

Y = label_binarize(Y, classes=[64, 65, 66, 67, 68, 69, 70])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# расширение векторов
print('расширение векторов')
extended_X_train = list()
extended_X_test = list()

# расширение обучающей выборки
print('расширение обучающей выборки')
for vector in X_train:
    probaLabels = clf.predict_proba([vector])
    extendedVector = np.concatenate([vector, probaLabels[0]])
    extended_X_train.append(extendedVector)

# расширение обучающей выборки
print('расширение проверяющей выборки')
for vector in X_test:
    probaLabels = clf.predict_proba([vector])
    extendedVector = np.concatenate([vector, probaLabels[0]])
    extended_X_test.append(extendedVector)

extended_X_train = np.array(extended_X_train)
extended_X_test = np.array(extended_X_test)

print('type(extended_X_train) =', type(extended_X_train))
print('type(extended_X_test) =', type(extended_X_test))
print(' extended_X_train.ndim =', extended_X_train.ndim)
print(' extended_X_test.ndim =', extended_X_test.ndim)
print(' extended_X_train.shape =', extended_X_train.shape)
print(' extended_X_test.shape =', extended_X_test.shape)

# построение классификатор на тексте ядрах
print('построение классификатор на тексте с ядрами')
classifier = OneVsRestClassifier(
    make_pipeline(StandardScaler(), LinearSVC(random_state=42))
)

# обучение классификатора с СЯ 
time1Fit = time.time()
classifier.fit(extended_X_train, Y_train)
time2Fit = time.time()
diffTimes = time2Fit - time1Fit
timeFitFile = open('время обучения с СЯ.txt', 'w', encoding='utf8')
print(diffTimes, file=timeFitFile)
timeFitFile.close()
# применение класссификатора с СЯ
timeDec1 = time.time()
y_score = classifier.decision_function(extended_X_test)
timeDec2 = time.time()
diffTimes = timeDec2 - timeDec1
timeFitFile = open('скорость классификации с СЯ.txt', 'w', encoding='utf8')
timeFitFile2 = open('время классификации c СЯ.txt', 'w', encoding='utf8')
num_rows, num_cols = extended_X_test.shape
print(diffTimes/num_rows, file=timeFitFile)
print(diffTimes, num_rows, file=timeFitFile2)
timeFitFile.close()
timeFitFile2.close()

print('применение классификатора с ядрами')
# For each class
precision = dict()
recall = dict()
average_precision = dict()
for i in range(7):
    precision[i], recall[i], _ = precision_recall_curve(Y_test[:, i], y_score[:, i])
    average_precision[i] = average_precision_score(Y_test[:, i], y_score[:, i])

# A "micro-average": quantifying score on all classes jointly
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
#_ = display.ax_.set_title("Micro-averaged over all classes with kernels")
_ = display.ax_.set_title("Классификатор с СЯ")
plt.savefig('классификатор с СЯ рус.png')
plt.show()


ROC_value = roc_auc_score(Y_test, y_score, multi_class='ovr')
print('ROC классификатора с ядрами =', ROC_value)
ROC_file = open('ROCwithKernels.txt', 'w', encoding='utf8')
ROC_file.write(str(ROC_value))
ROC_file.close()

# сохранение классификатора с ядрами
print('сохранение классификатора с ядрами')
modelFileName = 'ClassifierWithKernels.bin'
modelFile = open(modelFileName, 'wb')
pickle.dump(classifier, modelFile)
modelFile.close()

# построение классификатор на тексте без ядер
print('построение классификатор на тексте без ядер')
classifier = OneVsRestClassifier(
    make_pipeline(StandardScaler(), LinearSVC(random_state=42))
)

# обучение классификатора без СЯ 
time1Fit = time.time()
classifier.fit(X_train, Y_train)
time2Fit = time.time()
diffTimes = time2Fit - time1Fit
timeFitFile = open('время обучения без СЯ.txt', 'w', encoding='utf8')
print(diffTimes, file=timeFitFile)
timeFitFile.close()
# применение класссификатора без СЯ
timeDec1 = time.time()
y_score = classifier.decision_function(X_test)
timeDec2 = time.time()
diffTimes = timeDec2 - timeDec1
timeFitFile = open('скорость классификации без СЯ.txt', 'w', encoding='utf8')
timeFitFile2 = open('время классификации без СЯ.txt', 'w', encoding='utf8')
num_rows, num_cols = extended_X_test.shape
print(diffTimes/num_rows, file=timeFitFile)
print(diffTimes, num_rows, file=timeFitFile2)
timeFitFile.close()
timeFitFile2.close()

print('применение классификатора без ядер')
# For each class
precision = dict()
recall = dict()
average_precision = dict()
for i in range(7):
    precision[i], recall[i], _ = precision_recall_curve(Y_test[:, i], y_score[:, i])
    average_precision[i] = average_precision_score(Y_test[:, i], y_score[:, i])

# A "micro-average": quantifying score on all classes jointly
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

_ = display.ax_.set_title("Классификаторо без СЯ")
plt.savefig('классификатор без СЯ рус.png')
plt.show()


ROC_value = roc_auc_score(Y_test, y_score, multi_class='ovr')
print('ROC классифкатора без ядер =', ROC_value)
print('ROC =', ROC_value)
ROC_file = open('ROCwithoutKernels.txt', 'w', encoding='utf8')
ROC_file.write(str(ROC_value))
ROC_file.close()

# сохранение классификатора без ядер
print('сохранение классификатора без ядер')
modelFileName = 'ClassifierWithoutKernels.bin'
modelFile = open(modelFileName, 'wb')
pickle.dump(classifier, modelFile)
modelFile.close()


print('работа программы успешно завершена!')
