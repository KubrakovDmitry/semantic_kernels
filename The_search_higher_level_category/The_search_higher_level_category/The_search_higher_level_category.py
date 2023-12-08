import dictionary_of_categories_and_higher_categories as dict_cahc
import datetime

def search_hc(dict_chc_param, deep=0, start=None):
    listCatsStart = start
    listCatsRet = listCatsStart

    count = 0

    while count < deep:

        listCatsCur = []

        for item in listCatsStart:
            if item not in dict_chc_param.keys():
                continue

            if dict_chc_param[item] == None:
                continue

            for internal_item in dict_chc_param[item]:
                if (internal_item not in listCatsRet) and (internal_item not in listCatsCur):
                    listCatsCur.append(internal_item)

        listCatsStart = listCatsCur
        listCatsRet.extend(listCatsCur)

        listCatsRet = set(listCatsRet)
        listCatsRet = list(listCatsRet)
        
        count += 1
    
    
    return listCatsRet


def main():

    result_file = open('result file.txt', 'w', encoding='utf-8')
    result_file.close()

    dict_chc = dict_cahc.dictionary_of_categories_and_higher_categories()

    print( 'Введите значение для ограничения ' )
    print('>', end=' ')
    deep = int(input())

    #categories = ''
    counter = 0
    for item in dict_chc.keys():
        result_file = open('result file.txt', 'a', encoding='utf-8')
        counter += 1
        result = search_hc(dict_chc, deep, dict_chc[item])
        if counter%1000 == 0:
            print('item, result = ', item, result)
        print('item, result = ', item, result, file=result_file)
        result_file.close()
    
    print('Работа завершена успешно!')
    #print('result = ', result)
    #for k, v in dict_chc.items():
    #        print(k, ':', v)

if __name__ == '__main__':
    main()