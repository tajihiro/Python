a = {"田島","中村","千葉"}
b = {"守田","藤原","松本", "田島"}

c = a | b
print(c)

d = a & b
print(d)


c.add("中谷")
print(c)