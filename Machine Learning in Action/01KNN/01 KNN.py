# coding:utf-8
"""
Time:2017.09.02
Author:kevinelstri
"""
# KNN
import numpy as np
import operator


def createDataSet():  # 数据及其标签
    group = np.array([[1, 1.1], [1, 1], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def calDis(new_data, dataSet, labels):
    Dis = []
    for i in range(len(dataSet)):
        dis = ((new_data[0] - dataSet[i][0]) ** 2 + (new_data[1] - dataSet[i][1]) ** 2) ** 0.5
        Dis.append(dis)
    minDis = min(Dis)  # 取距离最小的数值
    place = Dis.index(minDis)  # 通过索引对应到原始数据集中的位置
    classify = labels[place]  # 将位置对应到标签上，获取标签分类
    return classify


if __name__ == '__main__':
    group, labels = createDataSet()
    print group
    print labels
    new_data = [0, 0]
    classify = calDis(new_data, group, labels)
    print classify
