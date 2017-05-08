
def is_integer(a):
    if  (a % 2) == 0:
        print(a)
        return

if __name__ == '__main__':
    list = range(1, 20)
    for l in list:
        is_integer(l)
