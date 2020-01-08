import json
with open("../date_file/user_info.json",'r') as g:
    data = g.read()

user_list = json.loads(data)
print(user_list)
