import re
import math

myfile = open("orig-xmastree.brd", "r")
myline = myfile.readline()
f = 1.2
l = 0
while myline:
    if l < 110 and myline.startswith("<wire "):
        x = re.findall('<wire x1="(.*)" y1="(.*)" x2="(.*)" y2="(.*)" width="0.1524" layer="20"/>', myline)
        x1 = round(float(x[0][0]) * f, 2);
        y1 = round(float(x[0][1]) * f, 2);
        x2 = round(float(x[0][2]) * f, 2);
        y2 = round(float(x[0][3]) * f, 2);
        print(f'<wire x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" width="0.1524" layer="20"/>', end='')
    else:
        print(myline, end='')
    l = l + 1
    myline = myfile.readline()
myfile.close()











