from bs4 import BeautifulSoup
import os

dirPath = '..\\..\\..\\tasks\\Task_2\\round_2'


filesList = list()
print('получение списка html-файлов')
for root, dirs, files in os.walk(dirPath):
    for file in files:
        filesList.append(os.path.join(root, file))

# создание директории для файлов с отпарсенных текстом из html-документов 
dirName = '..\\..\\..\\tasks\\Task_2\\parsed'
if not os.path.exists(dirName):
    os.mkdir(dirName)
# парсинг файлов из спика файлов
print('парсинг файлов из спсика файлов')
count = 0                               # счётчик не удачных файлов
counter = 0                              
for path in filesList:
    outputpath = dirName + '\\' + 'parsed_' + os.path.basename(path)
    
    if counter % 1000 == 0:
        print(f'переработано {counter} файлов, неудачных файлов {count}')
    inputfile = open(path, "r", encoding='utf8')
    contents = ''
    try:
        contents = inputfile.read()
    except:
        count += 1
        continue
    soup = BeautifulSoup(contents, 'lxml')
    outputfile = open(outputpath, 'w', encoding='utf8')
    text = soup.find('html').text
    print(' '.join(soup.find('html').text.split()), file=outputfile)
    outputfile.close()
    inputfile.close()
    counter += 1
        
    

print(f'число неудачных файлов {count}')
print(f'исходных файлов {len(filesList)}, переработанных файлов {len(filesList) - count}')

print('Работа программы успешно завершена!')