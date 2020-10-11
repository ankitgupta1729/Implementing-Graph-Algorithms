import sys

def bfs_implementation(graph, num, start):
    visited[start - 1] = 'T'
    que = []
    que.append(start)
    while que:
        y = que.pop(0)
        print(y, end = " ")
        for m in graph[y]:
            if visited[m - 1] == 'F':
                que.append(m)
                visited[m - 1] = 'T'
if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("File is not passed as command line argument")
    file_n = sys.argv[1]
    l_list = [li.strip('\n') for li in open(file_n)]
    l = l_list[0].split()
    num = int(l[0])
    start = int(l[1])
    graph = dict()
    for p in range(1, num + 1):
	    neigh_v = l_list[p].split()
	    neigh_v = [int(t) for t in neigh_v] 
	    graph[p] = neigh_v
    visited = ['F'] * int(num)
    bfs_implementation(graph, num, start)
    for j in range(0, len(visited)):
    	if visited[j] == 'F':
    		bfs_implementation(graph, num, j + 1)
