def num(mc):
    mark_ct = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    i = 1
    for i, mark in enumerate(mark_ct):
        if mc == mark_ct[i]:
            i = i + 1
            break
    return i

def calc_score(marks):
    score = 0
    for i, mark in enumerate(marks):
        if mark == '+':
            score = score + num(marks[i + 1]) + 10
        elif mark == '-':
            score = score + num(marks[i - 1]) + 10
        else:
            score = score + num(marks[i])
    return score

if __name__ == '__main__':
    print(calc_score(["1", "+", "2", "-", "3", "6", "5"]))