with(open("../date_file/user_info.txt",'r')) as user_file:
     data = user_file.readlines()
users = []
for line  in data:
    user = line[:].split(":")
    users.append(user)
#print(users)
print(users[0][0],users[0][1])
print(users[3][0],users[3][1])