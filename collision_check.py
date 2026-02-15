import numpy as np
import matplotlib.pyplot as plt

class collision_check:
    def __init__(self, map, x1,y1,x2,y2):
        self.map = map
        self.x1= x1
        self.y1 = y1
        self.x2 = x2
        self.y2 =y2

        self.collision_check = True

    def points_from_start_2_end(self):
        t=0
        step_size = 0.1
        point_list = []
        dist= np.linalg.norm(np.array([self.x2 - self.x1, self.y2 - self.y1]))

        while t<=1:
            x= int(t*self.x1 +(1-t)*self.x2)
            y= int(t*self.y1 +(1-t)*self.y2)

            t += step_size/dist
            point_list.append([x,y]) 

        return point_list
    
    def result(self):
        point= self.points_from_start_2_end()
        for x,y in point:
            if self.map[x,y]==0:
                self.collision_check = False
                break

        return self.collision_check
    
    def viz_collision_check(self):
        point= self.points_from_start_2_end()
        xs, ys = zip(*point)
        plt.imshow(self.map, cmap='gray_r', origin='lower')
        plt.scatter(xs, ys, c='blue', s=2)
        plt.show()

                




        

    

        