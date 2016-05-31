def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False

print(is_factor(6, 18))
print(is_factor(6, 19))

