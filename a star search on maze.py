#!/usr/bin/env python
# coding: utf-8

# In[8]:


import heapq


# In[9]:


class PriorityQueue:
    def __init__(self):
        self.elements=[]
        
    def is_empty(self):
        return not self.elements
    
    def put(self,item,priority):
        heapq.heappush(self.elements,(priority,item))
        
    def get(self):
        return heapq.heappop(self.elements)[1]
    
    def __str__(self):
        return str(self.elements)


# In[6]:


if __name__=="__main__":
    pq=PriorityQueue()
    print(pq)
    pq.put("deep learning",2)
    pq.put("reinforcement learning",1)
    pq.put("nlp",3)
    print(pq)
    pq.get()
    print(pq.is_empty())
    print(pq)


# In[10]:


maze=[[0]*4 for row in range(4)]
maze[0][2]='*'
maze[2][1]='*'
maze[2][3]='*'
maze


# In[11]:


offsets={
    'right':(0,1),
    'left':(0,-1),
    'up':(-1,0),
    'down':(1,0),
}


# In[12]:


def is_legal_pos(maze,neighbor):
    row,col=neighbor
    #print('row',row,'col',col)
    if row<0 or row>len(maze)-1:
        return False
    if col<0 or col>len(maze[0])-1:
        return False
    if maze[row][col]=='*':
        return False
    return True


# In[13]:


def get_path(predecessors, start, goal):
    path=[]
    path.append(goal)
    value=goal
    while value!=start:
        path.append(predecessors[value])
        value=predecessors[value]
        
    return path[::-1]
        


# In[14]:


def heuristic(goal,neighbor):
    x1,y1=goal
    x2,y2=neighbor
    return abs(x1-x2)+abs(y1-y2)


# In[15]:


def a_star(maze, start, goal):
    pq=PriorityQueue()
    pq.put(start,0)
    predecessors={start:None}
    g_values={start:0}
    while not pq.is_empty():
        current_cell=pq.get()
        if current_cell==goal:
            return get_path(predecessors, start, goal)
        for direction in ['up','right','down','left']:
            row_offset,column_offset=offsets[direction]
            neighbor=(current_cell[0]+row_offset,current_cell[1]+column_offset)
            if is_legal_pos(maze,neighbor) and neighbor not in g_values:
                g_values[neighbor]=g_values[current_cell]+1
                f_value=g_values[neighbor]+heuristic(goal,neighbor)
                predecessors[neighbor]=current_cell
                pq.put(neighbor,f_value)
    return None


# In[16]:


way=a_star(maze,(0,0),(3,3))
print(way)


# In[ ]:




