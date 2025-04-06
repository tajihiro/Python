bin = [None] * 32
n = 5

def print_bin():
    for i in range(1, n):
        print(f'{bin[i]}', end='')
    print('')


# noinspection PyTypeChecker
def binary_number(k):
    if k > n:
        print_bin()
    else:
        bin[k] = 0
        binary_number(k + 1)
        bin[k] = 1
        binary_number(k + 1)

if __name__ == '__main__':
    binary_number(0)