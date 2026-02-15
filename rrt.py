import numpy as np
from tree_node import Node
from collision_check import collision_check

class RRT:
    def __init__(self,map, start, end, radius, dist):
        self.map = map
        self.start= Node(start)
        self.end = Node(end)
        self.radius = radius
        self.dist= dist
        self.path=[self.start]

    def random_point(self):
        [x_rand,y_rand]= np.random.randint([0,0],[self.map.shape],2)
        return [x_rand,y_rand]
    
    def find_neareast_point(self, x_rand, y_rand):
        point_comp= [x_rand, y_rand]
        dist = np.inf
        for nodes in self.path:
            curr_point  = [nodes.x, nodes.y]
            curr_dist        = np.linalg.norm(curr_point - point_comp)
            if curr_dist < dist:
                nearest_point = curr_point

        return nearest_point
    
    def move_d_to_rand_point(self,nearest_point,x_rand, y_rand ):
        dist = np.linalg.norm(nearest_point- [x_rand, y_rand])
        new_x = int((nearest_point[0]*(dist - self.dist) + x_rand*(dist)) / dist)
        new_y = int((nearest_point[1]*(dist - self.dist) + y_rand[1]*(dist)) / dist)
        return [new_x, new_y]



    def check_collision(self, x_near,y_near, x_d, y_d):
        a=collision_check(self.map, x_near,y_near, x_d, y_d)
        return(a.result())
        

    def add_valid_node(self,x_near,y_near,x_d,y_d):
        pass

    def is_goal_achieved(self, x_d, y_d):
        pass

    def extract_path(self):
        pass




