import numpy as np
import pickle


# модель без применения семантических ядер
def originalModel():
    pathList = '..\\..\\..\\tasks\\Task_2\\writtenList.txt'
    pathVectorsTD = '..\\..\\..\\tasks\\Task_2\\vectorsTD.txt'
    pathModel = '..\\..\\..\\tasks\\Task_2\\model.pkl'

    vectors = np.loadtxt(pathVectorsTD, encoding='utf8')
    print(f'Тип vectors - {type(vectors)}')
    print(f'vectors[0] - {vectors[0]}')
    print(f'vectors[1] - {vectors[1]}')
    print(f'vectors[2] - {vectors[2]}')
    print(f'vectors - {vectors}')

    model = pickle.load(open(pathModel, 'rb'))
    print(f'labels - {model.labels_}')

    

if __name__ == '__main__':
    originalModel()
    print('работа программы успешно завершена!')
