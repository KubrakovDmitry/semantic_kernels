import hashlib


listOfTriples = list()
counterRepeat = 0
counter = 0
inputfile = open('E:\\MAI\\Dissertation\\program part\\triplet collection module\\triplet collection module\\newTriplets_en.txt', 'r', encoding='utf8')
outputfile = open ('unique_en.txt', 'w', encoding='utf8')

line = inputfile.readline()
while line:
    counter += 1
    hash_object = hashlib.sha512(line.encode())
    hex_dig = hash_object.hexdigest()
    if hex_dig not in listOfTriples:
        listOfTriples.append(hex_dig)
        outputfile.write(line)
    else:
        counterRepeat += 1
    if (counter%10000 == 0) and (counter != 0): 
        print(f'Переработано {counter}')
        print(f'Повторений в треплетах {counterRepeat}')
    line = inputfile.readline()
print(f'Повторений в треплетах {counterRepeat}')
inputfile.close()
outputfile.close()
print('Работа программы завершена успешно!')