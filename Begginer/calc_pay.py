hour_pay = input("時給は？")
work_hour = input("労働時間は？")
payment = int(hour_pay) * int(work_hour)

print("あなたの給料は、{:,}円です。".format(payment))