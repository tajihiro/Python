class Variable:
    def __init__(self, data):
        self.data = data


# import numpy as np
#
# data = np.array(1.0)
# print (data.ndim)
#
# x = Variable(data)
# print (x.data)
#
# x.data = np.array(2.0)
# print (x.data)
#
# class Function:
#     def __call__(self, input):
#         x = input.data
#         y = x ** 2
#         output = Variable(y)
#         return output
#
# x = Variable(np.array(10))
# f = Function()
# y = f(x)
#
# print (type(y))
# print (y.data)

