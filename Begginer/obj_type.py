v1 = 20
print(type(v1))
v2 = v1.__add__(15)
print(v1)
print(v2)

#--
s1 = "たぢ"
print(type(s1))
s2 = s1.__add__("さん")
print(s2)

#--
print("-----------------")
print("Info of int")
print("-----------------")
int_dir_list = dir(v1)
for i_dir in int_dir_list:
 print(i_dir)

#--
print("-----------------")
print("Info of str")
print("-----------------")
str_dir_list = dir(s1)
for s_dir in str_dir_list:
 print(s_dir)
