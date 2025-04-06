arr = [[3, 5, 8, 11, 15],
       [17, 20, 25, 32, 33],
       [40, 43, 51, 62, 71]]
i_max = len(arr) - 1
j_max = len(arr[0]) - 1

def search_dimensional_array(num):
    i = i_max
    j = 0
    while (i >= 0) and (j <= j_max):
        if arr[i][j] == num:
            return 'OK'
        elif arr[i][j] > num:
            i = i - 1
        else:
            j = j + 1
    return 'NG'

if __name__ == '__main__':
    print(search_dimensional_array(71))