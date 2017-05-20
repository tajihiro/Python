score_list = [34, 54, 98, 43, 56, 70, 68]
total = 0
for score in score_list:
  total += score
  print("累積：" + str(total))

print("-----------")
print("合計：{}点 / 合計数：{}".format(total,len(score_list)))
ave = total / len(score_list)
print("平均：{:.1f}点".format(ave))

print("-----------")
print("合計：" + str(sum(score_list)))

score_list.append(40)
print("合計：" + str(sum(score_list)))
