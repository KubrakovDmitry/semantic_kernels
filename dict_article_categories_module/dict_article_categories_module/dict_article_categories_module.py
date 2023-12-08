def dict_article_categories():
   
    # переменные для статистики работы модуля выработки словарей категории статей
    emptryStrings = 0
    uncorrectTriples = 0
    correctTriples = 0
    statistics = open('statistics', 'w')

    second_el_triple = '<http://purl.org/dc/terms/subject>'


    dict_ac = {}

    paths = [
                '..\\..\\..\\Файлы Dbpedia\\Dataset 3.9\\article_categories_ru.ttl\\article_categories_ru.ttl',
                '..\\..\\..\\Файлы Dbpedia\\Dataset 3.9\\article_categories_en_uris_ru.ttl\\article_categories_en_uris_ru.ttl',
                '..\\..\\..\\Файлы Dbpedia\\Dataset 3.9\\article_categories_en.ttl\\article_categories_en.ttl'
            ]

    counter = 0
    for path in paths:
        f = open(path, 'r', encoding='utf-8')
        print(path)
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
            if second_el_triple in triple:
                correctTriples += 1
                # если такой ресурс-ключ уже встречалась, то пополняем её список вышестоящих категорий
                if triple[0] in dict_ac:
                    dict_ac[triple[0]].append(triple[2].rstrip(' .\n'))
                # в противном случае, для новой ресурс-ключа создаётся свой список 
                else:
                    dict_ac[triple[0]] = [triple[2].rstrip(' .\n')]
            if counter%1000000 == 0:
                print('переработано записей ', counter)
        
        f.close()
   
    print ('не триплетов (пустых строк): ', emptryStrings)
    print ('некорректных триплетов: ', uncorrectTriples)
    print ('корректных триплетов: ', correctTriples)
    print ('не триплетов (пустых строк): ', emptryStrings, file=statistics)
    print ('некорректных триплетов: ', uncorrectTriples, file=statistics)
    print ('корректных триплетов: ', correctTriples, file=statistics)
        
    statistics.close()

    return dict_ac

def main():

    print('This is the dict_article_categories_module program!')

    dict_out_put = dict_article_categories()

    print('работа завершилась успешно!')


if __name__ == '__main__':
    main()
