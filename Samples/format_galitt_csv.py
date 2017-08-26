import sys
# args = sys.argv
#  file_name = args[1]
file_name = "galitt"
# file_name = "20170825_OWU"
# #file_name = "20170825_YINN"
f_in = open("assets/" + file_name + ".csv", 'r')
lines = f_in.readlines()
f_in.close()

stacklines = list()
for line in lines:
    if line.startswith('"'):
        stacklines.append(line)
    else:
        preline = stacklines.pop()
        stacklines.append(preline.replace('\n','') + line)

f_out = open('assets/' + file_name + '_format.csv','w')
for stackline in stacklines:
    print(stackline.replace('\n',''))
    f_out.write(stackline)
f_out.close()
