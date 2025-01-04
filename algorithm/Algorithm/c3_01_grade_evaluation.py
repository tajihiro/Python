def grade_evaluation(score):
    result = ''
    if score >= 80:
        result = f'評価A : {score}点'
    elif score >= 60:
        result = f'評価B : {score}点'
    else:
        result = f'評価C : {score}点'
    return result

score = 59
print(grade_evaluation(score))
