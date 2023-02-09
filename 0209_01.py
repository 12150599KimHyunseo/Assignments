def convertor(number, base):
    q, r = divmod(number, base)
    return convertor(q, base) + nums[r] if q else nums[r]


nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

print(convertor(11, 2))


if __name__ == "__main__":
    number = int(input('10진수 입력 --> '))
    print()
    print('2진수 : ', convertor(number, 2))
    print()
    print('8진수 : ', convertor(number, 8))
    print()
    print('16진수 : ', convertor(number, 16))
