def is_factor(a, b):
    if b % a == 0:
        return True
    else:
        return False

print(is_factor(6, 18))
print(is_factor(6, 19))

for i in range(1, 15):
    a = i
    b = i + 3 * 8
    print(str(a)  + '/' + str(b) + ':' + str(is_factor(a, b)))

# Python
print(3 / 2) # => 1.5
print(3 // 2) # => 1

print(5 % 2) # => 1
