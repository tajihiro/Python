import numpy as np

x = np.array([1.0, 2.0, 3.0])
y = np.array([4.0, 5.0, 6.0])

z = x + y
print(type(x))
print(x)
print(y)
print('-------------')
print(z)
print(z / 2)

print(z[0])
print(z[1])
print(z[2])

for val in x:
  print(val)