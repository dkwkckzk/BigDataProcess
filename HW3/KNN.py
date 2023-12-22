#!/usr/bin/python3

import numpy as np
import operator

def createDataset():
    group = np.array([[1.0, 1.1],[1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels



def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataset = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataset = dataSet - np.tile(minVals, (m, 1))
    normDataset = normDataset / np.tile(ranges, (m, 1))
    return normDataset, ranges, minVals



def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1))
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sotredDisIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sotredDisIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]



if __name__ == "__main__":

    group, labels = createDataset()
    print("group\n", group)
    print("labels = ", labels)
    print(classify0([0, 0], group, labels, 3))