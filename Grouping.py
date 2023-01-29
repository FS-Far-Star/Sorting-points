from functions import *

N = 100 # Number of points
scaling = 100 # Maximum
d = 10 # Grouping Distance

point_cloud = np.random.rand(N,2)*scaling

temp = np.transpose(np.arange(0,N))
point_cloud = np.column_stack((point_cloud,temp))

max_x = int(np.max(point_cloud[:,0])//(2*d)+1)
max_y = int(np.max(point_cloud[:,1])//(2*d)+1)

divided_space = np.empty((max_x,max_y), dtype=object)

# Split points into (2d)^2 grid
for i in range(0,N):
    x = int(point_cloud[i,0]//(2*d))
    y = int(point_cloud[i,1]//(2*d))
    if divided_space[x,y] is None:
        divided_space[x,y] = [i]
    else:
        divided_space[x,y] = np.append(divided_space[x,y],i)
# print(divided_space)

# Group self-check
for i in range(0,max_x):
    for j in range(0,max_y):
        if divided_space[x,y] is None or len(divided_space[x,y]) == 1:
                pass
        else:
            for a in range(0,len(divided_space[x,y])):
                for b in range(a+1,len(divided_space[x,y])):
                    # if points are within d to each other, merge their groups
                    if is_close(a,b,point_cloud,d):
                        a_group = point_cloud[a,2]
                        b_group = point_cloud[b,2]
                        point_cloud = merge_groups(a_group,b_group,point_cloud)


print(point_cloud)

plt.plot(point_cloud[:,0],point_cloud[:,1],'.')
plt.show()