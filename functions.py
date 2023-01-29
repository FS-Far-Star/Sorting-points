import numpy as np
import matplotlib.pyplot as plt

def is_close(a,b,point_cloud,d):
    distance = np.sqrt((point_cloud[a,0] - point_cloud[b,0])**2 + (point_cloud[a,1] - point_cloud[b,1])**2)
    if distance <= d:
        # print('True')
        return True
    else:
        return False
def merge_groups(a_group,b_group,point_cloud):
    N = len(point_cloud[:,0])
    for i in range(0,N):
        if point_cloud[i,2] == b_group:
            point_cloud[i,2] = a_group
            print('merged')
    return point_cloud