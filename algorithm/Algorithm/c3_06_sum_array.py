def sum_array(arr1, arr2):
    result = 0
    for i in range(0, len(arr2)):
        result += arr1[arr2[i]]
    return result

if __name__ == '__main__':
    arr1 = [3,8,5,4,16,13,7,9,6,5]
    arr2 = [2,4,7]
    print(sum_array(arr1, arr2))