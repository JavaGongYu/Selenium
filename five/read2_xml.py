from xml.dom.minidom import parse

dom = parse('../date_file/config.xml')
root = dom.documentElement

login_info = root.getElementsByTagName('login')

username = login_info[0].getAttribute("username")
print(username)
password = login_info[0].getAttribute('password')
print(password)