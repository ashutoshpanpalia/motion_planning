import numpy as np
import matplotlib.pyplot as plt
from tree_node import Node
from collision_check import collision_check

class RRT:
    def __init__(self,map, start, end, radius=25.0, dist=10,viz=True, num_itr=2000):
        self.map = map
        self.start= Node(start[0],start[1])
        self.start.parent= None
        self.end = Node(end[0],end[1])
        self.radius = radius
        self.dist= dist
        self.tree=[self.start]
        self.num_itr = num_itr
        self.viz=viz

    def random_point(self):
        x = np.random.randint(0, self.map.shape[1])
        y = np.random.randint(0, self.map.shape[0])
        return [x, y]

    
    def find_neareast_point(self, x_rand, y_rand):
        point_comp= np.array([x_rand, y_rand])
        dist = np.inf
        for nodes in self.tree:
            curr_point  = np.array([nodes.x, nodes.y])
            curr_dist        = np.linalg.norm(curr_point - point_comp)
            if curr_dist < dist:
                nearest_point = curr_point
                nearest_node = nodes
                dist = curr_dist

        return nearest_node
    
    def move_d_to_rand_point(self, nearest_point, x_rand, y_rand):
        nearest_point = np.array(nearest_point)
        rand_point = np.array([x_rand, y_rand])

        direction = rand_point - nearest_point
        length = np.linalg.norm(direction)

        if length == 0:
            return nearest_point.tolist()

        step = min(self.dist, length)
        new_point = nearest_point + (direction / length) * step
        # Clamp to map bounds
        new_point[0] = np.clip(new_point[0], 0, self.map.shape[1] - 1)
        new_point[1] = np.clip(new_point[1], 0, self.map.shape[0] - 1)
        # Convert to int grid coordinates
        return [int(round(new_point[0])), int(round(new_point[1]))]


    def check_collision(self, x_near,y_near, x_d, y_d):
        a=collision_check(self.map, x_near,y_near, x_d, y_d)
        return(a.result())
        

    def add_valid_node(self,node_near,x_d,y_d):
        node_child=Node(x_d,y_d)
        node_parent=node_near
        node_child.parent=node_parent
        self.tree.append(node_child)



    def is_goal_achieved(self, x_d, y_d):
        goal=np.array([self.end.x,self.end.y])
        last_pt=np.array([x_d,y_d])
        d= np.linalg.norm(goal - last_pt)
        if d<=self.radius: 
            return True
        
        else:
            return False

    def extract_shortet_path(self):
        p=[[self.end.x,self.end.y]]
        d=len(self.tree)
        node = self.tree[d-1]
        p.append([node.x,node.y])

        while node.parent is not None:
            parent = node.parent            
            p.append([parent.x,parent.y])
            node = parent

        
        return p



    def rrt_path(self):
        #Basic conditions and edge cases check:
        h, w = self.map.shape

        cond3 = 0 <= self.start.x < w
        cond4 = 0 <= self.end.x   < w
        cond5 = 0 <= self.start.y < h
        cond6 = 0 <= self.end.y   < h

        if not (cond3 and cond4 and cond5 and cond6):
            return []

        cond1 = self.map[self.start.y, self.start.x] == 0
        cond2 = self.map[self.end.y, self.end.x] == 0


        if cond1 and cond2 and cond3 and cond4 and cond5 and cond6:
            if self.viz:
                itr=0
                plt.imshow(self.map, cmap='gray_r', origin='lower')
                plt.scatter(self.start.x, self.start.y, c='red', s=50)
                plt.scatter(self.end.x, self.end.y, c='green', s=50)
                plt.ion()

                while itr <=self.num_itr:
                    itr+=1
                    p=[]
                    [x_rand, y_rand] = self.random_point()
                    
                    node_near=self.find_neareast_point(x_rand, y_rand)
                    
                    [x_near, y_near]= [node_near.x,node_near.y]
                    
                    [x_d, y_d]=self.move_d_to_rand_point([x_near,y_near],x_rand, y_rand)
                    if not self.check_collision(x_near,y_near,x_d,y_d):
                        
                        #True for no collision
                        self.add_valid_node(node_near,x_d,y_d)
                        plt.plot([x_near, x_d], [y_near, y_d], 'b-', linewidth=0.5)
                        plt.pause(0.01)
                        if self.is_goal_achieved(x_d, y_d):
                            plt.plot([x_d,self.end.x], [y_d,self.end.y], 'b-', linewidth=0.5)
                            p= self.extract_shortet_path()
                            return p
                    else:
                        continue

                return p
            
            else:
                
                itr=0
                while itr <=self.num_itr:
                    itr+=1
                    p=[]
                    [x_rand, y_rand] = self.random_point()
                    node_near=self.find_neareast_point(x_rand, y_rand)
                    [x_near, y_near]= [node_near.x,node_near.y]
                    [x_d, y_d]=self.move_d_to_rand_point([x_near,y_near],x_rand, y_rand)
                    if not self.check_collision(x_near,y_near,x_d,y_d):
                        self.add_valid_node(node_near,x_d,y_d)
                        if self.is_goal_achieved(x_d, y_d):
                            p= self.extract_shortet_path()
                            return p
                    else:
                        continue

                return p
        else:
            return []



if __name__ == '__main__':
    map =np.loadtxt('map2.txt')
    start= np.random.randint([0,0],[map.shape],2)
    end= np.random.randint([0,0],[map.shape],2)
    motion_planning = RRT(map,start,end)
    path_1 = motion_planning.rrt_path()
    xs, ys = zip(*path_1)

    plt.imshow(map, cmap='gray_r', origin='lower')
    plt.scatter(start[0],start[1], c='red', s=20)
    plt.scatter(end[0],end[1], c='green', s=20)
    plt.scatter(xs, ys, c='blue', s=2)
    plt.pause(5)
    plt.show()