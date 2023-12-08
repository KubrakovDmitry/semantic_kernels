def dictionary_of_categories_and_higher_categories():

    # переменные для статистики работы модуля, вырабатывающего словарь категорий и вышестоящих категорий
    emptryStrings = 0
    uncorrectTriples = 0
    correctTriples = 0
    statistics = open('statistics', 'w')

    second_el_triple = '<http://www.w3.org/2004/02/skos/core#broader>'

    dict_ocahc = {}

    paths = [
                '..\\..\\..\\Файлы Dbpedia\\DataSet 3.9\\skos_categories_ru.ttl\\skos_categories_ru.ttl',
                '..\\..\\..\\Файлы Dbpedia\\DataSet 3.9\\skos_categories_en_uris_ru.ttl\\skos_categories_en_uris_ru.ttl',
                '..\\..\\..\\Файлы Dbpedia\\DataSet 3.9\\skos_categories_en.ttl\\skos_categories_en.ttl'
            ]

    counter = 0

    for path in paths:

        print(path)

        f = open(path, 'r', encoding='utf-8')

        # пропуск ненужной, первой строки (это строка времени начала ведения триплетов)
        row = f.readline()

        
        while row:
            row = f.readline()
            counter += 1
            triple = row.split(' ', maxsplit=2)
            if triple == '':
                emptryStrings += 1
                continue
            if len(triple) < 3:
                uncorrectTriples += 1
                continue
            # если в триплете присутствует признак отношения "категория" и "вышестоящая категория", 
            # то перерабатываем его
            if second_el_triple in triple:
                correctTriples += 1
                # если такая категория-ключ уже встречалась, то пополняем её список вышестоящих категорий
                if triple[0] in dict_ocahc:
                    dict_ocahc[triple[0]].append(triple[2].rstrip(' .\n'))
                # в противном случае, для новой категории-ключа создаётся свой список 
                else:
                    dict_ocahc[triple[0]] = [triple[2].rstrip(' .\n')]
            if counter%1000000 == 0:
                print('переработано записей', counter)
        f.close()
    
    print ('не триплетов (пустых строк): ', emptryStrings)
    print ('некорректных триплетов: ', uncorrectTriples)
    print ('корректных триплетов: ', correctTriples)
    print ('не триплетов (пустых строк): ', emptryStrings, file=statistics)
    print ('некорректных триплетов: ', uncorrectTriples, file=statistics)
    print ('корректных триплетов: ', correctTriples, file=statistics)
        
    statistics.close()

    return dict_ocahc

def main():

    print('This is the dictionary_of_categories_and_higher_categories program!')

    dict_out_put = dictionary_of_categories_and_higher_categories()

    print('работа выполнена успешно!')


if __name__ == '__main__':
    main()