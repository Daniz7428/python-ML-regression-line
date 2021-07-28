import matplotlib.pyplot as plt
import numpy as np
from random import randint


def plotDataset(trainDataset,predictDataset):
    plt.scatter(trainDataset[0],trainDataset[1])
    plt.show()


def saveDataset(trainDataset,predictDataset):
    dataFile = open('dataset.txt','w')
    n = len(trainDataset[0])
    m = len(predictDataset[0])
    dataFile.write(str(n)+"\n")
    for i in range (n):
        a = trainDataset[0][i]
        h = trainDataset[1][i]
        dataFile.write(str(a)+' '+str(h)+'\n')
    dataFile.write(str(m)+'\n')
    for i in range(m):
        a = predictDataset[0][i]
        dataFile.write(str(a)+ '\n')
    dataFile.close()


def main():
    e = 10
    n = 30
    m = 10
    trainDataset = [[],[]]
    predictDataset = [[]]
    for i in range (n):
        age = randint(8,20)
        height = age*4 + 100 + randint(-e,e)
        trainDataset[0].append(age)
        trainDataset[1].append(height)
    for i in range(m):
        age = randint(8,20)
        predictDataset[0].append(age)
    plotDataset(trainDataset,predictDataset)
    saveDataset(trainDataset,predictDataset)


if __name__=='__main__':
    main()
