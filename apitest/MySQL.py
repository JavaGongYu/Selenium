import MySQLdb

mysql=MySQLdb.connect(
    host="127.0.0.1",
    user='root',
    password='123456',
    db='bbs',
    charset='utf8')

my = mysql.cursor()
for i in range(1000):
    my.execute("insert into test(username,age,sex,gps)values('jining{}',20,'W','jining{}')".format(i+1,i+1))

mysql.commit()

# for x in range(1000):
# #     my.execute("delete from test where id={}".format(x+1))
# #
# # mysql.commit()

my.execute("select * from test")

# row = my.fetchall()
# print(row)

for i in range(my.rowcount):
    row=my.fetchone()
    print(row)
    # if row[1] =='jinan':
    #     print("含有济南")