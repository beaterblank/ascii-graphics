with open("version.txt","r") as fh:
  v = fh.read()
k = v.split(".")
k = int("".join(k))+1
l = list(str(k)[::-1])
try:
    a = l[2]
except:
    a = 0
try:
    b = l[1]
except:
    b = 0
try:
    c = l[0]
except:
    c=0
l = f"{a}.{b}.{c}"
with open("version.txt","w") as fh:
    fh.write(str(l))
