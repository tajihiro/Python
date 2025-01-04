def concat_array(x, y):
    len_x = len(x)
    len_y = len(y)
    result = [None] * (len_x + len_y)
    for i in range(len_x):
        result[i] = x[i]
    for i in range(len_y):
        result[len_x + i] = y[i]
    return result

if __name__ == '__main__':
    arr1 = ['A', 'p', 'p', 'l', 'e']
    arr2 = ['P', 'e', 'n']
    print(concat_array(arr1, arr2))