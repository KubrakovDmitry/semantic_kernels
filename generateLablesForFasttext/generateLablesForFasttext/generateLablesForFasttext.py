import removingPunctuation

path = '..\\..\\..\\program part\\clusterization\\clusterization\\result.txt'
inputfile = open(path, 'r', encoding='utf8')
outputfile = open(path.split('\\')[-1].split()[0] + 'idLabels.txt', 'w', encoding='utf8')

label = '__label__'         # приставка метка для fasttext 
line = inputfile.readline() # строка ID текста c меткой кластера (ядра)
counter = 0                 # счётчик переработанных записей
counter_EOS = 0  
print('работа в цикле начилась')
while line:
        if line == '\n':
            line = inputfile.readline()
            counter_EOS += 1
            continue
        else:
            try:
                id, number = line.split(' <---*---> ')
                print(label + number.replace('\n', ''), removingPunctuation.rmPunct(id), file=outputfile)
                line = inputfile.readline()
                counter += 1
            except:
                print('ошибка кодировки')
            if counter % 100000 == 0:
                print(f'число переработанных записей равно ', counter )
    
outputfile.close()
print('число пустых строк -', counter_EOS)
print('Работа программы успешно завершина!')

