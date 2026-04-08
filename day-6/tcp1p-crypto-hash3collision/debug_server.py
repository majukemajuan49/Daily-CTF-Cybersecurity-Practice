#!/usr/bin/env python3

FLAG = "TCP1P{test_flag}"

# my very original hash function!!1!
def my_hash(string):
    sum = 0
    for char in string:
        sum += ord(char)
    sum = sum % 16777216
    return str(sum).encode().hex()

# username & hashed passwords
user_database = {
    'admin': '32323931', # 2291
    'user1': '32303638', # 2068
    'user2': '31333433', # 1343
}

logged_in = False
#ZZZZZZZZZZZZZZS

# main code
while True:
    print("""
        =================WELCOME=================
        1. Login
        2. Exit
        =========================================
        """)

    choose = input(">> ")

    if choose == "1":
        inp_username = input("Username: ")
        inp_password = input("Password: ")
        try:
            print(f"{my_hash(inp_password) = }")
            if my_hash(inp_password) == user_database[inp_username]:
                logged_in = True
                print("Login successful!")
            else:
                assert 1 == 0  # raise error, go to "except" codeblock
        except:
            print("Username or Password might be wrong...")

    elif choose == "2":
        print("Good Bye!")
        exit(0)

    else:
        print("Choose correctly!")
        continue

    while logged_in:
        print("""
        ===========WELCOME BACK, USER============
        1. Get Flag
        2. Logout
        =========================================
        """)

        choose = input(">> ")

        if choose == "1":
            print(f"Here is your flag: {FLAG}")
            exit(0)

        elif choose == "2":
            print("Logging out...")
            logged_in = False

        else:
            print("Choose correctly!")
            continue
# Challenge: Hash 3: Collision