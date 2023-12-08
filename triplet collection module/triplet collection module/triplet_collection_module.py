import dict_article_categories_module as dacm
import The_search_higher_level_category as shlc
import dictionary_of_categories_and_higher_categories as dchc
import datetime

#begin = datetime.datetime.now()

print('введите глубину обхода')
print('>', end='')
inputDeep=int(input())

#outPath = 'newTriplets_ru.txt'
#outPath = 'newTriplets_en_ru.txt'
outPath = 'newTriplets_en.txt'
outputFile = open (outPath, 'w', encoding='utf-8')
outputFile.close()

emptryStrings = 0
uncorrectTriples = 0
correctTriples = 0
statistics = open('statistics', 'w')

second_el_triple = '<http://dbpedia.org/ontology/abstract>'
empty_text = '""@ru.'

dict_ocahc = dchc.dictionary_of_categories_and_higher_categories()
categories = dacm.dict_article_categories()
newTriple = []

paths = [
            #'..\\..\\..\\Файлы Dbpedia\\Dataset 3.9\\long_abstracts_ru.ttl\\long_abstracts_ru.ttl'#,
            #'..\\..\\..\\Файлы Dbpedia\\Dataset 3.9\\long_abstracts_en_uris_ru.ttl\\long_abstracts_en_uris_ru.ttl'#,
            '..\\..\\..\\Файлы Dbpedia\\Dataset 3.9\\long_abstracts_en.ttl\\long_abstracts_en.ttl'
        ]

counter = 0

for path in paths:

    inputFile = open (path, 'r', encoding='utf-8') 
    print(path)

    # пропуск ненужной, первой строки (это строка времени начала ведения триплетов)
    row = inputFile.readline()

    
    while row:

        counter += 1
        text = ''
        high_level_category = ''
        row = inputFile.readline()
        triple = row.split(' ', maxsplit=2)
        if triple == '':
            emptryStrings += 1
            continue
        if len(triple) < 3:
            uncorrectTriples += 1
            continue
        if second_el_triple in triple:
            correctTriples += 1

            if triple[2] != empty_text:

                if triple[0] in categories.keys():
                    if categories[triple[0]] != None:
                        high_level_categories = shlc.search_hc(dict_ocahc, deep=inputDeep, start=categories[triple[0]])
                        text = triple[2].replace('\xa0', ' ')
                        #newTriple = [text, triple[0], high_level_categories]
                        if text != '\"\"@ru .\n' or text != '\"\"@en .\n':
                            newTriple = [text, categories[triple[0]], high_level_categories]
                        else:
                            continue


        outputFile = open (outPath, 'a', encoding='utf-8')
        print(newTriple, file=outputFile)
        #print(newTriple)
        outputFile.close()

        if counter%10000 == 0:
            print(counter, 'записей переработано')
            #break


  
    inputFile.close()

print ('не триплетов (пустых строк): ', emptryStrings)
print ('некорректных триплетов: ', uncorrectTriples)
print ('корректных триплетов: ', correctTriples)
print ('не триплетов (пустых строк): ', emptryStrings, file=statistics)
print ('некорректных триплетов: ', uncorrectTriples, file=statistics)
print ('корректных триплетов: ', correctTriples, file=statistics)
        
statistics.close()

if not outputFile.closed:
    outputFile.close()

print('Работа завершена успешно')