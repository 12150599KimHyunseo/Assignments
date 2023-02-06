class Node:
    def __init__(self):
        self.flink = None
        self.blink = None
        self.data = None


def print_nodes(start):
    current = start
    if current.flink == None:
        return
    print("정방향 : ", end=' ')
    print(current.data, end=' ')
    while current.flink != None:
        current = current.flink
        print(current.data, end=' ')
    print()
    print("역방향 : ", end=' ')
    print(current.data, end=' ')
    while current.blink != None:
        current = current.blink
        print(current.data, end=' ')


head, current, pre = None, None, None
memory = list()
data_array = [1, 2, 3, 4, 5]

if __name__ == "__main__":
    node = Node()
    node.data = data_array[0]
    head = node
    memory.append(node)

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.flink = node
        node.blink = pre
        memory.append(node)


print_nodes(head)
