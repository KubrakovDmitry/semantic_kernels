import os
from random import shuffle
import pandas as pd


sourceFilesPath = '..\\..\\..\\tasks\\Task_3\\sourcesFile'
#noKernels = '..\\..\\..\\tasks\\Task_3\\nokernels'

texts = list()
texts_labels = list()

for file in os.listdir(sourceFilesPath):
    file = os.path.join(sourceFilesPath, file)
    dataset = pd.read_csv(file, delimiter=',')
    news_headlines = dataset['news_headline']
    news_articles = dataset['news_article']
    news_categories = dataset['news_category']
    count = dataset.shape[0]
    for i in range(0, count):
        text = news_headlines[i] + news_articles[i]
        if text not in texts:
            label = -1
            if news_categories[i] == 'automobile':
                label = 64
            if news_categories[i] == 'politics':
                label = 65
            if news_categories[i] == 'sports':
                label = 66
            if news_categories[i] == 'entertainment':
                label = 67
            if news_categories[i] == 'technology':
                label = 68
            if news_categories[i] == 'world':
                label = 69
            if news_categories[i] == 'science':
                label = 70
            text_label = text + "<---*--->" + str(label)
            texts_labels.append(text_label)
            texts.append(text)


shuffle(texts_labels)

directPath = '..\\..\\..\\tasks\\Task_3'
dirName1 = 'part_1'
dirName2 = 'part_2'
fullDirName1 = os.path.join(directPath, dirName1)
fullDirName2 = os.path.join(directPath, dirName2)

if not os.path.isdir(fullDirName1):
    os.mkdir(fullDirName1)
if not os.path.isdir(fullDirName2):
    os.mkdir(fullDirName2)

countfile = 0
for i in range(len(texts_labels)):
    countfile += 1
    text, label = texts_labels[i].split('<---*--->')
    if i < len(texts_labels) // 2:
        dirForClass = os.path.join(fullDirName1, label)
        if not os.path.isdir(dirForClass):
            os.mkdir(dirForClass)
        fileName = str(countfile) + '.txt'
        fileName = os.path.join(dirForClass, fileName) 
        input = open(fileName, 'w', encoding='utf8')
        input.write(text)
        input.close()

    if i > len(texts_labels) // 2:
        dirForClass = os.path.join(fullDirName2, label)
        if not os.path.isdir(dirForClass):
            os.mkdir(dirForClass)
        fileName = str(countfile) + '.txt'
        fileName = os.path.join(dirForClass, fileName)
        input = open(fileName, 'w', encoding='utf8')
        input.write(text)
        input.close()

print('работа прораммы успешно завершена!')
