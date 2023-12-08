import sys

# программа сбора данных о статьях и их категориях
def checkAndAddFun(articleLabel, qMass1):
    if (articleLabel[0] not in qMass1):
        qMass1.append(articleLabel[0])
        qMass1.sort()

def skosCheckAdd(articleLabel, qMass2):
    if articleLabel[1] == '<http://www.w3.org/2004/02/skos/core#broader>':
        if articleLabel[0] not in qMass2:
            qMass2.append(articleLabel[0])
            qMass2.sort()
        if articleLabel[2] not in qMass2:
            qMass2.append(articleLabel[2])
            qMass2.sort()
        

def outFile1(fileName, countRows, lenghtFile):
    print(fileName, countRows, file=lenghtFile)

def secordWork(locFile, numberOfColumn):
    locFile.seek(0,0)
    row = locFile.readline() # пропуски  комментария 
    i = 0
    while row:
        row = locFile.readline()
        i += 1
        if i > 20:
            break    
        articleLabel = row.split(' ', maxsplit=1)
        if qMass1.index(articleLabel[0]) not in list(qarrayArticle.keys()):
            alist = [0] * 15
            alist[numberOfColumn] = 1
            qarrayArticle[qMass1.index(articleLabel[0])] = alist
        else:
            #print('статья уже есть и она обновляется!')
            qarrayArticle[qMass1.index(articleLabel[0])][numberOfColumn] = 1

lenghtFile = open('lenghtFile.txt', 'w', encoding='utf-8')
# Описание списка, в которую сохраняется результат анализа
#qList = []
qMass1 = [] 

# работа с первым файлом
file1 = open('d:\\kdd_2\\файлы dbpedia\\dataset 3.9\\labels_en.ttl\\labels_en.ttl', 'r', encoding='utf-8')
row = file1.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file1.readline()
    countRows += 1
    i += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    print('File 1 articleLabel[0] = ', articleLabel[0])
    qMass1.append(articleLabel[0])
outFile1('d:\\kdd_2\\файлы dbpedia\\dataset 3.9\\labels_en.ttl\\labels_en.ttl', countRows, lenghtFile)

qMass1.sort()

# работа со вторым файлом 
file2 = open('d:\\kdd_2\\файлы dbpedia\\dataset 3.9\\labels_ru.ttl\\labels_ru.ttl', 'r', encoding='utf-8')
row = file2.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file2.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('d:\\kdd_2\\файлы dbpedia\\dataset 3.9\\labels_en.ttl\\labels_en.ttl', countRows, lenghtFile)
     
# работа с третьим файлом
file3 = open('d:\\kdd_2\\файлы dbpedia\\dataset 3.9\\labels_en_uris_ru.ttl\\labels_en_uris_ru.ttl', 'r', encoding='utf-8')
row = file3.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file3.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('d:\\kdd_2\\файлы dbpedia\\dataset 3.9\\labels_en_uris_ru.ttl\\labels_en_uris_ru.ttl', countRows, lenghtFile)

file4 = open('d:\\kdd_2\\файлы dbpedia\\dataset 3.9\\short_abstracts_en_uris_ru.ttl\\short_abstracts_en_uris_ru.ttl', 'r', encoding='utf-8')
row = file4.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file4.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('d:\\kdd_2\\файлы dbpedia\\dataset 3.9\\short_abstracts_en_uris_ru.ttl\\short_abstracts_en_uris_ru.ttl', countRows, lenghtFile)


file5 = open('D:\\kdd_2\Файлы Dbpedia\\Dataset 3.9\\short_abstracts_en_uris_ru.ttl\\short_abstracts_en_uris_ru.ttl', 'r', encoding='utf-8')
row = file5.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file5.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('D:\\kdd_2\Файлы Dbpedia\\Dataset 3.9\\short_abstracts_en_uris_ru.ttl\\short_abstracts_en_uris_ru.ttl', countRows, lenghtFile)

