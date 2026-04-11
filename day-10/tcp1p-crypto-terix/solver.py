enc = [
    [82, 65, 77, 65], 
    [68, 65, 78, 123], 
    [69, 52, 115, 121], 
    [45, 99, 104, 52], 
    [108, 108, 95, 77], 
    [52, 116, 114, 49], 
    [120, 33, 125, 33]
]

flag = ''

for i in enc:
    for j in i:
        flag += chr(j)
        
print(flag)
# RAMADAN{E4sy-ch4ll_M4tr1x!}!
# RAMADAN{E4sy-ch4ll_M4tr1x!}