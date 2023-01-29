import numpy as np
import matplotlib.pyplot as plt

N = 100 # Number of points
scaling = 100 # Maximum
d = 10 # Grouping Distance

point_cloud = np.random.rand(N,2)*scaling

temp = np.transpose(np.arange(0,N))
point_cloud = np.column_stack((point_cloud,temp))

max_x = int(np.max(point_cloud[:,0])//(2*d)+1)
max_y = int(np.max(point_cloud[:,1])//(2*d)+1)

divided_space = np.empty((max_x,max_y), dtype=object)

# Group points with (2d)^2
for i in range(0,N):
    x = int(point_cloud[i,0]//(2*d))
    y = int(point_cloud[i,1]//(2*d))
    if divided_space[x,y] is None:
        divided_space[x,y] = [i]
    else:
        divided_space[x,y] = np.append(divided_space[x,y],i)

print(divided_space)

def is_close(a,b,point_cloud,d):
    distance = np.sqrt((point_cloud[a,0] - point_cloud[b,0])**2 + (point_cloud[a,1] - point_cloud[b,1])**2)
    if distance <= d:
        print('True')
        return True
    else:
        return False

# Group self-check
for i in range(0,max_x):
    for j in range(0,max_y):
        if divided_space[x,y] is None:
            pass
        else:
            s = len(divided_space[x,y])
            if s == 1:
                pass
            else:
                for a in range(0,s):
                    for b in range(a+1,s):
                        if is_close(a,b,point_cloud,d):
                            a_group = point_cloud[a,2]
                            b_group = point_cloud[b,2]
                            print(a_group,b_group)
                            for length in range(0,N):
                                if point_cloud[length,2] == b_group:
                                    print('found')
                                    point_cloud[length,2] = a_group

print(point_cloud)

plt.plot(point_cloud[:,0],point_cloud[:,1],'.')
plt.show()