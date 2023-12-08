import removingPunctuation
import os


directoryPath = '..\\..\\..\\tasks\\Task_3\\kernels'

clusterPath = '..\\..\\..\\program part\\clusterization\\clusterization\\result.txt'

clusterFile = open(clusterPath, 'r', encoding='utf8')

counter = 0 
counterfile = 0

line = clusterFile.readline()
while line:
    #print('line =', line)
    text, numberCluster = line.split('<---*--->')
    text = removingPunctuation.rmPunct(text)
    numberCluster = numberCluster.strip()
    #print('numberCluster = ', numberCluster)
    nameDirKernel = os.path.join(directoryPath, numberCluster)
    if not os.path.isdir(nameDirKernel):
        os.mkdir(nameDirKernel)
    #print('nameDirKernel = ', nameDirKernel)


    kernelFileName = os.path.join(nameDirKernel, str(counterfile)+'.txt')
    kernelFile = open(kernelFileName, 'w', encoding='utf8')
    kernelFile.write(text)
    kernelFile.close()

    counterfile += 1
    counter += 1
    if counter % 100000 == 0:
        print(f'переработа {counter} записей')

    line = clusterFile.readline()


print('Работа программы успешно завершена!')

