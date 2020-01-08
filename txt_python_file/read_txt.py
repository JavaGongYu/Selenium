with(open("../date_file/user_info.txt",'r')) as user_file:
     data = user_file.readlines()
users = []
for line  in data:
    user = line[:-1].split(":")
    users.append(user)
print(users)

