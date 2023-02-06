def is_stack_full():
    global Size, stack, top
    if top >= Size - 1:
        return True
    return False


def is_stack_empty():
    global Size, stack, top
    if top == -1:
        return True
    return False


def push(data):
    global Size, stack, top
    if(is_stack_full()):
        return
    top = top + 1
    stack[top] = data


def pop():
    global Size, stack, top
    if(is_stack_empty()):
        return None
    data = stack[top]
    stack[top] = None
    top = top - 1
    return data


def peek():
    global Size, stack, top
    if (is_stack_empty()):
        return None
    return stack[top]


Size = 6
stack = [None for _ in range(Size)]
top = -1

if __name__ == "__main__":
    stone_array = ["주황", "초록", "파랑", "보라", "빨강", "노랑"]

    print("과자집에 가는길 : ", end=' ')
    for stone in stone_array:
        push(stone)
        print(stone, " >", end=' ')
    print("과자집")

    print("우리집에 오는길 : ", end=' ')
    while True:
        stone = pop()
        if stone == None:
            break
        print(stone, " >", end=' ')
    print("우리집")