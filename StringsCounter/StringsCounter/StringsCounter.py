paths = [
        'E:\\MAI\\Dissertation\\program part\\generateIDs\\generateIDs\\trio triplets with IDs.txt'
    ]

CL = open('CountLines.csv', 'w')

#str_en = '\"\"@en'
#count_en = 0

for path in paths:
    countLines = 0
    print(path)
    f = open(path, 'r', encoding='utf-8') 
    row = f.readline()
    #if str_en in row:
    #    count_en += 1
    while row:
        try:
            if '\n' == row:
                row = f.readline()
            else:
                countLines += 1
                row = f.readline()
        except:
            print('Ошибка кодировки!')
            row = f.readline()
        if countLines % 100000 == 0:
            print(countLines)
  
    f.close()
    print(path, countLines, file = CL)
    print(path, '-',  countLines)
    #print(str_en, '-',  count_en)

CL.close()
print('Вычисления закончены!')
print('Нажмите любую клавишу!')
