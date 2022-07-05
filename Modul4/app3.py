# def check_logs():
#     users = []
#     passwd = []
#     for i in range(1, 4):
#         users.append(input(f"User PC {i}: "))
#         passwd.append(input(f"User password {i}: "))
#     for i in range(3):
#         print(f"{users[i]} --> {passwd[i]}")
# check_logs()

def credentiale():
    acces = {}
    for i in range(1, 4):
        acces[input(f"User PC {i}: ")] = input(f"User password {i}: ")
    for user, password in acces.items():
        print(f"{user} --> {password}")
    # print(acces)

credentiale()

