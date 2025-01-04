def search_array_max(arr):
    max_num = len(arr)
    target_num = arr[0]
    for i in range(0, max_num):
        if arr[i] > target_num:
            target_num = arr[i]
    return target_num

if __name__ == '__main__':
    print(search_array_max([3, 21, 5, 4, 16, 13, 20, 19, 6, 5]))