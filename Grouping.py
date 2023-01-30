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
for x in range(0,max_x):
    for y in range(0,max_y):
        if divided_space[x,y] is None or len(divided_space[x,y]) == 1:
                pass
        else:
            for a in range(0,len(divided_space[x,y])):
                for b in range(a+1,len(divided_space[x,y])):
                    index1 = divided_space[x,y][a]
                    index2 = divided_space[x,y][b]
                    if not(point_cloud[index1,2] == point_cloud[index2,2]):
                        # if points are within d to each other, merge their groups
                        if is_close(index1,index2,point_cloud,d):
                            point_cloud = merge_groups(point_cloud[index1,2],point_cloud[index2,2],point_cloud)

# Check between adjacent groups
for x in range(0,max_x):
    for y in range(0,max_y):
        if not divided_space[x,y] is None:
            # DO NOT change the order of the logic statements or it will try to reach outside the array boundaries
            # check with x+1,y
            if x+1 >= max_x or divided_space[x+1,y] is None:
                pass
            else:
                point_cloud = check_between_groups(x,y,x+1,y,divided_space,point_cloud,d)
            # check with x,y+1
            if y+1 >= max_y or divided_space[x,y+1] is None:
                pass
            else:
                point_cloud = check_between_groups(x,y,x,y+1,divided_space,point_cloud,d)
            # check with x+1,y+1                
            if x+1 >= max_x or y+1 >= max_y or divided_space[x+1,y+1] is None:
                pass
            else:
                point_cloud = check_between_groups(x,y,x+1,y+1,divided_space,point_cloud,d)

np.set_printoptions(precision=3, suppress=True)
# print(point_cloud)

keys = list(Counter(point_cloud[:,2]).keys())
values = list(Counter(point_cloud[:,2]).values())

# for i in range(0,len(keys)):
#     print('Group',i,'has',values[i],'points')

# print(keys)
# print(values)

storage = np.zeros((len(keys),3),dtype=object)
# [color, string, points]

for i in range(0,len(keys)):
    storage[i,0] = "#"+''.join([random.choice('0123456789ABCDEF') for c in range(6)])
    if values[i] ==1:
        storage[i,1] = 'G '+str(i)+'- 1 point'
    else: 
        storage[i,1] = 'G '+str(i)+'- '+str(values[i])+' points'
    storage[i,2] = []
    for j in range(0,N):
        if point_cloud[j,2] == keys[i]:
            storage[i,2] = np.append(storage[i,2],int(j))

fig = plt.figure()
ax = plt.subplot(111)

for i in range(0,len(keys)):
    index = np.array(storage[i,2][:],dtype=int)
    ax.plot(point_cloud[index[:],0],point_cloud[index[:],1],'.',c=storage[i,0],label=storage[i,1])

# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

# plt.plot(point_cloud[:,0],point_cloud[:,1],'.',c="#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)]))
plt.show()