arg = input("年齢をいれてください。")
age = float(arg)

if(age < 13):
  print("300円")
elif(13 <= age and age < 20):
  print("500円")
else:
  print("600円")

