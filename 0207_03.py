import random


class Treenode:
    def __init__(self):
        self.right = None
        self.data = None
        self.left = None


SIZE = 10
memory = list()
root = None
merch = ['레쓰비캔커피', '도시락', '삼각김밥', '코카콜라', '삼다수', '츄파츕스']
sold_data = [random.choice(merch) for _ in range(SIZE)]

print('오늘 판매된 물건(중복O) --> ', sold_data)


if __name__ == "__main__":
    node = Treenode()
    node.data = sold_data[0]
    root = node
    memory.append(node)

    for name in sold_data[1:]:
        node = Treenode()
        node.data = name

        current = root
        while True:
            if name == current.data:
                break
            elif name < current.data:
                if current.left == None:
                    current.left = node
                    memory.append(node)
                    break
                current = current.left
            else:
                if current.right == None:
                    current.right = node
                    memory.append(node)
                    break
                current = current.right


def preorder(node):
    if node == None:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


print("이진 탐색 트리 구성 완료!")

print("오늘 판매된 종류(중복X)-->", end=' ')
preorder(root)
