import os

pds = []

rg = range(0, 10)

for three in rg:
    for four in rg:
        for five in rg:
            for six in rg:
                num = "%s%s%s%s" % (three, four, five, six)
                pds.append(num)

# file_object = open('/Users/edge/Desktop/pwdNum4.txt', 'w')
file_object = open('C:\Users\edge\Desktop\pwdNum4.txt', 'w')
file_object.writelines(['%s%s' % (x, os.linesep) for x in pds])
file_object.close()
