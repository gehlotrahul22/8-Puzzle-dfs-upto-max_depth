initial=(" ", 1, 2,
         3,4,5,
         6,7,8)

goal_st=( 7,3,1,
          4,2," " ,
          5, 6 ,8)

max_depth=20


def printChilds(A):
    node=initial
    level=1
    for j in range(len(A)):
        
        print("<----------Level {}---------> ".format(depth_holder[j]))
        print(moves[j])
        printNode(A[j])
        
def printNode(A):
    for i in range(0,9,3):
            print("{} {} {}".format(A[i],A[i+1],A[i+2]))

moves=[" "]
    
def up(A,i):
    A=list(A)
    A[i],A[i-3]=A[i-3],A[i] 
    move.append("Move Up")
    return A
def down(A,i):
    A=list(A)
    A[i],A[i+3]=A[i+3],A[i]
    move.append("Move Down")
    return A
def left(A,i):
    A=list(A)
    A[i],A[i-1]=A[i-1],A[i]
    move.append("Move Left")
    return A
def right(A,i):
    A=list(A)
    A[i],A[i+1]=A[i+1],A[i]
    move.append("Move Right")
    return A


        
def findChilds(Node):

    index=Node.index(" ")
    childs=[]
    if((index+1 in range(0,9)) and (index % 3 != 2)):
        c1=right(Node,index)
        childs.append(c1)
        
    if(index+3 in range(0,9)):
        c2=down(Node,index)
        childs.append(c2)
    
    if(index-3 in range(0,9)):
        c3=up(Node,index)
        childs.append(c3)

    if((index-1 in range(0,9)) and (index % 3 !=0)):
        c4=left(Node,index)
        childs.append(c4)
    return childs
move=[]       
explored=[]
depth_holder=[]
def dfs_traversal(start,goal):
    start=list(start)
    goal=list(goal)
    
    depth=[0]
    queue = [start]
    move.append("Start Node")

    while queue:

        node = queue.pop()
        d=depth.pop()
        mo=move.pop()
        if node not in explored:
            explored.append(node)
            print(node,d)
            depth_holder.append(d)
            moves.append(mo)
            if node==goal:
                return explored
            if d<max_depth:
                neighbours = findChilds(node)
                for neighbour in neighbours:
                    queue.append(neighbour)
                    depth.append(d+1)

def backtrack(Node):
    printNode(Node)
    print("\n/|\ ")
    print(moves[rest.index(Node)])
    print(" | \n")
    for i in range(rest.index(Node)-1,-1,-1):
        if Node in findChilds(rest[i]):
            backtrack(rest[i])
    
rest=dfs_traversal(initial,goal_st)
#print("Total Cost :- ",len(rest)-1)
moves.pop(0)
#printChilds(rest)
print("<---------------Backtracked Path------------------------->")
#backtrack(rest[-1])


