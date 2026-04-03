# !@#$%^&*( is 123456789
# this is when you hold shift on the keyboard and type 123456789
dictionary = {
    '!': '1',
    '@': '2',
    '#': '3',
    '$': '4',
    '%': '5',
    '^': '6',
    '&': '7',
    '*': '8',
    '(': '9',
    ')': '0'
}

enc = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"
enc = enc.split(',')
flag = ''

for group in enc:
    temp = ''
    for char in group:
        temp += dictionary[char]
    flag += chr(int(temp))

print(flag)