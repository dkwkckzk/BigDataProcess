from sklearn.neighbors import KNeighborsClassifier
from os import listdir
import numpy as np

def img_to_vector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        line = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(line[j])
    return returnVect 

def create_dataset(directory):
    training_file_list = listdir(directory)
    m = len(training_file_list)
    training_matrix = np.zeros((m, 1024))
    digit_labels = []
    for i in range(m):
        file_names = training_file_list[i]
        file_name = file_names.split('.')[0]
        digit = int(file_name.split('_')[0])
        digit_labels.append(digit)
        training_matrix[i, :] = img_to_vector('%s/%s' % (directory, file_names))
    return training_matrix, digit_labels

def handwriting_class_test(k, trainingMat, hwLabels, testDirectory):
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(trainingMat, hwLabels)
    
    testFileList = listdir(testDirectory)
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img_to_vector('%s/%s' % (testDirectory, fileNameStr))
        classifierResult = knn.predict(vectorUnderTest)
        if (classifierResult != classNumStr): errorCount += 1.0
    
    errorRate = int((errorCount/float(mTest)) * 100) # 에러율을 백분율로 변환 후 소수점을 절사
    return errorCount, errorRate # 에러의 총 수와 에러율 반환

trainingMat, hwLabels = create_dataset('trainingDigits')
errorCounts = []
errorRates = []
for k in range(1, 21):
    errorCount, errorRate = handwriting_class_test(k, trainingMat, hwLabels, 'testDigits')
    errorCounts.append(errorCount)
    errorRates.append(errorRate)

print(*errorCounts, sep = "\n") # 각 k에 대한 에러의 총 수를 한 줄에 한 숫자로 출력
print(*errorRates, sep = "\n") # 각 k에 대한 에러율을 한 줄에 한 숫자로 출력

python3 Student20211743.py trainingDigits testDigits