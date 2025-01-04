def gcd(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

if __name__ == '__main__':
    a = 48
    b = 128
    print(gcd(a, b))