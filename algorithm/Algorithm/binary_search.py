btree = [[13, 1, 2], [10, 4, -1], [15, 3, 5],
             [14, -1, -1], [8, -1, -1], [16, -1, -1]]

def lookup(val):
    t = 0
    while t != -1:
        if val == btree[t][0]:
            return True
        elif val < btree[t][0]:
            t = btree[t][1]
        else:
            t = btree[t][2]
    return False

if __name__ == '__main__':
    print(lookup(3))