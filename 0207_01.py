def is_queue_full():
    global Size, queue, front, rear
    if rear == Size - 1:
        return True
    return False


def is_queue_empty():
    global Size, queue, front, rear
    if rear == front:
        return True
    return False


def de_queue():
    global Size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    front = front + 1
    data = queue[front]
    queue[front] = None

    for i in range(front+1, rear+1):
        queue[i-1] = queue[i]
        queue[i] = None
    front = -1
    rear = rear - 1

    return data


def en_queue(data):
    global Size, queue, front, rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return None
    rear = rear + 1
    queue[rear] = data


def peek():
    global Size, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[front+1]


Size = 5
queue = [None for _ in range(5)]
front = rear = -1


if __name__ == "__main__":
    en_queue("정국")
    en_queue("뷔")
    en_queue("지민")
    en_queue("진")
    en_queue("슈가")
    print("대기 줄 상태 : ", queue)

    for i in range(rear+1):
        print(de_queue(), "님 식당에 들어감")
        print("대기 줄 상태 : ", queue)

    print("식당 영업 종료!")
