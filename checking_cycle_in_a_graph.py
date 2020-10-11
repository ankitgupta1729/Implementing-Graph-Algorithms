import sys

def cycle_detection(ch_dict, x, y):
    p_1 = [x]
    p_2 = [y]
    while ch_dict[x] != 'root':
        p_1.append(ch_dict[x])
        x = ch_dict[x]
    while ch_dict[y] != 'root':
        p_2.append(ch_dict[y])
    common = None
    while p_1[-1] == p_2[-1]:
        p_1.pop(-1)
        common = p_2.pop(-1)
    t1 = ''.join([str(m) for m in p_1])
    t2 = ''.join([str(n) for n in p_2])
    return (t1 + str(common) + t2[::-1])
def cycle(graph,ch_dict, num, x):
    visited[x - 1] = 'T'
    ch_dict[x] = 'root'
    que = []
    que.append(x)
    while que:
        m = que.pop(0)
        for t in graph[m]:
            if visited[t-1] == 'F':
                que.append(t)
                ch_dict[t] = m
                visited[t - 1] = 'T'
            elif ch_dict[m] != t:
                print(cycle_detection(ch_dict, t, m))


if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("File is not passed as command line argument")
    file_n = sys.argv[1]
    l_list = [line.strip('\n') for line in open(file_n)]
    l = l_list[0].split()
    num = int(l[0])
    x = int(l[1])
    graph = dict()
    for j in range(1, num+1):
        neigh_v = l_list[j].split()
        neigh_v = [int(k) for k in neigh_v]
        graph[j] = neigh_v
    visited = ['F'] * int(num)
    ch_dict = dict()
    cycle(graph, ch_dict, num, x)

    for k in range(1, len(visited)):
        if visited[k] == 'F':
            cycle(graph,ch_dict, num, k+1)
