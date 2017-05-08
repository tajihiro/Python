name = "田島啓之"
age = 45

#print(name + ' ' + age + "歳です。")
print(name + ' ' + str(age) + "歳です。")

fmt = "私の名前は、{name}です。{age}歳です。"
msg = fmt.format(age=age, name=name)
print(msg)