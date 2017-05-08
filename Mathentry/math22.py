

if __name__ == '__main__':
  simple_list = [1,2,3]
  print(simple_list[0])
  print(simple_list[1])
  print(simple_list[2])
#  print(simple_list[3])

  string_list = ['str1','str2','str3']
  print(string_list[0])
  string_list.append('str9')
  print(len(string_list))

  for list in string_list:
    print(list)

for key, value in enumerate(string_list):
  print(key, value)