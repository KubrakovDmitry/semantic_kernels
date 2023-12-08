import pandas as pd
import os


sourceFilesPath = '..\\..\\..\\tasks\\Task_3\\sourcesFile'
noKernels = '..\\..\\..\\tasks\\Task_3\\nokernels'

countfile = 1

texts = list()

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
            folder = os.path.join(noKernels, str(label))
            if not os.path.isdir(folder):
                os.mkdir(folder)
            fullFileNane = os.path.join(folder, str(countfile)+'.txt')
            output = open(fullFileNane, 'w', encoding='utf8')
            output.write(text)
            output.close()
            countfile += 1

print('работа прораммы успешно завершена!')