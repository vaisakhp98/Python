stri = "VAISAKH"
lists = list(stri)
c = 0

for i in lists:
    c = 0
    if i!= " ":
        for j in range (0,len(lists)):
            if i == lists[j]:
                c += 1
                lists[j] = " "
        print(f"{i} = {c}")
