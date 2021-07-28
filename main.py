from matplotlib import pyplot as plt
import numpy as np
import random


def recta_regressio (trainData):
    n = len(trainData[0])
    xav,yav=0,0
    for i in range(n):
        xav = xav + trainData[0][i]
        yav = yav + trainData[1][i]
    xav,yav = xav/n , yav/n
    a,xst = 0,0
    for i in range(n):
        a = a + (trainData[0][i] - xav) * (trainData[1][i] - yav)
        xst = xst + (trainData[0][i] - yav) ** 2
    if (xst == 0):
        a = 0
    else:
        a = a/xst
    b = yav - a * xav
    return (a,b)


def llegir_dades():
    fitxerDades = open("dataset.txt","r")
    dadesLines = fitxerDades.readlines()
    n = int(dadesLines[0])
    trainData = [[],[]]
    for i in range(1, n+1):
        a,h = dadesLines[i].split(' ')
        trainData[0].append(int(a))
        trainData[1].append(int(h))
    m = int (dadesLines[n+1])
    predictData=[[]]
    for i in range(n+2,n+m+2):
        a = dadesLines[i]
        predictData[0].append(int(a))
    return (trainData, predictData)


def accuracy(testData,a,b):
    error = 0.0
    for i in range(len(testData[0])):
        error = error + (a * testData[0][i] + b - testData[1][i] ** 2)
    error = error/len(testData[0])
    return error


def plotline(trainData,a,b):
    xmin,xmax=1000,0
    for x in trainData[0]:
        xmin = min(xmin,x)
        xmax = max(xmax,x)
    x = [xmin,xmax]
    y = [a * xmin + b, a * xmax + b]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(trainData[0],trainData[1])
    ax.plot(x,y,c = 'red')
    ax.set_xlabel('age(years)')
    ax.set_ylabel('height(cm')
    plt.show()


def main():
    trainData,predictData = llegir_dades()
    ind = int (9.0 * len(trainData[0])/10)
    testData = [[],[]]
    testData[0] = trainData[0][ind:]
    testData[1] = trainData[1][ind:]
    trainData[0] = trainData[0][ind:]
    trainData[1] = trainData[1][ind:]
    a,b = recta_regressio(trainData)
    print('A: ',a,'B: ',b)
    acc = accuracy(testData,a,b)
    print('Squared distance error of: ',str(acc))
    if (acc>200):
        print('It is a bad model')
    elif(acc>100):
        print('It is a decent model')
    else:
        print('is a good model')
    for i,x in enumerate(predictData[0]):
        print('Predicted height: ' + str(i+1) + ' is ' + str(a+x+b) + 'cm')
    plotline(trainData,a,b)


if __name__ == '__main__':
    main()