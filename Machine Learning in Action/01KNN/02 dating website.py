# coding:utf-8
"""
Time:2017.09.02
Author:kevinelstri
"""
# dating website by KNN
import numpy as np


def readSet():
    data = []
    labels = []
    for line in open('02 datingTestSet_800.txt').readlines():
        line = line.strip()
        line = line.split('\t')
        da = []
        for i in range(len(line) - 1):
            da.append(float(line[i]))
        data.append(da)
        labels.append(line[-1])
    return data, labels


def Dis(new_data, data, labels):
    outer = []
    for i in range(len(new_data)):
        inner = []
        for j in range(len(data)):
            dis = ((float(new_data[i][0])-float(data[j][0]))**2 + (float(new_data[i][1])-float(data[j][1]))**2 + (float(new_data[i][2])-float(data[j][2])**2))**0.5
            inner.append(dis)
        outer.append(inner)
    print np.array(outer)
    print type(outer)

    forcast_labels = []  # 预测结果
    for i in range(len(outer)):
        min_dis = min(outer[i])
        index_dis = outer[i].index(min_dis)
        new_labels = labels[index_dis]
        forcast_labels.append(new_labels)
    return forcast_labels

if __name__ == '__main__':
    data, labels = readSet()
    # print np.array(data)
    # print labels

    new_data = []
    new_labels = []
    for line in open('02 datingTestSet_200.txt').readlines():
        line = line.strip()
        line = line.split('\t')
        new = []
        for i in range(len(line)-1):
           new.append(line[i])
        new_data.append(new)
        new_labels.append(line[-1])

    forcast_labels = Dis(new_data, data, labels)

    # 准确率
    correct_num = 0
    for i in range(len(forcast_labels)):
        if forcast_labels[i] == new_labels[i]:
            correct_num += 0
        else:
            correct_num += 1
    print correct_num
    correct_rate = correct_num/(len(forcast_labels)+0.0)
    print correct_rate

