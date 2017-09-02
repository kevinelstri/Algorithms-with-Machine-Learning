# coding:utf-8
"""
Time:2017.09.02
Author:kevinelstri
"""
import numpy as np
import random

# kmeans
def readDataSet():
    DataSet = []
    for line in open('testSet.txt').readlines():
        line = line.strip()
        line = line.split('\t')
        Line = []
        for i in range(len(line)):
            Line.append(float(line[i]))
        DataSet.append(Line)
    return np.array(DataSet)


def RandCent(DataSet, k):  # 生成随机的k个聚类中心
    random_num = random.sample(range(len(DataSet)), k)  # 生成k个随机数，随机数的大小范围[0-80）,len(DataSet)=80
    # print random_num  # 随机数
    rand_cent = []
    for i in range(len(random_num)):
        rand_cent.append(DataSet[random_num[i]])
    # print np.array(rand_cent)  # 随机聚类中心
    return np.array(rand_cent)


def dis(data1, data2):
    sum = 0
    for i in range(len(data1)):
        sum += (data1[i] - data2[i])**2
    return sum**0.5


def KMeans(rand_cent, k):
    outer = []  # 质心与点之间的距离
    for i in range(len(rand_cent)):
        inner = []
        for j in range(len(DataSet)):
            inner.append(dis(rand_cent[i], DataSet[j]))
        outer.append(inner)
    # 转置取最小值
    outer = np.array(outer).T
    # print outer
    # print

    Min = [[] for i in range(k)]
    # Min[0].append(1)
    # Min[1].append(2)
    # print Min
    for i in range(len(outer)):
        # print outer[i].tolist()
        # print type(outer[i].tolist())
        min_dis = min(outer[i].tolist())
        # print min_dis
        place = outer[i].tolist().index(min_dis)
        Min[place].append(DataSet[i].tolist())
    print Min  # 每个质心的最小距离点
    print np.array(Min)
    print len(Min)  # 5=k
    print Min[0][0]
    print Min[1]
    print len(Min[0])

    average = []
    for i in range(k):
        for j in range(len(Min[i])):
            ave = []
            first = sum(Min[i][j][0])/len(Min[j])
            second = sum(Min[i][j][1])/len(Min[j])
            ave.append(first)
            ave.append(second)
            average.append(ave)
    print average

    # num = 1
    # if average is rand_cent:
    #     return num
    # else:
    #     KMeans(average, k)
    #     num += 1

if __name__ == '__main__':
    DataSet = readDataSet()
    print len(DataSet)
    rand_cent = RandCent(DataSet, 5)
    print rand_cent
    KMeans(rand_cent, 5)
