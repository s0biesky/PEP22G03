def check_logs():
    users = []
    passwd = []
    for i in range(1, 4):
        users.append(input(f"User PC {i}: "))
        passwd.append(input(f"User password {i}: "))
    for i in range(3):
        print(f"{users[i]} --> {passwd[i]}")
check_logs()