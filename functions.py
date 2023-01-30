import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import random

def is_close(a,b,point_cloud,d):
    distance = np.sqrt((point_cloud[a,0] - point_cloud[b,0])**2 + (point_cloud[a,1] - point_cloud[b,1])**2)
    if distance <= d:
        # print('True')
        return True
    else:
        return False
    
def merge_groups(a_group,b_group,point_cloud):
    # print('merged group',a_group,'and group',b_group)
    N = len(point_cloud[:,0])
    for i in range(0,N):
        if point_cloud[i,2] == b_group:
            point_cloud[i,2] = a_group
    # print(point_cloud)
    return point_cloud

def check_between_groups(x1,y1,x2,y2,divided_space,point_cloud,d):
    group1 = [point_cloud[i,2] for i in range(0,len(divided_space[x1,y1]))]
    group2 = [point_cloud[i,2] for i in range(0,len(divided_space[x2,y2]))]
    distinct_groups = len(list(Counter(group1).keys())) + len(list(Counter(group2).keys()))     # Number of groups within the two sections
    max_merge = distinct_groups - 1
    merge_counter = 0
    for i in range(0,len(divided_space[x1,y1])):
        for j in range(0,len(divided_space[x2,y2])):
            if merge_counter >= max_merge:
                pass
            else: 
                index1 = divided_space[x1,y1][i]
                index2 = divided_space[x2,y2][j]
                if not(point_cloud[index1,2] == point_cloud[index2,2]):
                    if is_close(index1,index2,point_cloud,d):
                        point_cloud = merge_groups(point_cloud[index1,2],point_cloud[index2,2],point_cloud)
                        merge_counter += 1
    return point_cloud