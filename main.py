#from turtle import *
from struct import pack

from person import Person
# from whoocus import package
# from whoocus.package import method
from whoocus.package import method



name = "こんにちは。たぢさん"
print("Hello " + name + " python!!")

print(name.index("ぢ"))
print(name.count("ん"))

p = Person("たぢ")
p.myName()


# method()
# package.method()
#whoocus.package.method()
method()