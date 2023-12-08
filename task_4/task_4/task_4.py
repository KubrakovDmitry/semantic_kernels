import pandas as pd


dataset = pd.read_csv('C:\\Users\\kubra\\Downloads\\archive (6)\\text_series_full.csv')

textClass = dict()

for i in range(0, dataset.shape[0]):
    articleClass = dataset['class'][i]
    text = dataset['text'][i]
    if text not in textClass.keys():
        textClass[text] = list()
    if articleClass not in textClass[text]:
        textClass[text].append(textClass[text])

print(len(textClass.keys()))

