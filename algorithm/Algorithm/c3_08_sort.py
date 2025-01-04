arr = [3, 8, 9, 13, 14, 16, 21, 25, 31, 40, 15]
def sort(n):
    temp = arr[n]
    i = n - 1
    while arr[i] > temp:
        arr[i + 1] = arr[i]
        i = i - 1
    arr[i + 1] = temp
    print(arr)

if __name__ == '__main__':
    sort(10)