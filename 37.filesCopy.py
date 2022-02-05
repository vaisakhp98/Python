f=open("vaisakh.txt",'r')
s=f.read()
print(s)

f=open("vaisakh_cpy.txt",'w')
f.write(s)
f.close()