file6 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\short_abstracts_ru.ttl\\short_abstracts_ru.ttl', 'r', encoding='utf-8')
row = file6.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file6.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\short_abstracts_ru.ttl\\short_abstracts_ru.ttl', countRows, lenghtFile)

file7 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\long_abstracts_en.ttl\\long_abstracts_en.ttl', 'r', encoding='utf-8')
row = file7.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file7.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\long_abstracts_en.ttl\\long_abstracts_en.ttl', countRows, lenghtFile)

file8 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\long_abstracts_en_uris_ru.ttl\\long_abstracts_en_uris_ru.ttl', 'r', encoding='utf-8')
row = file8.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file8.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\long_abstracts_en_uris_ru.ttl\\long_abstracts_en_uris_ru.ttl', countRows, lenghtFile)

file9 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\long_abstracts_ru.ttl\\long_abstracts_ru.ttl', 'r', encoding='utf-8')
row = file9.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file9.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\long_abstracts_ru.ttl\\long_abstracts_ru.ttl', countRows, lenghtFile)

file10 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\wikipedia_links_en.ttl\\wikipedia_links_en.ttl', 'r', encoding='utf-8')
row = file10.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file10.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\wikipedia_links_en.ttl\\wikipedia_links_en.ttl', countRows, lenghtFile)

file11 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\wikipedia_links_ru.ttl\\wikipedia_links_ru.ttl', 'r', encoding='utf-8')
row = file11.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file11.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\wikipedia_links_ru.ttl\\wikipedia_links_ru.ttl', countRows, lenghtFile)

file12 = open('d:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_en.ttl\\article_categories_en.ttl', 'r', encoding='utf-8')
row = file12.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file12.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('d:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_en.ttl\\article_categories_en.ttl', countRows, lenghtFile)

file13 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_en_uris_ru.ttl\\article_categories_en_uris_ru.ttl', 'r', encoding='utf-8')
row = file13.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file13.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_en_uris_ru.ttl\\article_categories_en_uris_ru.ttl', countRows, lenghtFile)

file14 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_ru.ttl\\article_categories_ru.ttl', 'r', encoding='utf-8')
row = file14.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file14.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=1)
    checkAndAddFun(articleLabel, qMass1)
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_ru.ttl\\article_categories_ru.ttl', countRows, lenghtFile)
# вывод полученного списка на время отладки 
#print('ратоба со статьями завершена. Вывод qMass1', *qMass1, sep='\n', end='\n')

print('Собраны сведения о статьях')

# Формирование списка категорий 

qMass2 = []
#print('после описания qMass2', *qMass2, sep='\n', end='\n')

file12 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_en.ttl\\article_categories_en.ttl', 'r', encoding='utf-8')
row = file12.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file12.readline()
    countRows += 1
    i += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=3)
    if articleLabel[2] in qMass2:
        continue
    else:
        qMass2.append(articleLabel[2])
        qMass2.sort()
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_en.ttl\\article_categories_en.ttl', countRows, lenghtFile)

file13 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_en_uris_ru.ttl\\article_categories_en_uris_ru.ttl', 'r', encoding='utf-8')
row = file13.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file13.readline()
    countRows += 1
    i += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=3)
    if articleLabel[2] in qMass2:
        continue
    else:
        qMass2.append(articleLabel[2])
        qMass2.sort()
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_en_uris_ru.ttl\\article_categories_en_uris_ru.ttl', countRows, lenghtFile)

file14 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_ru.ttl\\article_categories_ru.ttl', 'r', encoding='utf-8')
row = file14.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file14.readline()
    countRows += 1
    i += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=3)
    if articleLabel[2] in qMass2:
        continue
    else:
        qMass2.append(articleLabel[2])
        qMass2.sort()
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\article_categories_ru.ttl\\article_categories_ru.ttl', countRows, lenghtFile)

