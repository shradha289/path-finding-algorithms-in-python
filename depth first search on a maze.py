#!/usr/bin/env python
# coding: utf-8

# In[26]:


class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
       # return not self.items

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# In[2]:


def read_maze(file_name):
    try:
        with open(file_name) as fh:
            maze=[[char for char in line.strip('\n')] for line in fh]
            num_cols_top_row=len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular")
                    raise SystemExit
            return maze
    except OSError:
        print("There is a problem with the file you have specified")
        raise SystemExit


# In[7]:


maze=read_maze("C:/Users/Dell/Desktop/challenge_maze.txt")
print(maze)


# In[20]:


maze=[[0]*4 for row in range(4)]
maze[0][2]='*'
maze[2][1]='*'
maze[2][3]='*'
maze


# In[30]:


offsets={
    'right':(0,1),
    'left':(0,-1),
    'up':(-1,0),
    'down':(1,0),
}


# In[58]:


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


# In[59]:


def get_path(predecessors, start, goal):
    path=[]
    path.append(goal)
    value=goal
    while value!=start:
        path.append(predecessors[value])
        value=predecessors[value]
        
    return path[::-1]
        


# In[60]:


def dfs(maze, start, goal):
    stack=Stack()
    stack.push(start)
    predecessors={start:None}
    while not stack.is_empty():
        current_cell=stack.pop()
        if current_cell==goal:
            return get_path(predecessors, start, goal)
            
        for direction in ['up','right','down','left']:
            row_offset,column_offset=offsets[direction]
            neighbor=(current_cell[0]+row_offset,current_cell[1]+column_offset)
            #print(neighbor)
            if is_legal_pos(maze,neighbor) and neighbor not in predecessors:
                stack.push(neighbor)
                #print(stack)
                predecessors[neighbor]=current_cell
    return None


# In[61]:


way=dfs(maze,(0,0),(3,3))


# In[62]:


print(way)


# In[ ]:




