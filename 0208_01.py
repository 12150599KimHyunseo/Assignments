class Graph():
    def __init__(self,size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    print(' ', end=' ')
    for v in range(g.size):
        print(store_stack[v], end=' ')
    print()
    for row in range(g.size):
        print(store_stack[row], end=' ')
        for col in range(g.size):
            print(g.graph[row][col], end=' ')
        print()
    print()


G1 = None
store_stack = [['GS25', 30], ['seven_ELEVEN', 10], ['CU', 60], ['MINI_STOP', 90], ['Emart24', 40]]
GS25, seven_ELEVEN, CU, MINI_STOP, Emart24 = 0, 1, 2, 3, 4
stack = []
visited_ary = []

g_size = 5
G1 = Graph(g_size)
G1.graph[GS25][CU] = 1; G1.graph[GS25][seven_ELEVEN] = 1;
G1.graph[seven_ELEVEN][GS25] = 1; G1.graph[seven_ELEVEN][CU] = 1; G1.graph[seven_ELEVEN][MINI_STOP] = 1;
G1.graph[CU][GS25] = 1; G1.graph[CU][seven_ELEVEN] = 1; G1.graph[CU][MINI_STOP] = 1;
G1.graph[MINI_STOP][seven_ELEVEN] = 1; G1.graph[MINI_STOP][CU] = 1; G1.graph[MINI_STOP][Emart24] = 1;
G1.graph[Emart24][MINI_STOP] = 1;

print('## 편의점 그래프 ##')
print_graph(G1)

current = 0
stack.append(current)
visited_ary.append(current)
max_store = current
max_stack = store_stack[current][1]

while len(stack) != 0:
    next = None
    for vertex in range(5):
        if G1.graph[current][vertex] == 1:
            if vertex in visited_ary:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visited_ary.append(current)
        if store_stack[current][1] > max_stack:
            max_store = current
            max_stack = store_stack[current][1]
    else:
        current = stack.pop()


print('허니버터칩 최대 보유 편의점(개수) --> ', store_stack[max_store][0], '  ', max_stack, '개')
