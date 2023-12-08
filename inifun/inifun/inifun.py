def getPath(nameFile):
    f = open('paths.ini', 'r', encoding='utf-8')
    string = 'the some string'
    while string:
        string = f.readline()
        if string.find(nameFile) != -1:
            return string
    f.close()

def main():
    print(getPath('article_categories_en.ttl'))
if __name__ == '__main__':
    main()