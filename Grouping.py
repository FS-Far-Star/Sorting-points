import numpy as np
import matplotlib.pyplot as plt

N = 10 # Number of points
scaling = 100 # Maximum
d = 5 # Grouping Distance

point_cloud = np.random.rand(N,2)*scaling

temp = np.zeros((N,3))
temp[:,:-1] =point_cloud
point_cloud = temp

max_x = int(np.max(point_cloud[:,0])//(2*d)+1)
max_y = int(np.max(point_cloud[:,1])//(2*d)+1)

divided_space = np.empty((max_x,max_y), dtype=object)

for i in range(0,N):
    x = int(point_cloud[i,0]//(2*d))
    y = int(point_cloud[i,1]//(2*d))
    if divided_space[x,y] is None:
        divided_space[x,y] = i
    else:
        divided_space[x,y] = np.append(divided_space[x,y],i)

print(divided_space)

plt.plot(point_cloud[:,0],point_cloud[:,1],'.')
plt.show()