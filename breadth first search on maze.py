#!/usr/bin/env python
# coding: utf-8

# In[6]:


from collections import deque


# In[7]:


class Queue:
    def __init__(self):
        self.items=deque()
        
    def is_empty(self):
        return not self.items
    
    def enqueue(self,item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.popleft()
    
    def peek(self):
        return self.items[0]
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)


# In[5]:


q=Queue()
q.enqueue(1)
print(q.peek())
q.enqueue('a')
print(q.dequeue())
print(q.size())


# In[8]:


maze=[[0]*4 for row in range(4)]
maze[0][2]='*'
maze[2][1]='*'
maze[2][3]='*'
maze


# In[9]:


offsets={
    'right':(0,1),
    'left':(0,-1),
    'up':(-1,0),
    'down':(1,0),
}


# In[10]:


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


# In[11]:


def get_path(predecessors, start, goal):
    path=[]
    path.append(goal)
    value=goal
    while value!=start:
        path.append(predecessors[value])
        value=predecessors[value]
        
    return path[::-1]
        


# In[12]:


def bfs(maze, start, goal):
    queue=Queue()
    queue.enqueue(start)
    predecessors={start:None}
    while not queue.is_empty():
        current_cell=queue.dequeue()
        if current_cell==goal:
            return get_path(predecessors, start, goal)
            
        for direction in ['up','right','down','left']:
            row_offset,column_offset=offsets[direction]
            neighbor=(current_cell[0]+row_offset,current_cell[1]+column_offset)
            #print(neighbor)
            if is_legal_pos(maze,neighbor) and neighbor not in predecessors:
                queue.enqueue(neighbor)
                #print(stack)
                predecessors[neighbor]=current_cell
    return None


# In[13]:


way=bfs(maze,(0,0),(3,3))


# In[14]:


print(way)


# In[ ]:




