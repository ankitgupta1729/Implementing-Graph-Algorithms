import sys

def Bipartite_Check(graph, num, x):  
    que = []
    que.append(x)
    visited[x - 1] = 'T'
    color[x - 1] = 'R'
    while que:
        m = que.pop(0)
        for k in graph[m]:
            if visited[k-1] == 'F':
                que.append(k)
                visited[k - 1] = 'T'
                if color[m - 1] == 'R':
                    color[k - 1] = 'B'
                else:
                    color[k - 1] = 'R'
            elif color[k - 1] == color[m - 1]:
                print("adjacent vertices %d and %d has same color %s. So, graph is not bipartite" %(k, m, color[m - 1]))

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("File is not passed as command line argument")

    file_n = sys.argv[1]
    l_list = [k.strip('\n') for k in open(file_n)]
    l = l_list[0].split()
    num = int(l[0])
    x = int(l[1])
    graph = dict()
    for k in range(1, num + 1):
	    neigh_v = l_list[k].split()
	    neigh_v = [int(p) for p in neigh_v] 
	    graph[k] = neigh_v
    visited = ['F'] *num
    color = [-1] * num
    x =Bipartite_Check(graph, num, x)
    res = 0
    for t in range(num):
        if visited[t] == 'F':
            res = 1

    if x == 1:
        pass
    elif res == 0 and x == 0: 
        print("Graph is bipartite")
        print('(', end ="")
        for p in range(num):
            if color[p] == 'R':
                print(p+1, end = " ")
        print(')', end =" ")  
        print('(', end ="")
        for p in range(num):
            if color[p] == 'B':
       	        print(p+1, end = " ")
        print(')', end ="")
    elif res == 1:
              for p in range(0, len(visited)):
                   if visited[p] == 'F':
                        x = Bipartite_Check(graph, num, p + 1)
    if x == 0:
        print("Graph is bipartite")
        print('(', end ="")
       	for p in range(num):
            if color[p] == 'R':
                print(p+1, end = " ")
        print(')', end =" ")
        print('(', end ="")
        for p in range(num):
             if color[p] == 'B':
                print(p+1, end = " ")
        print(')', end ="")
