import yagmail

server = yagmail.SMTP(user='15554421975@163.com',password='gy961117',host="smtp.163.com")

contents=['正文','标题']

server.send('15554421975@163.com','subject',contents)