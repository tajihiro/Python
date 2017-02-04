#from turtle import *
from struct import pack

from person import Person
# from whoocus import package
# from whoocus.package import method
#from whoocus.modules import method
from whoocus import modules

name = "こんにちは。たぢさん"
print("Hello " + name + " python!!")

print(name.index("ぢ"))
print(name.count("ん"))

p = Person("たぢ")
p.myName()


# method()
# package.method()
#whoocus.package.method()
modules.method()

# 米屋計算
sum = 1
for num in range(1,11):
  print(str(num) + "日目: " + str(sum) + "粒")
  sum =+ sum * 2
