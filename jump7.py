def is7Num(n = 7):
    if n % 7 == 0:
        print(n)
    elif n // 10 == 7:
        print(n)
    elif n % 10 == 7:
        print(n)

def test():
    for n in range(1, 101):
        is7Num(n)

if __name__ == '__main__':
    test()
