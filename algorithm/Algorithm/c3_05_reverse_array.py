def revers_array(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        temp = arr[right]
        arr[right] = arr[left]
        arr[left] = temp
        left += 1
        right -= 1
    return arr

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    print(revers_array(arr))