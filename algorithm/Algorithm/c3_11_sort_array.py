from c3_15_recursive import recursive

arry = [5, 2, 3, 4, 1]

def sort_array():
    for i in range(len(arry)):
        for j, val in reversed(list(enumerate(reversed(arry)))):
            if arry[j - 1] > arry[j]:
                tmp = arry[j]
                arry[j] = arry[j - 1]
                arry[j - 1] = tmp
            # print(f'j: {j}')
            # print(f'arry[j - 1]: {arry[j - 1]}')
            # print(f'arry[j]: {arry[j]}')
            # print('--------')
        print(arry)

if __name__ == '__main__':
    sort_array()