file15 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\category_labels_en.ttl\\category_labels_en.ttl', 'r', encoding='utf-8')
row = file15.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file15.readline()
    countRows += 1
    i += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=3)
    if articleLabel[2] in qMass2:
        continue
    else:
        qMass2.append(articleLabel[2])
        qMass2.sort()
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\category_labels_en.ttl\\category_labels_en.ttl', countRows, lenghtFile)

file16 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\category_labels_en_uris_ru.ttl\\category_labels_en_uris_ru.ttl', 'r', encoding='utf-8')
row = file16.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file16.readline()
    countRows += 1
    i += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=3)
    if articleLabel[2] in qMass2:
        continue
    else:
        qMass2.append(articleLabel[2])
        qMass2.sort()
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\category_labels_en_uris_ru.ttl\\category_labels_en_uris_ru.ttl', countRows, lenghtFile)

file17 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\category_labels_ru.ttl\\category_labels_ru.ttl', 'r', encoding='utf-8')
row = file17.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file17.readline()
    countRows += 1
    i += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=3)
    if articleLabel[2] in qMass2:
        continue
    else:
        qMass2.append(articleLabel[2])
        qMass2.sort()
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\category_labels_ru.ttl\\category_labels_ru.ttl', countRows, lenghtFile)

file18 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\skos_categories_en.ttl\\skos_categories_en.ttl', 'r', encoding='utf-8')
row = file18.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file18.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=3)
    skosCheckAdd(articleLabel, qMass2)
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\skos_categories_en.ttl\\skos_categories_en.ttl', countRows, lenghtFile)

file19 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\skos_categories_en_uris_ru.ttl\\skos_categories_en_uris_ru.ttl', 'r', encoding='utf-8')
row = file19.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file19.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=3)
    skosCheckAdd(articleLabel, qMass2)
outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\skos_categories_en_uris_ru.ttl\\skos_categories_en_uris_ru.ttl', countRows, lenghtFile)

file20 = open('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\skos_categories_ru.ttl\\skos_categories_ru.ttl', 'r', encoding='utf-8')
row = file20.readline() # пропуски  комментария 
i = 0
countRows = 0
while row:
    row = file20.readline()
    i += 1
    countRows += 1
    if i > 20:
        break    
    articleLabel = row.split(' ', maxsplit=3)
    skosCheckAdd(articleLabel, qMass2)




outFile1('D:\\kdd_2\\Файлы Dbpedia\\Dataset 3.9\\skos_categories_ru.ttl\\skos_categories_ru.ttl', countRows, lenghtFile)
# вывод полученного списка на время отладки 
print('Итоговое состояние qMass1', *qMass1, sep='\n', end='\n')
#print('Итоговое состояние qMass2', *qMass2, sep='\n', end='\n')
lenghtFile.close()

print('Собраны сведения о категориях')
#sys.exit(0)

qarrayArticle = {}
# работа с первым файлом
secordWork(file1, 0)
secordWork(file2, 1)
secordWork(file3, 2)
secordWork(file4, 3)
secordWork(file5, 4)
secordWork(file6, 5)
secordWork(file7, 6)
secordWork(file8, 7)
secordWork(file9, 8)
secordWork(file10, 9)
secordWork(file11, 10)
secordWork(file12, 11)
secordWork(file13, 12)
secordWork(file14, 13)


list_keys = list(qarrayArticle.keys())
list_keys.sort()

for item in list_keys:
    Values = qarrayArticle[item]
    j = 0
    summa = 0
    while j < 14:
        summa += Values[j]
        j += 1
    qarrayArticle[item][14] = summa

outputFile = open('output.csv', 'w')

for item in list_keys:
    #print('item = ', item)
    print(item, ';', *qarrayArticle[item], qMass1[item])
    print(item, ';', *qarrayArticle[item], qMass1[item], file=outputFile)

outputFile.close()
