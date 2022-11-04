import numpy as np
import pandas as pd
import math
import random

arr = 2 ** 16

def Euclid(point1, point2):
    D = len(point1)
    sum = 0.000
    #float
    for i in range(D):
        sum = sum + (point1[i] - point2[i]) ** 2
    return math.sqrt(sum)


def K_Means(hashset, k, max_iteration):
    n = len(hashset)
    centroid = []  
    # the coordinates of each centroid
    assigned_to = [-1] * n  
    # the centroid number each point assigneds to
    loss = []  
    # store the losses after each iterating
    clusterChanged = True
    # init centroid
    idx = random.sample(list(range(n)), k)
    for i in idx:
        centroid.append(hashset[i])
    # start k-means
    loss_iteration = 0  
    # the current loss_iteration of clustering
    while clusterChanged and loss_iteration < max_iteration:  
        # when cluster doesn't change or reaches the max iteration, stop
        clusterChanged = False
        tmp_loss = 0  
        # the loss after each loss_iteration
        # for each point, find their closest centroid
        for i in range(n):  
            # each point
            min_dist = arr
            closest_centroid = 0
            for j in range(k):  
                # calculate the closest centroid
                tmp_dist = Euclid(hashset[i], centroid[j])
                if tmp_dist < min_dist:
                    min_dist = tmp_dist
                    closest_centroid = j
            if assigned_to[i] != closest_centroid:  
                # assign the closest centroid to each point
                assigned_to[i] = closest_centroid
                clusterChanged = True
        # update centroids using k-means of points in each cluster
        for x in range(k):
            tmp_x = []
            for point_idx, assigned in enumerate(assigned_to):
                if assigned == x:
                    tmp_x.append(hashset[point_idx])
            centroid[x] = np.mean(tmp_x, axis=0)
        # calculate loss
        for point_idx in range(n):
            tmp_loss = tmp_loss + Euclid(hashset[point_idx], centroid[assigned_to[point_idx]]) ** 2 
        tmp_loss = tmp_loss / n 
        loss.append(tmp_loss)
        loss_iteration = loss_iteration + 1
        print()
        print('after {} iteration, the loss is:'.format(loss_iteration), tmp_loss)
    return centroid, assigned_to, loss

if __name__ == '__main__':
    file = pd.read_csv('Project3_Power_Consumption.csv')
    hashset = []
    for i in range(len(file)):
        hashset.append([float(file['Global_active_power'].values[i]), float(file['Global_reactive_power'].values[i]),
                        float(file['Voltage'].values[i]), float(file['Global_intensity'].values[i]),
                        float(file['Sub_metering_1'].values[i]), float(file['Sub_metering_2'].values[i]), float(file['Sub_metering_3'].values[i])])
    for k in range(2, 21):
        print('For K = {}:'.format(k))
        centroid, assigned_to, loss = K_Means(hashset, k, 50)
        for i_index, centroid in enumerate(centroid):
            print()
            print('The coordinates of centroid {}:'.format(i_index + 1), centroid)
            print()
            print(assigned_to.count(i_index), 'points are assigned to centroid', i_index + 1)