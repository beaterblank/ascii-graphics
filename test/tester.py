import os
import asciianim as b
b.clear()
a = [['1','2',' '],[' ','4','5'],['6',' ',' ']]
os.system("")
run = False
string = ""
for i in range(len(a)):
    text=""
    if(i!=0):
        text+="\n"
    for j in range(len(a[0])):
        if(a[i][j]!=' '):
            run = True
        else:
            run = False
        if(run):
            x=i+1
            y=j+1
            text += "\x1b7\x1b["+str(x)+";"+str(y)+"f"+a[i][j]+"\x1b8"
    
    string+=text
string = string.strip()
print(string)
input()

