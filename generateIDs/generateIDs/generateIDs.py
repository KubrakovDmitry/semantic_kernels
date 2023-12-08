import removingPunctuation

def genIDs():
    paths = [
            '..\\..\\..\\program part\\uniqueTriplets\\uniqueTriplets\\unique_ru.txt',
            '..\\..\\..\\program part\\uniqueTriplets\\uniqueTriplets\\unique_en_ru.txt',
            '..\\..\\..\\program part\\replacing\\replacing\\unique_en2.txt'
        ]
    
    outputf = open('trio triplets with IDs.txt', 'w', encoding='utf8')
    for path in paths:
        print(path)
        prefix = path.split('\\')[-1]
        prefix = prefix.rsplit( ".", 1 )[0] 
        inputf = open(path, 'r', encoding='utf8')
        count = 1
        line = inputf.readline()
        while line:
            if line == '\n':
                line = inputf.readline()
                continue
            id = line
            id = id.rstrip('\n')
            text = removingPunctuation.rmPunct(line)
            print(id + ' <---*---> ' + text, file=outputf)
            line = inputf.readline()
            if count%100000 == 0:
                print(f'Переработано {count} записей')
            count += 1
        inputf.close()
    outputf.close()

if __name__ == '__main__':
    genIDs()
    print('Работа программы завершена!')