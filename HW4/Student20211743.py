#!/usr/bin/python3

# 1. trainigDigits을 사전학습한다. training_matrix을 만들 group과 labels 생성
# 2. testDigits을 본격적으로 학습한다. 

import numpy as np
import operator
from os import listdir

# 각 숫자 이미지를 숫자로 인식해야 됨.
# 벡터?로 변경해야 됨

def img_to_vector(filename): # 이미지를 벡터형태로 반환하는 역할만 수행함
    returnVect = np.zeros((1, 1024)) # 1*1024 크기의 0으로 초기화된 numpy 배열 생성(1차원 배열로)
    fr = open(filename)
    for i in range(32): # 각 라인을 읽어온다
        line = fr.readline()
        for j in range(32): # 각 행(라인)을 순회하며 픽셀값을 읽어온다.
            # 해당 픽셀의 값을 정수로 변환하여 벡터에 저장
            # 0 : 배경, 1: 숫자
            returnVect[0, 32*i+j] = int(line[j]) # 해당 위치에 저장한다.
    return returnVect 
            
def create_dataset(directory): # group이랑 labels
    training_file_list = listdir(directory)
    m = len(training_file_list)
    training_matrix = np.zeros((m, 1024))
    digit_labels = []
    for i in range(m):
        file_names = training_file_list[i]
        file_name = file_names.split('.')[0]
        digit = int(file_name.split('_')[0]) # 파일 이름에서 숫자 추출
        digit_labels.append(digit) # 숫자를 라벨 목록에 추가
        training_matrix[i, :] = img_to_vector('%s/%s' % (directory, file_names)) # 이미지 벡터화, 학습 행렬에 추가
    return training_matrix, digit_labels


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
    diffMat = dataSet - inX # 수정
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDisIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDisIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def handw_test(k, training_matrix, digit_labels, testDir):
    testFileList = listdir(testDir)
    error_count = 0.0
    total = len(testFileList)
    for i in range(total):
        file_names = testFileList[i]
        file_name = file_names.split('.')[0]
        digit = int(file_name.split('_')[0])
        vector_test = img_to_vector('%s/%s' % (testDir, file_names))
        classify_result = classify0(vector_test, training_matrix, digit_labels, k)
        if (classify_result != digit): 
            error_count += 1.0
    errorRate = int((error_count / float(total)) * 100)
    return errorRate 

training_matrix, digit_labels = create_dataset('trainingDigits')
error_rates = []
for k in range(1, 21):
    error_rate = handw_test(k, training_matrix, digit_labels, 'testDigits')
    error_rates.append(error_rate)

print(*error_rates, sep = "\n") # 각 k에 대한 에러율을 한 줄에 한 숫자로 출력
