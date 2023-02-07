def is_queue_full():
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front:
        return True
    else:
        return False


def is_queue_empty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def en_queue(data):
    global SIZE, queue, front, rear
    if is_queue_full():
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = data


def de_queue():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


def peek():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("큐가 비었습니다.")
        return None
    return queue[(front + 1) % SIZE]


def calc_time():
    global SIZE, queue, front, rear
    time = 0
    for i in range((front + 1) % SIZE, (rear + 1) % SIZE):
        time = time + queue[i][1]
    return time


SIZE = int(input("큐의 크기를 입력하세요 ==> "))
queue = [None for _ in range(SIZE)]
front = rear = 0


if __name__ == "__main__":
    call = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]

    for wait in call:
        print("귀하의 대기 예상시간은 ", calc_time(), "분입니다.")
        print("현재 대기 콜 --> ", queue)
        en_queue(call)
        print()

    print("최종 대기 콜 --> ", queue)
    print("프로그램 종료!")
