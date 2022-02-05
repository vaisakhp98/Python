import filecmp

s=filecmp.cmp("vaisakh.txt",'vaisakh_cpy.txt')
print(s)