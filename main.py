from rrt import RRT
import numpy as np
import matplotlib.pyplot as plt
map =np.loadtxt('rrt_map2.txt')
h, w = map.shape
start = np.array([
    np.random.randint(0, w),  # x
    np.random.randint(0, h)   # y
])

end = np.array([
    np.random.randint(0, w),
    np.random.randint(0, h)
])

motion_planning = RRT(map,start,end,viz=True)
path_1 = motion_planning.rrt_path()
if path_1==[]:
    print("No valid path")
else:
    xs, ys = zip(*path_1)
    plt.imshow(map, cmap='gray_r', origin='lower')
    plt.scatter(start[0],start[1], c='red', s=20)
    plt.scatter(end[0],end[1], c='green', s=20)
    plt.scatter(xs, ys, c='blue', s=2)
    plt.pause(5)
    plt.show()