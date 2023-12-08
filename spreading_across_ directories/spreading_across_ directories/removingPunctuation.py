import string

def rmPunct(line):
    newline = line.replace('@ru', '')
    newline = newline.replace('@en', '')
    newline = newline.replace('http://ru.dbpedia.org/resource/Категория:', '')
    newline = newline.replace('http://dbpedia.org/resource/Category:', '')
    #newline = newline.replace('_', ' ')
    newline = newline.replace('\'<', '')
    newline = newline.replace('>', '')
    newline = newline.replace('[', '')
    newline = newline.replace(']', '')
    #newline = newline.replace('(', '')
    #newline = newline.replace(')', '')
    newline = newline.replace('\'', '')
    newline = newline.replace('\"', '')
    #print(f'Строка после изменений {newline}')
    #newline = newline.translate(str.maketrans('', '', string.punctuation))
    newline = newline.replace(' n ', ' ')
    #newline = newline.replace('.\n', ' ')
    #print(f'Строка после удаления пунктуации {newline}')
    return newline

if __name__ == '__main__':
    file = open('E:\\MAI\\Dissertation\\program part\\largeOpen\\largeOpen\\part_of_unique_ru.txt', 'r', encoding='utf8')
    line = file.readline()
    str_en = '\"\"@en'
    count = 0
    while line:
        if str_en in line:
            line = file.readline()
        else:
            print(f'Строка до изменений: {line}')
            print(f'Cтрока после изменений: {rmPunct(line)}')
            line = file.readline()
        if count > 10:
            break
        count += 1
    print('Работа программы успешно завершена!')
    
