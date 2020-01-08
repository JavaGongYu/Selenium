import csv
import codecs
from itertools import islice

data = csv.reader(codecs.open("../date_file/read_csv.csv",'r','gbk'))

users = []

for l in islice(data,1,None):
    users.append(l)

print(users)