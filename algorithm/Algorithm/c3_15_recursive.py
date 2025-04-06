def recursive(n):
    if n <= 1:
        return 1
    else:
        return n + recursive(n - 1)

if __name__ == '__main__':
    print(recursive(4))